package controllers

import (
	"builder/models"
	"context"
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"cloud.google.com/go/storage"
	"github.com/gin-gonic/gin"
	"github.com/xuri/excelize/v2"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/option"
)

func Merge() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// list of reportIDs
		var inputJSONArr []string
		var now = time.Now()
		randNum := strconv.Itoa(rand.Int())
		var formattedNow = fmt.Sprintf("%d-%02d-%02dT%02d:%02d:%-2d", now.Year(), now.Month(), now.Day(), now.Hour(), now.Minute(), now.Second())

		err := ctx.BindJSON(&inputJSONArr)

		if err != nil {
			log.Panic(err)
		}
		fmt.Println(inputJSONArr)

		// query all the reportJSON
		reports := queryReports(inputJSONArr)

		// loop from second element onwards and
		// append to the "sheets" array in the first element

		// check reports does not have same sheet names
		isUniqueSheetNames := isUniqueSheetNames(reports)

		if !isUniqueSheetNames {
			ctx.AbortWithStatusJSON(
				http.StatusBadRequest,
				gin.H{
					"message": "sheet name must be unique",
				},
			)
			return
		}

		reportJSON := mergeSheets(reports)

		sheets := ConvertJSONToExcelCompatibleFormat(reportJSON)

		var fileName = reportJSON.ReportName + "_" + formattedNow + randNum + ".xlsx"

		//var fileName = request.ReportName + ".xlsx"

		f := excelize.NewFile()

		if !GenerateSheets(f, sheets) {
			log.Panic("invalid sheet name")

			ctx.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
				"message": "Invalid sheet name supplied",
			})
			return
		}
		GenerateCells(f, sheets)

		FitColumns(f, sheets)

		// save directory for cloud run
		err = f.SaveAs("/tmp/" + fileName)

		//err = f.SaveAs(fileName)

		if err != nil {
			log.Panic("error saving file")

			ctx.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{
				"message": err,
			})
			return
		}

		file, err := os.Open("/tmp/" + fileName)
		if err != nil {
			log.Panic("error opening file")
			ctx.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{
				"message": err,
			})
			return
		}

		//upload to cloud storage
		cloudCtx := context.Background()

		client, err := storage.NewClient(cloudCtx, option.WithCredentialsFile("service_account.json"))

		if err != nil {
			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError,
				gin.H{
					"message": err,
				},
			)
			return
		}

		//defer file.Close()
		wc := client.Bucket(BUCKET_NAME).Object(fileName).NewWriter(ctx)

		wc.ContentType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

		_, err = io.Copy(wc, file)

		if err != nil {
			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError,
				gin.H{
					"message": err,
				},
			)
			return
		}

		if err := wc.Close(); err != nil {
			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError,
				gin.H{
					"message": err,
				},
			)
			return
		}

		//delete directory for cloud run
		os.Remove("/tmp/" + fileName)

		//os.Remove(fileName)

		if err != nil {
			log.Panic("error removing file")
			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError, gin.H{
					"message": err,
				},
			)
			return
		}

		saKey, err := ioutil.ReadFile("service_account.json")
		if err != nil {
			log.Panic(err)
		}
		cfg, err := google.JWTConfigFromJSON(saKey)
		if err != nil {
			log.Panic(err)
		}

		url, err := storage.SignedURL(BUCKET_NAME, fileName, &storage.SignedURLOptions{

			GoogleAccessID: cfg.Email,
			PrivateKey:     cfg.PrivateKey,
			Method:         "GET",
			Expires:        time.Now().Add(time.Minute * 60),
		})

		if err != nil {
			log.Panic("error generating signed URL")
			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError,
				gin.H{
					"message": "error generating signed URL",
					"err":     err,
				},
			)
		}

		ctx.IndentedJSON(
			http.StatusOK,
			gin.H{
				"url": url,
				//"sheets": sheets,
			},
		)

	}
}

func contains(s []string, str string) bool {
	for _, sheetName := range s {
		if sheetName == str {
			return true
		}
	}
	return false
}

func isUniqueSheetNames(reports []models.ReportJSON) bool {

	sheetNameArr := []string{}

	for _, report := range reports {
		if contains(sheetNameArr, report.RawSheets[0].SheetName) {
			return false
		} else {
			sheetNameArr = append(sheetNameArr, report.RawSheets[0].SheetName)
		}
	}

	return true
}

func mergeSheets(reports []models.ReportJSON) models.ReportJSON {

	mainReport := reports[0]

	for _, report := range reports[1:] {
		sheet := report.RawSheets[0]
		mainReport.RawSheets = append(mainReport.RawSheets, sheet)
	}

	return mainReport
}

func queryReports(reportIDArry []string) []models.ReportJSON {
	reports := []models.ReportJSON{}
	for _, id := range reportIDArry {
		url := fmt.Sprintf(`https://formatter-container-2b4cd56mpa-as.a.run.app/render?reportID=%s`, id)

		resp, err := http.Get(url)

		if err != nil {
			log.Panic(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode == 200 {
			fmt.Println("is 200")
			var report models.ReportJSON
			//b, err := ioutil.ReadAll(resp.Body)

			if err != nil {
				log.Panic(err)
			}

			err = json.NewDecoder(resp.Body).Decode(&report)

			if err != nil {
				log.Panic(err)
			}
			reports = append(reports, report)
		}

	}
	return reports

}

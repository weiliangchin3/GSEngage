package controllers

import (
	"builder/models"
	"context"
	"io"
	"io/ioutil"
	"os"

	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"cloud.google.com/go/storage"
	"github.com/gin-gonic/gin"
	"github.com/xuri/excelize/v2"
	"golang.org/x/oauth2/google"
	"google.golang.org/api/option"
)

const (
	// S3_REGION   = "ap-southeast-1"
	// S3_BUCKET   = "reports-test-four-horsemen"
	PROJECT_ID  = "goldman-hackathon"
	BUCKET_NAME = "gs-report-bucket"
)

func D() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		// params := ctx.Request.URL.Query()

		// reportID := params["reportID"][0]

		// report := GetReport(reportID)

		var report models.ReportJSON

		var sheets []models.Sheet
		var now = time.Now()
		randNum := strconv.Itoa(rand.Int())
		var formattedNow = fmt.Sprintf("%d-%02d-%02dT%02d:%02d:%-2d", now.Year(), now.Month(), now.Day(), now.Hour(), now.Minute(), now.Second())

		err := ctx.BindJSON(&report)
		if err != nil{
			log.Panic(err)
		}

		if IsValidReportName(report.ReportName) {
			log.Panic("invalid report name")

			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError, gin.H{
					"message": "Invalid report name",
				},
			)
			return
		}

		var fileName = report.ReportName + "_" + formattedNow + randNum + ".xlsx"

		//var fileName = request.ReportName + ".xlsx"

		f := excelize.NewFile()

		sheets = ConvertJSONToExcelCompatibleFormat(report)

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
				//"report": report,
				"url":    url,
				//"sheets": sheets,
			},
		)
	}
}

func Download() gin.HandlerFunc {
	return func(ctx *gin.Context) {
		params := ctx.Request.URL.Query()

		reportID := params["reportID"][0]

		report := GetReport(reportID)

		var sheets []models.Sheet
		var now = time.Now()
		randNum := strconv.Itoa(rand.Int())
		var formattedNow = fmt.Sprintf("%d-%02d-%02dT%02d:%02d:%-2d", now.Year(), now.Month(), now.Day(), now.Hour(), now.Minute(), now.Second())

		fmt.Println(report.ReportName)

		if IsValidReportName(report.ReportName) {
			log.Panic("invalid report name")

			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError, gin.H{
					"message": "Invalid report name",
				},
			)
			return
		}

		var fileName = report.ReportName + "_" + formattedNow + randNum + ".xlsx"

		//var fileName = request.ReportName + ".xlsx"

		f := excelize.NewFile()

		sheets = ConvertJSONToExcelCompatibleFormat(report)

		if !GenerateSheets(f, sheets) {
			log.Panic("invalid sheet name")

			ctx.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
				"message": "Invalid sheet name supplied",
			})
			return
		}
		GenerateCells(f, sheets)

		FitColumns(f, sheets)

		//save directory for cloud run
		err := f.SaveAs("/tmp/" + fileName)

		//err := f.SaveAs(fileName)

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

package main

import (
	"builder/controllers"
	"builder/models"
	"fmt"
	"log"
	"math/rand"
	"net/http"
	"strconv"
	"time"

	"github.com/gin-contrib/cors"
	"github.com/gin-gonic/gin"
	"github.com/xuri/excelize/v2"
)

// const (
// 	// S3_REGION   = "ap-southeast-1"
// 	// S3_BUCKET   = "reports-test-four-horsemen"
// 	PROJECT_ID  = "goldman-hackathon"
// 	BUCKET_NAME = "gs-report-bucket"
// )

// var S3_KEY_ID = os.Getenv("S3_KEY_ID")
// var S3_SECRET_KEY = os.Getenv("S3_SECRET_KEY")

//var storageClient *storage.Client

func main() {
	gin.SetMode(gin.ReleaseMode)
	server := gin.Default()
	server.Use(cors.Default())
	log.Printf("starting server...")

	// verify jwt token
	// server.Use(func(c *gin.Context) {
	// 	client := &http.Client{}
	// 	authHeader := c.Request.Header.Get("Authorization")
	// 	if authHeader == "" {
	// 		c.AbortWithStatusJSON(
	// 			http.StatusUnauthorized, gin.H{
	// 				"message": "no token supplied",
	// 			},
	// 		)
	// 		return
	// 	}

	// 	req, _ := http.NewRequest("GET", "https://jwt-2b4cd56mpa-as.a.run.app/verify", nil)

	// 	req.Header.Set("Authorization", authHeader)

	// 	res, _ := client.Do(req)

	// 	if res.StatusCode == 200 {
	// 		c.Next()
	// 	} else {
	// 		c.AbortWithStatusJSON(
	// 			res.StatusCode,
	// 			gin.H{
	// 				//"message" : "error",
	// 			},
	// 		)
	// 		return
	// 	}

	// })

	server.GET("/ping", func(c *gin.Context) {
		c.IndentedJSON(http.StatusOK, "OK")

	})

	server.POST("/d", func(ctx *gin.Context) {

		var reportJSON models.ReportJSON
		var sheets []models.Sheet
		var now = time.Now()
		randNum := strconv.Itoa(rand.Int())
		var formattedNow = fmt.Sprintf("%d-%02d-%02dT%02d:%02d:%-2d", now.Year(), now.Month(), now.Day(), now.Hour(), now.Minute(), now.Second())

		err := ctx.BindJSON(&reportJSON)

		if err != nil {
			log.Panic(err)
		}

		fmt.Println(reportJSON.ReportName)

		if err != nil {
			log.Panic(err)
		}

		if controllers.IsValidReportName(reportJSON.ReportName) {
			log.Panic("invalid report name")

			ctx.AbortWithStatusJSON(
				http.StatusInternalServerError, gin.H{
					"message": "Invalid report name",
				},
			)
			return
		}

		sheets = controllers.ConvertJSONToExcelCompatibleFormat(reportJSON)

		var fileName = reportJSON.ReportName + "_" + formattedNow + randNum + ".xlsx"

		//var fileName = request.ReportName + ".xlsx"

		f := excelize.NewFile()

		if !controllers.GenerateSheets(f, sheets) {
			log.Panic("invalid sheet name")

			ctx.AbortWithStatusJSON(http.StatusBadRequest, gin.H{
				"message": "Invalid sheet name supplied",
			})
			return
		}
		controllers.GenerateCells(f, sheets)

		controllers.FitColumns(f, sheets)

		// save directory for cloud run
		//err = f.SaveAs("/tmp/" + fileName)

		err = f.SaveAs(fileName)

		if err != nil {
			log.Panic("error saving file")

			ctx.AbortWithStatusJSON(http.StatusInternalServerError, gin.H{
				"message": err,
			})
			return
		}

		ctx.IndentedJSON(
			http.StatusOK,
			gin.H{
				//"url":    url,
				"sheets": sheets,
			},
		)

	})

	server.POST("/download", controllers.Download())
	server.POST("/download/v2", controllers.D())

	server.POST("/merge", controllers.Merge())

	server.Run(":8080")

}

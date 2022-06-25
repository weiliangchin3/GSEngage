package controllers

import (
	"builder/models"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func GetReport(reportID string) models.ReportJSON {
	url := fmt.Sprintf(`https://formatter-container-2b4cd56mpa-as.a.run.app/render?reportID=%s`, reportID)
	//url := fmt.Sprintf(`http://localhost:8080/render?reportID=%s`, reportID)


	resp, err := http.Get(url)

	if err != nil{
		log.Panic(err)
	}

	var report models.ReportJSON

	if resp.StatusCode == 200{
		
		fmt.Println("is 200")
		body, err := ioutil.ReadAll(resp.Body)

		if err != nil{
			log.Panic(err)
		}

		err = json.Unmarshal(body, &report)

		if err != nil{
			log.Panic(err)
		}
	}

	return report


	

}
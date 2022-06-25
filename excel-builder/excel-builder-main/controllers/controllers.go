package controllers

import (
	"builder/models"
	"builder/styles"
	"strconv"
	"strings"
	"unicode/utf8"

	"github.com/xuri/excelize/v2"
)

const WHITE string = "#FFFFFF"
const YELLOW string = "#FFFF00"
const TEAL string = "#01FFFF"
const RED string = "#FF0000"
const BLACK string = "#000000"
const GREEN string = "#ADFF2E"
const BLUE string = "#366092"

func updateCellProperties(obj models.CellObject, cell *models.Cell) {

	fo := excelize.Font{}

	fil := excelize.Fill{
		Color: []string{},
	}

	props := strings.Split(obj.ClassName, " ")

	if strings.Contains(obj.Value, "="){
		cell.IsFormula = true
	}

	for _, prop := range props {
		// data type
		if strings.Contains(prop, "dType") {
			switch prop {
			case "dType_decimal":
				// check if "." is in string. If present
				// it is a float else it is normal int
				if strings.Contains(obj.Value, ".") {
					cell.IsFloat = true
					cell.CellStyle.DecimalPlaces = 2
					cell.CellStyle.NumFmt = 39
				} else {
					cell.IsInteger = true
					cell.CellStyle.NumFmt = 39
				}

			case "dType_double":
				cell.IsFloat = true
				cell.CellStyle.DecimalPlaces = 2
				cell.CellStyle.NumFmt = 39

			}

			// text color
		} else if strings.Contains(prop, "text") {
			c := ""

			switch prop {
			case "white_text":
				//cell.CellStyle.Font.Color = WHITE
				c = WHITE
			case "yellow_text":
				//cell.CellStyle.Font.Color = WHITE
				c = YELLOW
			case "teal_text":
				//cell.CellStyle.Font.Color = WHITE
				c = TEAL
			case "green_text":
				//cell.CellStyle.Font.Color = WHITE
				c = GREEN
			case "red_text":
				//cell.CellStyle.Font.Color = WHITE
				c = RED
			case "black_text":
				//cell.CellStyle.Font.Color = WHITE
				c = BLACK
			}

			fo.Color = c

			cell.CellStyle.Font = &fo
			// highlight cell
		} else if strings.Contains(prop, "highlight") {

			switch prop {
			case "yellow_highlight":
				fil.Type = "pattern"
				fil.Color = append(fil.Color, YELLOW)
				fil.Pattern = 1

			case "teal_highlight":
				fil.Type = "pattern"
				fil.Color = append(fil.Color, TEAL)
				fil.Pattern = 1

			case "blue_highlight":
				fil.Type = "pattern"
				fil.Color = append(fil.Color, BLUE)
				fil.Pattern = 1

			case "green_highlight":
				fil.Type = "pattern"
				fil.Color = append(fil.Color, GREEN)
				fil.Pattern = 1

			case "red_highlight":
				fil.Type = "pattern"
				fil.Color = append(fil.Color, RED)
				fil.Pattern = 1

			}
			cell.CellStyle.Fill = fil
			// align text
		} else if strings.Contains(prop, "align") {
			h := ""
			switch prop {
			case "left_align":
				h = "left"
			case "center_align":
				h = "center"
			case "right_align":
				h = "right"
			}
			Alig := excelize.Alignment{
				Horizontal: h,
			}

			cell.CellStyle.Alignment = &Alig

		} else if strings.Contains(prop, "bold") {
			fo.Bold = true
		} else if strings.Contains(prop, "border") {
			var b []excelize.Border
			black := "#000000"

			leftBorder := excelize.Border{
				Type:  "left",
				Color: black,
				Style: 1,
			}

			rightBorder := excelize.Border{
				Type:  "right",
				Color: black,
				Style: 1,
			}

			topBorder := excelize.Border{
				Type:  "top",
				Color: black,
				Style: 1,
			}

			bottomBorder := excelize.Border{
				Type:  "bottom",
				Color: black,
				Style: 1,
			}

			switch prop {
			case "border_left_right_top_bottom":
				b = append(b, leftBorder)
				b = append(b, rightBorder)
				b = append(b, topBorder)
				b = append(b, bottomBorder)

			case "border_left_top_bottom":
				b = append(b, leftBorder)
				b = append(b, topBorder)
				b = append(b, bottomBorder)

			case "border_right_top_bottom":
				b = append(b, rightBorder)
				b = append(b, topBorder)
				b = append(b, bottomBorder)

			case "border_left":
				b = append(b, leftBorder)
			case "border_right":
				b = append(b, rightBorder)
			case "border_top":
				b = append(b, topBorder)
			case "border_bottom":
				b = append(b, bottomBorder)

			case "border_left_top":
				b = append(b, leftBorder)
				b = append(b, topBorder)
			case "border_left_right":
				b = append(b, leftBorder)
				b = append(b, rightBorder)
			case "border_left_bottom":
				b = append(b, leftBorder)
				b = append(b, bottomBorder)
			case "border_top_bottom":
				b = append(b, topBorder)
				b = append(b, bottomBorder)
			case "border_right_bottom":
				b = append(b, rightBorder)
				b = append(b, bottomBorder)
			}
			cell.CellStyle.Border = b
		}

	}

	//fmt.Println("class properties ", props)
}

func ConvertJSONToExcelCompatibleFormat(request models.ReportJSON) []models.Sheet {
	var alphaColumn = []string{"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", 
	"AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ","AK","AL","AM","AN","AO","AP","AQ","AR","AS","AT","AU","AV","AW","AX","AY", "AZ"}
	var sheets []models.Sheet

	for _, rawSheet := range request.RawSheets {
		var sheet models.Sheet
		sheet.SheetName = rawSheet.SheetName
		//sheet.SheetSettings = rawSheet.SheetSettings
		// row loop
		for i, row := range rawSheet.Rows {
			// column loop
			for j, obj := range row {
				//if obj.Value != "" {
				var cell models.Cell
				var cellAddress string = alphaColumn[j] + strconv.Itoa((i + 1))

				cell.Label = obj.Value
				cell.CellAddress = cellAddress

				//var style *models.Style = new(models.Style)

				// need to check the styles to add here
				updateCellProperties(obj, &cell)

				sheet.Cells = append(sheet.Cells, cell)
				//}
			}

		}
		sheets = append(sheets, sheet)
	}
	return sheets
}

func GenerateSheets(f *excelize.File, sheets []models.Sheet) bool {
	for _, sheet := range sheets {
		if !IsInValidSheetName(sheet.SheetName) {
			f.NewSheet(sheet.SheetName)
			// if index == len(request.Sheets)-1{
			// 	index = -1
			// }
			//fmt.Println("index is", index)

			// to toggle gridlines
			//SetSheetProerties(f, sheet, -1)
		} else {
			return false
		}
	}
	f.DeleteSheet("Sheet1")
	return true

}

func GenerateCells(f *excelize.File, sheets []models.Sheet) {
	for _, sheet := range sheets {
		for _, cell := range sheet.Cells {
			cellAddress := cell.CellAddress
			label := cell.Label

			validateCellType(cell, sheet, cellAddress, label, f)

			//f.SetColWidth(sheet.SheetName, cellAddress[0:1], cellAddress[0:1], float64(largestWidth))

			styles.ApplyStyles(f, cell, sheet.SheetName)
		}
	}
}

// func GenerateTables(f *excelize.File, request models.GenerateReportRequestBody) {
// 	largestWidth := 0
// 	for _, sheet := range request.Sheets {
// 		for _, table := range sheet.Tables {
// 			if IsValidTable(table) {
// 				for _, cell := range table.Cells {
// 					// add padding

// 					cellWidth := utf8.RuneCountInString(cell.Label) + 2
// 					cellAddress := cell.CellAddress
// 					label := cell.Label

// 					if cellWidth > largestWidth {
// 						largestWidth = cellWidth
// 					}

// 					validateCellType(cell, sheet, cellAddress, label, f)

// 					//f.SetColWidth(sheet.SheetName, cellAddress[0:1], cellAddress[0:1], float64(largestWidth))

// 					styles.ApplyStyles(f, cell, sheet.SheetName)
// 				}
// 			}

// 		}
// 	}

// }

// func GenerateSingleValues(f *excelize.File, request models.GenerateReportRequestBody) {
// 	for _, sheet := range request.Sheets {
// 		for _, cell := range sheet.SingleValues {
// 			cellAddress := cell.CellAddress
// 			label := cell.Label

// 			validateCellType(cell, sheet, cellAddress, label, f)

// 			//f.SetColWidth(sheet.SheetName, cellAddress[0:1], cellAddress[0:1], float64(largestWidth))

// 			styles.ApplyStyles(f, cell, sheet.SheetName)
// 		}
// 	}
// }

// func GenerateLabels(f *excelize.File, request models.GenerateReportRequestBody) {
// 	largestWidth := 0
// 	for _, sheet := range request.Sheets {
// 		for _, cell := range sheet.Labels {
// 			cellWidth := utf8.RuneCountInString(cell.Label) + 2

// 			if cellWidth > largestWidth {
// 				largestWidth = cellWidth
// 			}

// 			cellAddress := cell.CellAddress
// 			label := cell.Label

// 			f.SetCellValue(sheet.SheetName, cellAddress, label)

// 			//f.SetColWidth(sheet.SheetName, cellAddress[0:1], cellAddress[0:1], float64(largestWidth))

// 			styles.ApplyStyles(f, cell, sheet.SheetName)
// 		}
// 	}
// }

// func SetSheetProerties(f *excelize.File, sheet models.Sheet, index int) {

// 	if !sheet.SheetSettings.DisplayGridLines {
// 		//	fmt.Println("gridlines is", sheet.SheetSettings.DisplayGridLines)
// 		//fmt.Println("index is", index)
// 		f.SetSheetViewOptions(sheet.SheetName, index, excelize.ShowGridLines(false))

// 	}

// }

// func GenerateChartSourceData(f *excelize.File, request models.GenerateReportRequestBody) {
// 	categories := map[string]string{
// 		"A2": "Small", "A3": "Normal", "A4": "Large", "B1": "Apple", "C1": "Orange", "D1": "Pear"}
// 	values := map[string]int{
// 		"B2": 2, "C2": 3, "D2": 3, "B3": 5, "C3": 2, "D3": 4, "B4": 6, "C4": 7, "D4": 8}
// 	f.NewSheet("chart_source_data")
// 	for k, v := range categories {
// 		f.SetCellValue("chart_source_data", k, v)
// 	}
// 	for k, v := range values {
// 		f.SetCellValue("chart_source_data", k, v)
// 	}
// }

// func GenerateCharts(f *excelize.File, request models.GenerateReportRequestBody) {
// 	if err := f.AddChart("Sheet1", "B10", `{
//         "type": "line",
//         "series": [
//         {
//             "name": "chart_source_data!$A$2",
//             "categories": "chart_source_data!$B$1:$D$1",
//             "values": "chart_source_data!$B$2:$D$2"
//         },
//         {
//             "name": "chart_source_data!$A$3",
//             "categories": "chart_source_data!$B$1:$D$1",
//             "values": "chart_source_data!$B$3:$D$3"
//         },
//         {
//             "name": "chart_source_data!$A$4",
//             "categories": "chart_source_data!$B$1:$D$1",
//             "values": "chart_source_data!$B$4:$D$4"
//         }],
//         "format":
//         {
//             "x_scale": 2.0,
//             "y_scale": 2.0,
//             "x_offset": 0,
//             "y_offset": 0,
//             "print_obj": true,
//             "lock_aspect_ratio": false,
//             "locked": false
//         },
//         "legend":
//         {
//             "position": "top",
//             "show_legend_key": false
//         },
//         "title":
//         {
//             "name": "Fruit Line Chart"
//         },
//         "plotarea":
//         {
//             "show_bubble_size": true,
//             "show_cat_name": false,
//             "show_leader_lines": false,
//             "show_percent": true,
//             "show_series_name": true,
//             "show_val": true
//         },
//         "show_blanks_as": "zero"
//     }`); err != nil {
// 		fmt.Println(err)
// 	}
// }

func IsInValidSheetName(sheetName string) bool {
	return sheetName == ""
}

func IsValidTable(table models.Table) bool {
	if len(table.Cells) == 0 {
		return false
	} else {
		for _, cell := range table.Cells {
			// no cell address
			if cell.CellAddress == "" {
				return false
			}
		}
	}
	return true
}

func IsValidReportName(reportName string) bool {
	return reportName == ""
}

func validateCellType(cell models.Cell, sheet models.Sheet, cellAddress string, label string, f *excelize.File) {
	var isNegative bool = false
	if cell.IsFormula {
		f.SetCellFormula(sheet.SheetName, cellAddress, label)
	} else if cell.IsInteger {
		if label[0:1] == "-" {
			isNegative = true
			label = label[1:]
		}
		label, _ := strconv.Atoi(label)

		if isNegative {
			label = convertNegativeInt(label)
			//fmt.Println("converted negative value is ", label)
		}
		f.SetCellInt(sheet.SheetName, cellAddress, label)
	} else if cell.IsFloat {
		if label[0:1] == "-" {
			isNegative = true
			label = label[1:]
		}
		if label, err := strconv.ParseFloat(label, 64); err == nil {
			//fmt.Println("float is ", label)
			//labelNum := new(Number(label)).toFixed(2)

			// if cell.IsPercentage{
			// 	label = label / 10
			// }

			if isNegative {
				label = convertNegativeFloat(label)
			}

			//fmt.Println("label is ", label)

			f.SetCellFloat(sheet.SheetName, cellAddress, label, cell.CellStyle.DecimalPlaces, 64)
		}
	} else {

		f.SetCellValue(sheet.SheetName, cellAddress, label)

	}

}

func convertNegativeInt(value int) int {
	return value * -1
}

func convertNegativeFloat(value float64) float64 {
	return value * -1
}

func FitColumns(f *excelize.File, sheets []models.Sheet) {

	for _, sheet := range sheets {
		cols, _ := f.GetCols(sheet.SheetName)
		for idx, col := range cols {
			largestWidth := 0
			for _, rowCell := range col {
				//cellWidth := utf8.RuneCountInString(rowCell) + 6 // + 2 for margin
				cellWidth := utf8.RuneCountInString(rowCell) // + 2 for margin
				if cellWidth > largestWidth {
					largestWidth = cellWidth
				}
			}
			name, _ := excelize.ColumnNumberToName(idx + 1)

			f.SetColWidth(sheet.SheetName, name, name, float64(largestWidth))
		}
	}

}

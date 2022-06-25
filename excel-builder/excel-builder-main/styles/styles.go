package styles

import (
	"builder/models"
	"log"

	"github.com/xuri/excelize/v2"
)

func ApplyStyles(f *excelize.File, cell models.Cell, sheetName string) {
	if cell.IsMerge {
		//fmt.Println("is merge")
		f.MergeCell(sheetName, cell.CellAddress, cell.MergeAddress)
	}

	style, err := f.NewStyle(
		&cell.CellStyle,
	)

	if err != nil {
		log.Panic(err)
	}
	if cell.IsMerge {
		f.SetCellStyle(sheetName, cell.CellAddress, cell.MergeAddress, style)

	} else {
		f.SetCellStyle(sheetName, cell.CellAddress, cell.CellAddress, style)

	}
	//print("style is ", style)

}

package models

import "github.com/xuri/excelize/v2"

// type GenerateReportRequestBody struct {
// 	ReportName string `json:"reportName"`
// 	Sheets []Sheet `json:"sheets"`
// }

// type ReportRenderWithoutInptus struct{
// 	ReportJSON ReportJSON `json:"report"`
// }

type ReportJSON struct {
	ReportID int `json:"reportId"`
	TemplateName string `json:"templateName"`
	ReportName string     `json:"reportName"`
	RawSheets  []RawSheet `json:"sheets"`
}

type RawSheet struct {
	SheetName string        `json:"sheetName"`
	RawInputs []interface{} `json:"rawInputs"`
	//SheetSettings *SheetSettings `json:"sheetSettings"`
	Rows [][]CellObject `json:"rows"`
}

type CellObject struct {
	Value     string 
	ClassName string
	IsKey     bool
	KeyType   string
	Key       string
}

type Sheet struct {
	SheetName string `json:"sheetName"`
	//SheetSettings *SheetSettings `json:"sheetSettings"`
	Cells []Cell `json:"cells"`

	// Tables    []Table `json:"tables"`
	// Labels     []Cell  `json:"labels"`
	// SingleValues []Cell `json:"singleValues"`
}

type Table struct {
	Cells []Cell `json:"cells"`
}

type Cell struct {
	Label          string `json:"label"`
	CellAddress    string `json:"cellAddress"`
	CellStyle      excelize.Style  `json:"cellStyle"`
	IsMerge        bool   `json:"isMerge"`
	MergeAddress   string `json:"mergeAddress"`
	IsFormula      bool   `json:"isFormula"`
	IsInteger      bool   `json:"isInteger"`
	IsFloat        bool   `json:"isFloat"`
	FloatPrecision int    `json:"floatPrecision"`
	IsPercentage   bool   `json:"isPercentage"`
}

// type Style struct {
// 	Border        []Border   `json:"border"`
// 	Fill          Fill       `json:"fill"`
// 	Font          Font       `json:"font"`
// 	Alignment     Alignment  `json:"alignment"`
// 	Protection    Protection `json:"protection"`
// 	NumFmt        int        `json:"number_format"`
// 	DecimalPlaces int        `json:"decimal_places"`
// 	CustomNumFmt  string     `json:"custom_number_format"`
// 	Lang          string     `json:"lang"`
// 	NegRed        bool       `json:"negred"`
// }

type Protection struct {
	Hidden bool `json:"hidden"`
	Locked bool `json:"locked"`
}

type Fill struct {
	Type    string   `json:"type"`
	Pattern int      `json:"pattern"`
	Color   []string `json:"color"`
	Shading int      `json:"shading"`
}

// type Border struct {
// 	Type  string `json:"type"`
// 	Color string `json:"color"`
// 	Style int    `json:"style"`
// }

type Alignment struct {
	Horizontal      string `json:"horizontal"`
	Indent          int    `json:"indent"`
	JustifyLastLine bool   `json:"justify_last_line"`
	ReadingOrder    uint64 `json:"reading_order"`
	RelativeIndent  int    `json:"relative_indent"`
	ShrinkToFit     bool   `json:"shrink_to_fit"`
	TextRotation    int    `json:"text_rotation"`
	Vertical        string `json:"vertical"`
	WrapText        bool   `json:"wrap_text"`
}

type Font struct {
	Bold      bool    `json:"bold"`
	Italic    bool    `json:"italic"`
	Underline string  `json:"underline"`
	Family    string  `json:"family"`
	Size      float64 `json:"size"`
	Strike    bool    `json:"strike"`
	Color     string  `json:"color"`
}

type SheetSettings struct {
	DisplayGridLines bool `json:"displayGridLines"`
}

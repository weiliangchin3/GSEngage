package tests

import (
	"builder/controllers"
	"testing"
)

// func TestValidTable(t *testing.T) {
// 	var testCases = []struct {
// 		input    models.Table
// 		expected bool
// 	}{
// 		//empty table
// 		{models.Table{}, false},

// 		// cell without cell address
// 		{models.Table{
// 			Cells: []models.Cell{
// 				{
// 					CellAddress: "",
// 				},

// 			},
// 		}, false},

// 		// cell with valid cell address
// 		{models.Table{
// 			Cells: []models.Cell{
// 				{
// 					CellAddress: "A5",
// 				},

// 			},
// 		}, true},
// 	}
// 	for _, test := range testCases {
// 		if output := controllers.IsValidTable(test.input); output != test.expected {
// 			t.Errorf("Test Failed: %v inputted, %v expected, received %v", test.input, test.expected, output)
// 		}
// 	}
// }

func TestValidSheetName(t *testing.T) {
	var testCases = []struct {
		input    string
		expected bool
	}{
		// empty sheet name
		{"", false},

		{"sheet1", true},
	}

	for i, test := range testCases {
		if output := !controllers.IsInValidSheetName(test.input); output != test.expected {
			t.Errorf("Test %v Failed: %v inputted, %v expected, received %v",i ,test.input, test.expected, output)
		}
	}

}

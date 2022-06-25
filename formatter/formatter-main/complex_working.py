import copy

## complex
complex_json = {
    "reportId": 2105265855,
    "templateName": "complex_report",
    "reportName": "complex_testing",
    "sheets": [
        {
            "sheetName": "test_sheet",
            "keysDataType": {
                "daysInflow": "decimal",
                "assetCode": "string",
                "daysOutflow": "decimal",
                "daysOutflowCalc": "decimal",
                "previousMonthNAV": "decimal",
                "groupAccount": "string",
                "outflow": "decimal",
                "currentMonthNAV": "decimal",
                "exposure": "decimal",
                "reportDate_Day": "decimal",
                "assetName": "string",
                "inflow": "decimal",
                "daysInflowCalc": "decimal",
                "compositionRate": "decimal"
            },
            "rawInputs": [
                {
                    "groupAccount": "132132",
                    "outflow": 23854338,
                    "assetCode": "100",
                    "assetName": "クッキー",
                    "daysOutflow": 10.40232405527246,
                    "daysOutflowCalc": 7833894
                },
                {
                    "groupAccount": "132132",
                    "outflow": 0,
                    "assetCode": "200",
                    "assetName": "MONDAY(MON)",
                    "daysOutflow": 0,
                    "daysOutflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "outflow": 16540500,
                    "assetCode": "300",
                    "assetName": "チョコレート(CHOC)",
                    "daysOutflow": 24,
                    "daysOutflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "outflow": 0,
                    "assetCode": "400",
                    "assetName": "コーヒー(COF)",
                    "daysOutflow": 0,
                    "daysOutflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "outflow": 0,
                    "assetCode": "500",
                    "assetName": "PA(パイナップル)",
                    "daysOutflow": 0,
                    "daysOutflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "daysInflow": 24,
                    "assetCode": "100",
                    "reportDate_Day": 30,
                    "assetName": "クッキー",
                    "inflow": 16540500,
                    "daysInflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "daysInflow": 15,
                    "assetCode": "200",
                    "reportDate_Day": 30,
                    "assetName": "MONDAY(MON)",
                    "inflow": 16020444,
                    "daysInflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "daysInflow": 0,
                    "assetCode": "300",
                    "reportDate_Day": 30,
                    "assetName": "チョコレート(CHOC)",
                    "inflow": 0,
                    "daysInflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "daysInflow": 0,
                    "assetCode": "400",
                    "reportDate_Day": 30,
                    "assetName": "コーヒー(COF)",
                    "inflow": 0,
                    "daysInflowCalc": 0
                },
                {
                    "groupAccount": "132132",
                    "daysInflow": 0,
                    "assetCode": "500",
                    "reportDate_Day": 30,
                    "assetName": "PA(パイナップル)",
                    "inflow": 0,
                    "daysInflowCalc": 0
                },
                {
                    "currentMonthNAV": 8060568,
                    "groupAccount": "132132",
                    "assetCode": "100",
                    "exposure": 8060568,
                    "assetName": "クッキー",
                    "previousMonthNAV": 15386579,
                    "compositionRate": 0.002542778584331914
                },
                {
                    "currentMonthNAV": 1536697544,
                    "groupAccount": "132132",
                    "assetCode": "200",
                    "exposure": 1536697544,
                    "assetName": "MONDAY(MON)",
                    "previousMonthNAV": 1517092239,
                    "compositionRate": 0.4847650445326743
                },
                {
                    "currentMonthNAV": 131622258,
                    "groupAccount": "132132",
                    "assetCode": "300",
                    "exposure": 131622258,
                    "assetName": "チョコレート(CHOC)",
                    "previousMonthNAV": 146077741,
                    "compositionRate": 0.04152142365945055
                },
                {
                    "currentMonthNAV": 148841273,
                    "groupAccount": "132132",
                    "assetCode": "400",
                    "exposure": 148841273,
                    "assetName": "コーヒー(COF)",
                    "previousMonthNAV": 144401851,
                    "compositionRate": 0.0469533166209999
                },
                {
                    "currentMonthNAV": 1344762582,
                    "groupAccount": "132132",
                    "assetCode": "500",
                    "exposure": 1344762582,
                    "assetName": "PA(パイナップル)",
                    "previousMonthNAV": 1332687412,
                    "compositionRate": 0.4242174366025433
                }
            ],
            "rows": [
                [],
                [
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "年金資産運用状況表（まとめ）"
                    }
                ],
                [
                    "",
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "顧客名称"
                    },
                    {
                        "className": "border_bottom",
                        "isKey": True,
                        "key": "clientCode1",
                        "keyType": "label",
                        "value": ""
                    },
                    {
                        "className": "border_bottom",
                        "isKey": True,
                        "key": "clientName",
                        "keyType": "label",
                        "value": ""
                    },
                    "",
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "会計基準(2)"
                    },
                    {
                        "className": "border_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [
                    "",
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "運用機関名称"
                    },
                    {
                        "className": "border_bottom",
                        "isKey": True,
                        "key": "assetManagerCode1",
                        "keyType": "label",
                        "value": ""
                    },
                    {
                        "className": "border_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_bottom",
                        "isKey": True,
                        "key": "assetManagerCode2",
                        "keyType": "label",
                        "value": ""
                    },
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "記入担当者名"
                    },
                    {
                        "className": "border_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [
                    "",
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "基準日(年YYYY)(月MM)"
                    },
                    {
                        "className": "border_bottom",
                        "isKey": True,
                        "key": "DateYear",
                        "keyType": "label",
                        "value": ""
                    },
                    {
                        "className": "border_bottom",
                        "isKey": True,
                        "key": "DateMonth",
                        "keyType": "label",
                        "value": ""
                    },
                    {
                        "className": "border_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "TEL・ﾒｰﾙｱﾄﾞﾚｽ"
                    },
                    {
                        "className": "border_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [],
                [
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "流入キャッシュフロー(5)"
                    },
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "流出キャッシュフロー(5)"
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_top_bottom",
                        "isKey": True,
                        "key": "assetCode",
                        "keyType": "column",
                        "value": ""
                    },
                    {
                        "className": "border_right_top_bottom",
                        "isKey": True,
                        "key": "assetName",
                        "keyType": "column",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "previousMonthNAV",
                        "keyType": "column",
                        "value": "前月末時価総額(1)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "inflow",
                        "keyType": "column",
                        "value": "買入総額"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "daysInflow",
                        "keyType": "column",
                        "value": "日数(4)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "outflow",
                        "keyType": "column",
                        "value": "売却総額(含む利配収入)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "daysOutflow",
                        "keyType": "column",
                        "value": "日数(4)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "currentMonthNAV",
                        "keyType": "column",
                        "value": "月末時価総額(1)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "exposure",
                        "keyType": "column",
                        "value": "実質エクスポージャー"
                    },
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "compositionRate",
                        "keyType": "column",
                        "value": "構成比(7)"
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "zzz"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "合計"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [],
                [],
                [],
                [],
                [
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月入出金状況"
                    },
                    "",
                    "",
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "ｷｬｯｼｭﾌﾛｰ･ﾁｪｯｸ(6)"
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月中入金"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "clientContribution",
                        "keyType": "label",
                        "value": ""
                    },
                    "",
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "流入総額"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "checkInflow",
                        "keyType": "label",
                        "value": ""
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "報酬(3)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "totalCashOutflow",
                        "keyType": "label",
                        "value": ""
                    },
                    "",
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "流出総額"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "checkOutflow",
                        "keyType": "label",
                        "value": ""
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月中出金"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "clientWithdrawal",
                        "keyType": "label",
                        "value": ""
                    },
                    "",
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "ｷｬｯｼｭﾌﾛｰ計"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "NET元本増減"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": True,
                        "key": "netIncreaseDecrease",
                        "keyType": "label",
                        "value": ""
                    },
                    "",
                    "",
                    "",
                    "",
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "誤差"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [],
                [],
                [
                    "",
                    {
                        "className": "",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "*為替オーバーレイ(個別のマンデートとして採用されている場合)"
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "前月末評価損益額(10)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月末評価損益額(10)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月分実現損益額"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月分評価損益額増分(10)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "当月評価損益増+実現"
                    }
                ],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "ｵﾌﾊﾞﾗﾝｽ為替(9)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ],
                [],
                [
                    "",
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": "為替オーバーレイ想定元本(11)"
                    },
                    {
                        "className": "border_left_right_top_bottom",
                        "isKey": False,
                        "key": "",
                        "keyType": "",
                        "value": ""
                    }
                ]
            ]
        }
    ]
}


inputJSON = {
  "header": {
    "request param": {
      "dataSourcesQueryParam": [
        {
          "name": "account",
          "queryParams": [
            {
              "dataType": "String",
              "name": "accountNumber",
              "value": "132132",
              "dataFormat": ""
            }
          ],
          "paramMapping": {
            "accountNumber": [
              "132132"
            ]
          }
        },
        {
          "name": "consultant",
          "queryParams": [
            {
              "calorbizday": "Calendar",
              "holidaycal": "",
              "value": "20210930",
              "numprioroffset": "1",
              "firstorlastdayoftheperiod": "Last",
              "dataFormat": "yyyyMMdd",
              "usecustomdate": 1,
              "dataType": "Date",
              "name": "asOfDate"
            },
            {
              "dataType": "String",
              "name": "consultantName",
              "value": "CHOCOLATE_CAKE",
              "dataFormat": ""
            },
            {
              "dataType": "String",
              "name": "groupAccount",
              "value": "132132",
              "dataFormat": ""
            }
          ]
        }
      ]
    }
  },
  "body": {
    "Asset NAV Details": {
      "columns": [
        {
          "name": "assetCode",
          "type": "string",
          "field": "assetCode"
        },
        {
          "name": "assetName",
          "type": "string",
          "field": "assetName"
        },
        {
          "name": "compositionRate",
          "type": "decimal",
          "field": "compositionRate"
        },
        {
          "name": "currentMonthNAV",
          "type": "decimal",
          "field": "currentMonthNAV"
        },
        {
          "name": "exposure",
          "type": "decimal",
          "field": "exposure"
        },
        {
          "name": "groupAccount",
          "type": "string",
          "field": "groupAccount"
        },
        {
          "name": "previousMonthNAV",
          "type": "decimal",
          "field": "previousMonthNAV"
        }
      ],
      "rows": [
        {
          "currentMonthNAV": 8060568,
          "groupAccount": "132132",
          "assetCode": "100",
          "exposure": 8060568,
          "assetName": "クッキー",
          "previousMonthNAV": 15386579,
          "compositionRate": 0.002542778584331914
        },
        {
          "currentMonthNAV": 1536697544,
          "groupAccount": "132132",
          "assetCode": "200",
          "exposure": 1536697544,
          "assetName": "MONDAY(MON)",
          "previousMonthNAV": 1517092239,
          "compositionRate": 0.4847650445326743
        },
        {
          "currentMonthNAV": 131622258,
          "groupAccount": "132132",
          "assetCode": "300",
          "exposure": 131622258,
          "assetName": "チョコレート(CHOC)",
          "previousMonthNAV": 146077741,
          "compositionRate": 0.04152142365945055
        },
        {
          "currentMonthNAV": 148841273,
          "groupAccount": "132132",
          "assetCode": "400",
          "exposure": 148841273,
          "assetName": "コーヒー(COF)",
          "previousMonthNAV": 144401851,
          "compositionRate": 0.0469533166209999
        },
        {
          "currentMonthNAV": 1344762582,
          "groupAccount": "132132",
          "assetCode": "500",
          "exposure": 1344762582,
          "assetName": "PA(パイナップル)",
          "previousMonthNAV": 1332687412,
          "compositionRate": 0.4242174366025433
        }
      ]
    }
  }
}

def allString(row):
    for el in row:
        if el != "":
            return False
    return True

def emptyRowIndex(rows):
    for i in range(len(rows)):
        if len(rows[i]) >0 and allString(rows[i]):
            return i
    return -1
    

def removeEmptyRow(rows):
   
    while emptyRowIndex(rows) != -1:
        i = emptyRowIndex(rows)
        rows.pop(i)
            
def notInColumn(rows:list, columnIndex:int, value, keysDataTypeObj):
    for row in rows:
        if len(row) > columnIndex and type(row[columnIndex]) == dict:
            el = row[columnIndex]["value"]
            k = row[columnIndex]["key"]
            
            if k != "" and k in keysDataTypeObj:
            
                t = keysDataTypeObj[k]
                if t =="string" and  el == value and value.isnumeric():
                    
                    return False

    
    return True
    

def addColumnStyles(className:str):
    bold = "bold "
    border = "border_left_right_top_bottom "
    
    className = className + bold + border
    
    return className

def isInvalidBody(o:dict):
    return not("body" in list(o.keys()))

def containsKeyObj(row:list):
    for el in row:
        if type(el) == dict and el["isKey"]:
            #print("row contains key")
            return True
    #print("row does not contain key")
    return False

def updateKeyDataType(columnKeys:list, sheetKeys: dict):
    for keyObj in columnKeys:
            sheetKeys[keyObj["name"]] = keyObj["type"]
            

def updateToRemoveIndexs(toRemoveIndexes, index):
    for i in range(index, len(toRemoveIndexes)):
        toRemoveIndexes[i]-= 1
    
def updateRawInputsArray(rawInputsArray:list, inputJSONArray:list):
    updatedRawInputs = []
    
    sampleInputObj = inputJSONArray[0]
    
    for rawInputObj in rawInputsArray:
         if set(sampleInputObj.keys()) != set(rawInputObj.keys()):
            updatedRawInputs.append(rawInputObj)
         elif set(sampleInputObj.keys()) == set(rawInputObj.keys()):
             print("same key found, overidding")
    updatedRawInputs += inputJSONArray
    #print(f"updated raw inputs {updatedRawInputs}")
    
    
    
    return updatedRawInputs
    
def nextAvailableRow(rows:list, toInsertCol: int, currentRowIndex: int):
    for j in range(currentRowIndex,len(rows)):
        for i in range(len(rows[j])):
            if rows[j][i] == "" and i == toInsertCol:
                #print("available row index ", j)
                return j
            
            
def setDataType(columnKey, templateKeysDataObj):
    
    return f"dType_{templateKeysDataObj[columnKey]}" + " "



def containsLabelKeys(row:list):
    for el in row:
        if type(el) == dict and el['isKey'] and el["keyType"] == "label":
            return True
    return False

def containsColumnKeys(row:list):
    for el in row:
        if type(el) == dict and el['isKey'] and el["keyType"] == "column":
            return True
    return False

def isLabelKey(o):
    return type(o) == dict and o['isKey'] and o['keyType'] == "label"



def findLabelValue(rawInputs:list, key:str):
    for inputObj in rawInputs:
        if key in inputObj:
            return str(inputObj[key])

def findKeyIndex(rowKeys, rawInputIndex):
    for i in range(len(rowKeys)):
        if rowKeys[i] == rawInputIndex:
            return i
    return -1


def replaceEmptyString(rows):
    for i in range(len(rows)):
            for j in range(len(rows[i])):
                if type(rows[i][j]) == str:
                    emptyObj = {"className" : "", "isKey" : False, "keyType" : "", "value" : ""}
                    
                    rows[i][j] = emptyObj
                    
def inputMatchWithRow(row:list, rawInputObj:dict):
    rowKeys = []
    rawInputKeys = list(rawInputObj.keys())
    for el in row:
        if type(el) == dict and el['isKey']:
            rowKeys.append(el['key'])
    
    for rawInputKey in rawInputKeys:
       if rawInputKey in  rowKeys:
           return True
    return False



def updateDataInputsAndTypes(inputJson:dict, reportJson:dict):
    
    maxRowLength = 0
    
    body = inputJson['body']
        
    bodyKeys = list(body.keys())
    
    for bodyKey in bodyKeys:
        rawInputs = reportJson["sheets"][0]["rawInputs"]

        rows = reportJson["sheets"][0]['rows']
        
        for row in rows:
            if len(row) > maxRowLength:
                maxRowLength = len(row)
        
        if reportJson["sheets"][0]['keysDataType'] == None:
            colKeys = {}
        
        else:
            colKeys = reportJson["sheets"][0]['keysDataType']
        
        # check if rawInputs array already contain objects with the same keys
        # if rawInputs already have same object(s) remove all those same 
        
        reportJson["sheets"][0]["rawInputs"] = updateRawInputsArray(rawInputs, body[bodyKey]["rows"])
        
        # loop through JSON input "columns" array to store/update the data type for each key
        updateKeyDataType(body[bodyKey]["columns"], colKeys)

# count rows that have at least one numeric value
# else is considered a duplicate row
def rowObjectCount(row):
    count = 0
    for el in row:
        if type(el) == dict:
            
            count += 1
            
            
def checkRowForNumericValue(row, keysDataTypeObj):
    for i in range(len(row)):
        if type(row[i]) == dict:
            cellObj = row[i]
            
            key = cellObj["key"]
            
            dataType = keysDataTypeObj[key]
            v = cellObj["value"]
            
            if dataType == "decimal":
                print("is decimal value is", v)
                return True
                  
    return False
    
        
# here
def removeDuplicateColumnRows(rows: list, keysDataTypeObj:dict):
    o = []
    hasDuplicates = True
    
    while hasDuplicates:
        o.clear()
        # only rows with key
        for i in range(len(rows)):
            appended = False
            for j in range(len(rows[i])):
                
                if type(rows[i][j]) == dict:
                    cellObj = rows[i][j]
                    
                    if cellObj["key"] != "" and not cellObj["isKey"]:
                        print(f"value is {cellObj['value']}")
                        # check if row has any numeric value
                        
                        if not checkRowForNumericValue(rows[i], keysDataTypeObj):
                            rows.pop(i)
                            o.append(i)
                            appended = True
                            break
            if appended:
                break
        
        if len(o) == 0:
            hasDuplicates = False               


    print(rows)
    

def addPlaceHolders(rows:list):
    for row in rows:
        while len(row) < 50:
            emptyObj = {
                        "value" : "",
                        "key" : "",
                        "className" : "",
                        "isKey" : False,
                        "keyType" : ""
                    }
            row.append(emptyObj)
        

    
   
     

def render(reportJSON :dict):
    rawInputs = copy.deepcopy(reportJSON["sheets"][0]["rawInputs"])

    rows = reportJSON["sheets"][0]["rows"]
    
    keysDataTypeObj = reportJSON["sheets"][0]["keysDataType"]
    
    insertIndex = 0

    numberOfRowsWithKeys = len(rows)

    maxRowLength = 0

    for row in rows:
        if len(row) > maxRowLength:
            maxRowLength = len(row)

    while len(rawInputs) > 0:
        
        # if currentRowWithKeysPosition >= len(rows):
        #     currentRowWithKeysPosition = 0
        
        #enRow = len(rows[currentRowWithKeysPosition])
        rawInputIndex = 0
        currentRowWithKeysPosition = 0
        for i in range(len(rows)):
            if containsLabelKeys(rows[i]) and  len(rawInputs) > 0 and inputMatchWithRow(rows[i], rawInputs[rawInputIndex]):
                
                for j in range(len(rows[currentRowWithKeysPosition])):
                    if isLabelKey(rows[currentRowWithKeysPosition][j]):
                        value = findLabelValue(rawInputs, rows[currentRowWithKeysPosition][j]['key'])
                    
                        if value != None:
                            className = setDataType(rows[currentRowWithKeysPosition][j]['key'], reportJSON["sheets"][0]["keysDataType"])
                            className = addColumnStyles(className)
                            print(f"inserted value is {value}")
                            rows[currentRowWithKeysPosition][j]["className"] = className
                            rows[currentRowWithKeysPosition][j]["value"] = value
                        
                    
            # check row contain column keys
            # check current input has matching key
            if containsColumnKeys(rows[i]) and inputMatchWithRow(rows[i], rawInputs[rawInputIndex]):
                print("is column")
                maxRowCount = 0
                currentRowWithKeysPosition = i
                # looping through row keys
                for j in range(len(rows[currentRowWithKeysPosition])):
                    if type(rows[currentRowWithKeysPosition][j]) == dict and rows[currentRowWithKeysPosition][j]['keyType'] == "column":
                            colObj = rows[currentRowWithKeysPosition][j]
                            colObjKey = colObj["key"]
                            colKeyCount =0
                            for rawInput in rawInputs:
                                if colObjKey in rawInput:
                                    colKeyCount += 1
                            if colKeyCount > maxRowCount:
                                maxRowCount = colKeyCount
                #print(f"max row count for current row keys is {maxRowCount}")
                insertIndex = currentRowWithKeysPosition + 1
                for a in range(maxRowCount):
                    #blankRow = ["" for i in range(lenRow)]
                    blankRow = ["" for m in range(maxRowLength)]
                    rows.insert(insertIndex, blankRow)
                #if maxRowCount > 0:
                    #currentRowWithKeysPosition += maxRowCount + 1
                numberOfRowsWithKeys -= 1
        
        
                for z in range(i,len(rows)):
                    
                    #if containsColumnKeys(rows[z]):
                        
                    #rowKeys = [rowObj["key"] for rowObj in rows[i]]
                    rowKeys = []
                    
                    for a in rows[z]:
                        if type(a) == dict:
                            rowKeys.append(a["key"])
                        else:
                            rowKeys.append("")
                        
                    
                    toInsertRow = currentRowWithKeysPosition + 1
                    
                    rawInputIndex = 0
                    while len(rawInputs) > 0 and rawInputIndex < len(rawInputs):
                        
                        matchKey = False
                        # loop through each input JSON key, if one does not 
                        # exist in the current keys row, break
                        rawInputKeys = list(rawInputs[rawInputIndex].keys())
                        
                        for inputKey in rawInputKeys:
                            if inputKey in rowKeys:
                                matchKey = True
                                break
                        
                        if not matchKey:
                            rawInputIndex += 1
                            print("no key found")
                        
                        elif matchKey:
                            for rawInputKey in rawInputKeys:
                                if rawInputKey in rowKeys:
                                   
                                    
                                    #print("index in rowKeys ", rowKeys.index(rawInputKey))
                                    toInsertCol = rowKeys.index(rawInputKey)
                                    #print("value is ", rawInputsCopy[j][rawInputKey])
                                    
                                    className = setDataType(rawInputKey, reportJSON["sheets"][0]["keysDataType"])
                                    className = addColumnStyles(className)
                                    
                                    value = str(rawInputs[rawInputIndex][rawInputKey])
                                    
                                    if value == "200":
                                        print("here")
                                    
                                    # to insert for column value
                                    o = {
                                        "value" : value,
                                        "key" : rawInputKey,
                                        "className" : className,
                                        "isKey" : False,
                                        "keyType" : ""
                                    }
                                    
                                    if value == "200":
                                        print("value is ", o['value'])
                                    
                                    # if index of toInsertRow and toInsertCol already has a dict
                                    # need a function to find the next row that has empty "" in the same column index
                                    
                                    if type(rows[toInsertRow][toInsertCol]) != str:
                                        nextRow = nextAvailableRow(rows, toInsertCol, toInsertRow)
                                        #print(f"next availble row is {nextRow}")
                                        #print(f"inserted into row {nextRow}, column {toInsertCol}, value is {o['value']}, column name is {rawInputKey}")
                                        rows[nextRow][toInsertCol] = o
                                    
                                    elif type(rows[toInsertRow][toInsertCol]) == str: 
                                        #print(f"inserted into row {toInsertRow}, column {toInsertCol}, value is {o['value']}, column name is {rawInputKey}")
                                        rows[toInsertRow][toInsertCol] = o
                                        
                            rawInputs.pop(rawInputIndex)
                            rawInputIndex = 0
                numberOfRowsWithKeys -= 1
                
            currentRowWithKeysPosition += 1
            insertIndex = currentRowWithKeysPosition + 1
        print("popped input")
        if len(rawInputs) > 0:
            rawInputs.pop(0)
        rawInputIndex = 0
    removeDuplicateColumnRows(rows, keysDataTypeObj)
    removeEmptyRow(rows)
    replaceEmptyString(rows)
    
    addPlaceHolders(rows)

            


updateDataInputsAndTypes(inputJSON, complex_json)
            
render(complex_json)

print("done")
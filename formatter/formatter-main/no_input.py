import copy
from dataclasses import replace




complete_complex_json = {
        "reportName": "complex_report",
        "sheets": [
            {
                "keysDataType": {
                    "DateMonth": "string",
                    "DateYear": "string",
                    "TerminationDate": "string",
                    "assetCode": "string",
                    "assetManagerCode1": "string",
                    "assetManagerCode2": "string",
                    "assetName": "string",
                    "clientCode1": "string",
                    "clientName": "string",
                    "compositionRate": "decimal",
                    "currentMonthNAV": "decimal",
                    "exposure": "decimal",
                    "groupAccount": "string",
                    "previousMonthNAV": "decimal",
                    "reportingMonth": "string",
                    "daysInflow" : "decimal",
                    "reportDate_Day" : "decimal",
                    "inflow" : "decimal",
                    "daysInflowCalc" : "decimal",
                    "daysOutflow" : "decimal",
                    "daysOutflowCalc" : "decimal",
                    "outflow" : "decimal",
                },
                "rawInputs": [
                   {
                        "DateMonth": "9",
                        "DateYear": "2021",
                        "TerminationDate": "",
                        "assetManagerCode1": "1011",
                        "assetManagerCode2": "1",
                        "clientCode1": "1010",
                        "clientName": "ABC株式会社",
                        "reportingMonth": "09/30/2021"
                    },
                    {
                        "assetCode": "100",
                        "assetName": "クッキー",
                        "compositionRate": 0.002542778584331914,
                        "currentMonthNAV": 8060568,
                        "exposure": 8060568,
                        "groupAccount": "132132",
                        "previousMonthNAV": 15386579
                    },
                    {
                        "assetCode": "200",
                        "assetName": "MONDAY(MON)",
                        "compositionRate": 0.4847650445326743,
                        "currentMonthNAV": 1536697544,
                        "exposure": 1536697544,
                        "groupAccount": "132132",
                        "previousMonthNAV": 1517092239
                    },
                    {
                        "assetCode": "300",
                        "assetName": "チョコレート(CHOC)",
                        "compositionRate": 0.04152142365945055,
                        "currentMonthNAV": 131622258,
                        "exposure": 131622258,
                        "groupAccount": "132132",
                        "previousMonthNAV": 146077741
                    },
                    {
                        "assetCode": "400",
                        "assetName": "コーヒー(COF)",
                        "compositionRate": 0.0469533166209999,
                        "currentMonthNAV": 148841273,
                        "exposure": 148841273,
                        "groupAccount": "132132",
                        "previousMonthNAV": 144401851
                    },
                    {
                        "assetCode": "500",
                        "assetName": "PA(パイナップル)",
                        "compositionRate": 0.4242174366025433,
                        "currentMonthNAV": 1344762582,
                        "exposure": 1344762582,
                        "groupAccount": "132132",
                        "previousMonthNAV": 1332687412
                    },
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
                            "className": "",
                            "isKey": True,
                            "key": "clientCode1",
                            "keyType": "label",
                            "value": "1010"
                        },
                        {
                            "className": "",
                            "isKey": True,
                            "key": "clientName",
                            "keyType": "label",
                            "value": "ABC株式会社"
                        },
                       "",
                       "",
                        {
                            "className": "",
                            "isKey": False,
                            "key": "",
                            "keyType": "",
                            "value": "会計基準(2)"
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
                            "className": "",
                            "isKey": True,
                            "key": "assetManagerCode1",
                            "keyType": "label",
                            "value": ""
                        },
                          "",
                           {
                            "className": "",
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
                            "className": "",
                            "isKey": True,
                            "key": "DateYear",
                            "keyType": "label",
                            "value": ""
                        },
                          "",
                           {
                            "className": "",
                            "isKey": True,
                            "key": "DateMonth",
                            "keyType": "label",
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
                    ],
                    [],
                    [
                        "",
                       {
                            "className": "",
                            "isKey": True,
                            "key": "assetCode",
                            "keyType": "column",
                            "value": "Asset Code"
                       },
                       {
                            "className": "",
                            "isKey": True,
                            "key": "assetName",
                            "keyType": "column",
                            "value": "Asset Name"
                       },
                        {
                            "className": "",
                            "isKey": True,
                            "key": "previousMonthNAV",
                            "keyType": "column",
                            "value": "前月末時価総額(1)"
                       },
                       {
                            "className": "",
                            "isKey": True,
                            "key": "inflow",
                            "keyType": "column",
                            "value": "買入総額"
                       },
                 
                        {
                            "className": "",
                            "isKey": True,
                            "key": "daysInflow",
                            "keyType": "column",
                            "value": "日数(4)"
                       },
                   
                        {
                            "className": "",
                            "isKey": True,
                            "key": "outflow",
                            "keyType": "column",
                            "value": "売却総額(含む利配収入)"
                       },
                   
                       {
                            "className": "",
                            "isKey": True,
                            "key": "currentMonthNAV",
                            "keyType": "column",
                            "value": "月末時価総額(1)"
                       },
                       {
                            "className": "",
                            "isKey": True,
                            "key": "exposure",
                            "keyType": "column",
                            "value": "実質エクスポージャー"
                       },
                       "",
                       {
                            "className": "",
                            "isKey": True,
                            "key": "compositionRate",
                            "keyType": "column",
                            "value": "構成比(7)",
                            "format" : "percentage"
                       },
                    ],
                    [
                        "",
                        {
                            "className": "",
                            "isKey": False,
                            "key": "",
                            "keyType": "",
                            "value": "zzz"
                       },
                         {
                            "className": "",
                            "isKey": False,
                            "key": "",
                            "keyType": "",
                            "value": "合計"
                       },
                    ]
                ],
                "sheetName": "test_sheet"
            }
        ],
        "templateName": "complex_report"
}


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

def findLabelValue(rawInputs:list, key:str):
    for inputObj in rawInputs:
        if key in inputObj:
            return inputObj[key]

def findKeyIndex(rowKeys, rawInputIndex):
    for i in range(len(rowKeys)):
        if rowKeys[i] == rawInputIndex:
            return i
    return -1

def isLabelKey(o):
    return type(o) == dict and o['isKey'] and o['keyType'] == "label"


def setDataType(columnKey, templateKeysDataObj):
    
    return f"dType_{templateKeysDataObj[columnKey]}" + " "

def nextAvailableRow(rows:list, toInsertCol: int, currentRowIndex: int):
    for j in range(currentRowIndex,len(rows)):
        for i in range(len(rows[j])):
            if rows[j][i] == "" and i == toInsertCol:
                #print("available row index ", j)
                return j
            
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
    

rawInputs = copy.deepcopy(complete_complex_json["sheets"][0]["rawInputs"])

rows = complete_complex_json["sheets"][0]["rows"]
currentRowWithKeysPosition = 0
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
    for i in range(len(rows)):
        if containsLabelKeys(rows[i]) and inputMatchWithRow(rows[i], rawInputs[rawInputIndex]):
            
            
            for j in range(len(rows[currentRowWithKeysPosition])):
                if isLabelKey(rows[currentRowWithKeysPosition][j]):
                    value = findLabelValue(rawInputs, rows[currentRowWithKeysPosition][j]['key'])
                    print(f"value is {value} for {rows[currentRowWithKeysPosition][j]['key']}")
                    rows[currentRowWithKeysPosition][j]["value"] = value
            #rawInputs.pop(rawInputIndex)
            #rawInputIndex = 0
            
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
                    
                    # for rowKey in rowKeys:
                        
                    #     if rowKey != "" and rowKey not in rawInputKeys:
                    #         matchKey = False
                    #         break
                    
                    # for rawInputKey in rawInputKeys:
                    #     if rawInputKey not in rowKeys:
                    #         matchKey = False
                    #         break
                    
                    #toInsertCol = 0
                    
                    if not matchKey:
                        rawInputIndex += 1
                        print("no key found")
                    
                    elif matchKey:
                        for rawInputKey in rawInputKeys:
                            if rawInputKey in rowKeys:
                                # current row is rows[i] (keys)
                                # currentColKey = rows[i][toInsertCol]['key']
                                # print(f"key is {currentColKey}")
                                
                                #print("index in rowKeys ", rowKeys.index(rawInputKey))
                                toInsertCol = rowKeys.index(rawInputKey)
                                #print("value is ", rawInputsCopy[j][rawInputKey])
                                
                                className = setDataType(rawInputKey, complete_complex_json["sheets"][0]["keysDataType"])
                                
                                
                                
                                o = {
                                    "value" : str(rawInputs[rawInputIndex][rawInputKey]),
                                    "key" : rawInputKey,
                                    "className" : className,
                                    "isKey" : False,
                                    "keyType" : ""
                                }
                                
                                print("value is ", o['value'])
                                
                                # if index of toInsertRow and toInsertCol already has a dict
                                # need a function to find the next row that has empty "" in the same column index
                                
                                if type(rows[toInsertRow][toInsertCol]) != str:
                                    nextRow = nextAvailableRow(rows, toInsertCol, toInsertRow)
                                    #print(f"next availble row is {nextRow}")
                                    #print(f"inserted into row {nextRow}, column {toInsertCol}, value is {o['value']}, column name is {rawInputKey}")
                                    rows[nextRow][toInsertCol] = o
                                
                                else: 
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
        
    
    
replaceEmptyString(rows)


print("done")
        
        
    
from flask import Flask , jsonify, request
from flask_cors import CORS
import copy
import requests



app = Flask(__name__)
CORS(app)
## simple

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
            value = inputObj[key]
            if type(value) == float:
                value = round(value, 2)
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

def addColumnStyles(className:str):
    bold = "bold "
    border = "border_left_right_top_bottom "
    
    className = className + bold + border
    
    return className
    
    
def getInputKeys(newInput: dict):
    newBodyInput = newInput["body"]
    bodyKeys = list(newBodyInput.keys())

    for bodykey in bodyKeys:
        sampleKeys = list(newBodyInput[bodykey]["rows"][0].keys())
        sampleKeys.sort()
        return sampleKeys
            
def getCurrentInputKeys(currentInputArr:list):
    o = []
    
    for currentInput in currentInputArr:
        body = currentInput["body"]
        bodyKeys = list(body.keys())
        for bodyKey in bodyKeys:
            k = list(body[bodyKey]["rows"][0].keys())
            k.sort()
            o.append(k)
            break
    return o

def updateReportJSON(reportJSON: dict):
    url = "https://report-2b4cd56mpa-as.a.run.app/update"
    r = requests.put(url, json=reportJSON)
    print(r.status_code)
    
    
def notInColumn(rows:list, columnIndex:int, value, keysObj):
    for row in rows:
        if len(row) > columnIndex and type(row[columnIndex]) == dict:
            el = row[columnIndex]["value"]
            k = row[columnIndex]["key"]
            
            if k != "" and k in keysObj:
                t = keysObj[k]
                
                if t == "string" and el == value and value.isnumeric():
        
                    return False

    
    return True

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
     
    
@app.route("/ping")
def ping():
    return jsonify({
        "message" : "OK"
        }),200
    

# @app.route("/update/inputs", methods=["POST"])
# def updateJSON():
#     if request.get_json():
#         isOverride = False
#         newInput = request.get_json()["newInput"]
#         currentInputArray = request.get_json()["currentInputArray"]
        
#         newInputKeys = getInputKeys(newInput)
#         print(f"new input keys {newInputKeys}")
        
#         currentInputKeysArr = getCurrentInputKeys(currentInputArray)
        
#         for i in range(len(currentInputKeysArr)):
#             if newInputKeys == currentInputKeysArr[i]:
#                 print("is match")
#                 isOverride = True
#                 currentInputArray[i] = newInput
#                 break
                
                
        
        
#         if not isOverride:
#             currentInputArray.append(newInput)
            
#     return jsonify({
#        "inputJSON" : currentInputArray,
#        "isOverride" : isOverride,
#        "length" : len(currentInputArray)
#         }),200
        
    

# @app.route("/save", methods=["POST"])
# def save():
#     if request.args.get("reportID"):
#         id = request.args.get('reportID')
#         inputsArr = request.get_json()["inputs"]
#         reportName = request.get_json()["reportName"]
#         reportJSON = getReportJSON(id)
        
#         # update reportName
#         for input in inputsArr:
#             updateDataInputsAndTypes(input, reportJSON)
    
        
        
#     return jsonify({
#         "report" : reportJSON
#         }),200
    
# @app.route("/r")
# def noInputJSON():
#     reportJSON = request.get_json()
    
#     render(reportJSON)
    
#     return jsonify({
#         "report" : reportJSON
#         }),200
    
@app.route("/render/inputs", methods =["POST"])
def withInput():
    if request.get_json():
        id = request.args.get("reportID")
        
        if id == "":
            return jsonify({
                "message" : "missing report ID"
                }),200
        
        reportJSON = getReportJSON(id)
        if type(reportJSON) == bool and not reportJSON:
            return jsonify({
             "message" : f"no report with ID {id}"
            }),400
        else:
            inputJSON = request.get_json()
            updateDataInputsAndTypes(inputJSON, reportJSON)
            
            # save updated JSON object in reports DB
            updateReportJSON(reportJSON)
            
            render(reportJSON)
            return reportJSON,200
            

# render without needing to pass in any new input
@app.route("/render")
def noInput():
    if request.args.get("reportID"):
        id = request.args.get("reportID")
        # query report json based on reportId
        reportJSON = getReportJSON(id)
    
    
        render(reportJSON)
    
        return reportJSON,200
    

def getReportJSON(reportID):
    url = f"https://report-2b4cd56mpa-as.a.run.app/id={reportID}"
    resp =  requests.get(url)
    if resp.status_code == 200:
        return resp.json()
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
    
def render(reportJSON :dict):
    rawInputs = copy.deepcopy(reportJSON["sheets"][0]["rawInputs"])
    
    keysDataTypeObj = reportJSON["sheets"][0]["keysDataType"]

    rows = reportJSON["sheets"][0]["rows"]
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
        currentRowWithKeysPosition = 0
        for i in range(len(rows)):
            if containsLabelKeys(rows[i]) and  len(rawInputs) > 0 and inputMatchWithRow(rows[i], rawInputs[rawInputIndex]):
                
                for j in range(len(rows[currentRowWithKeysPosition])):
                    if isLabelKey(rows[currentRowWithKeysPosition][j]):
                        value = findLabelValue(rawInputs, rows[currentRowWithKeysPosition][j]['key'])
                    
                        if value != None:
                            className = setDataType(rows[currentRowWithKeysPosition][j]['key'], reportJSON["sheets"][0]["keysDataType"])
                            className = addColumnStyles(className)
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
                                    
                                    # to insert for column value
                                    
                                    value = str(rawInputs[rawInputIndex][rawInputKey])
                                    
                                    o = {
                                        "value" : value,
                                        "key" : rawInputKey,
                                        "className" : className,
                                        "isKey" : False,
                                        "keyType" : ""
                                    }
                                    
                                    #print("value is ", o['value'])
                                    
                                    # if index of toInsertRow and toInsertCol already has a dict
                                    # need a function to find the next row that has empty "" in the same column index
                                    
                                    keysObj =reportJSON["sheets"][0]["keysDataType"]
                                    
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
    
    while len(rows) < 50:
        emptyObj = {
                        "value" : "",
                        "key" : "",
                        "className" : "",
                        "isKey" : False,
                        "keyType" : ""
                    }
        emptyRow = [emptyObj for i in range(50)]
        rows.append(emptyRow)

    
    print(len(rows))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
    
    
    
    
    
    
    
    
    

    
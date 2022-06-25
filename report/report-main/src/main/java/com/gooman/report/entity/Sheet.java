package com.gooman.report.entity;

import com.google.gson.JsonArray;

import java.util.ArrayList;
import java.util.HashMap;

public class Sheet {
    private String sheetName;
    private HashMap<String, String> keysDataType;
    private ArrayList rawInputs;
    private ArrayList<ArrayList> rows;

    public Sheet(String sheetName, HashMap<String, String> keysDataType, ArrayList rawInputs, ArrayList<ArrayList> rows) {
        this.sheetName = sheetName;
        this.keysDataType = keysDataType;
        this.rawInputs = rawInputs;
        this.rows = rows;
    }

    public String getSheetName() {
        return sheetName;
    }

    public void setSheetName(String sheetName) {
        this.sheetName = sheetName;
    }

    public HashMap<String, String> getKeysDataType() {
        return keysDataType;
    }

    public void setKeysDataType(HashMap<String, String> keysDataType) {
        this.keysDataType = keysDataType;
    }

    public ArrayList getRawInputs() {
        return rawInputs;
    }

    public void setRawInputs(ArrayList rawInputs) {
        this.rawInputs = rawInputs;
    }

    public ArrayList<ArrayList> getRows() {
        return rows;
    }

    public void setRows(ArrayList<ArrayList> rows) {
        this.rows = rows;
    }

    @Override
    public String toString() {
        return "Sheet{" +
                "sheetName='" + sheetName + '\'' +
                ", keysDataType=" + keysDataType +
                ", rawInputs=" + rawInputs +
                ", rows=" + rows +
                '}';
    }
}

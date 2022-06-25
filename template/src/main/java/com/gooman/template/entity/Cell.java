package com.gooman.template.entity;

public class Cell {
    private String value;
    private String className;
    private boolean isKey;
    private String keyType;
    private String key;

    public Cell(String value, String className, boolean isKey, String keyType, String key) {
        this.value = value;
        this.className = className;
        this.isKey = isKey;
        this.keyType = keyType;
        this.key = key;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public String getClassName() {
        return className;
    }

    public void setClassName(String className) {
        this.className = className;
    }

    public boolean getIsKey() {
        return isKey;
    }

    public void setIsKey(boolean key) {
        isKey = key;
    }

    public String getKeyType() {
        return keyType;
    }

    public void setKeyType(String keyType) {
        this.keyType = keyType;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
}

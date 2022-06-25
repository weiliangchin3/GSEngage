package com.gooman.report.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.annotation.PersistenceConstructor;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.Instant;
import java.util.ArrayList;
import java.util.HashMap;

@Document(collection = "report")
public class Report {
    @Id
    private int reportId;

    private String templateName;

    private String reportName;

    private ArrayList<Sheet> sheets;


    public Report() {
        this.reportId = Math.abs(Instant.now().hashCode());
    }

    @PersistenceConstructor
    public Report(String templateName, String reportName, ArrayList<Sheet> sheets) {
        this();
        this.templateName = templateName;
        this.reportName = reportName;
        this.sheets = sheets;
    }

    public int getReportId() {
        return reportId;
    }

    public String getTemplateName() {
        return templateName;
    }

    public void setTemplateName(String templateName) {
        this.templateName = templateName;
    }

    public String getReportName() {
        return reportName;
    }

    public void setReportName(String reportName) {
        this.reportName = reportName;
    }

    public ArrayList<Sheet> getSheets(){
        return sheets;
    }

    public void setSheets(ArrayList<Sheet> sheets){
        this.sheets = sheets;
    }


    @Override
    public String toString() {
        return "Report{" +
                "reportId=" + reportId +
                ", templateName='" + templateName + '\'' +
                ", reportName='" + reportName + '\'' +
                ", sheets=" + sheets +
                '}';
    }
}

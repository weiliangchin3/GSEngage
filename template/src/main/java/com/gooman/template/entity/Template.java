package com.gooman.template.entity;

import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.time.Instant;
import java.util.ArrayList;
import java.util.HashMap;

@Document(collection = "templates")
public class Template {

    @Id
    private int templateId;

    private String templateName;
    private String reportName;
    private ArrayList<Sheet> sheets;


    public Template() {
        this.templateId = Math.abs(Instant.now().hashCode());
    }

    public Template(String templateName, String reportName, ArrayList<Sheet> sheets) {
        this();
        this.templateName = templateName;
        this.reportName = reportName;
        this.sheets = sheets;
    }

    public int getTemplateId() {
        return templateId;
    }

    public void setTemplateId(int templateId) {
        this.templateId = templateId;
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

    public ArrayList<Sheet> getSheets() {
        return sheets;
    }

    public void setSheets(ArrayList<Sheet> sheets) {
        this.sheets = sheets;
    }

    @Override
    public String toString() {
        return "Template{" +
                "templateId=" + templateId +
                ", templateName='" + templateName + '\'' +
                ", reportName='" + reportName + '\'' +
                ", sheets=" + sheets +
                '}';
    }
}

package com.gooman.report.entity;

public class ReportOverview {
    private int reportId;

    private String reportName;

    public ReportOverview(int reportId, String reportName) {
        this.reportId = reportId;
        this.reportName = reportName;
    }

    public int getReportId() {
        return reportId;
    }

    public void setReportId(int reportId) {
        this.reportId = reportId;
    }

    public String getReportName() {
        return reportName;
    }

    public void setReportName(String reportName) {
        this.reportName = reportName;
    }
}

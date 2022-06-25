package com.gooman.report.service;

import com.gooman.report.entity.*;
import com.gooman.report.repository.reportRepository;
import lombok.extern.java.Log;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.crossstore.ChangeSetPersister;
import org.springframework.stereotype.Service;

import com.google.gson.*;

import java.util.*;
import java.util.logging.Logger;

@Service
public class reportService {

    Logger LOG = Logger.getLogger(reportService.class.getName());
    @Autowired
    private reportRepository reportRepository;

    public String test() {
        return "Test Successful: " + java.time.LocalDateTime.now();
    }

    public List<Report> getAllReports() {
        return reportRepository.findAll();
    }

    public List<ReportOverview> getReportOverview(){
        List<Report> reports = reportRepository.findAll();
        List<ReportOverview> reportOverviews = new ArrayList<>();
        for (Report r: reports) {
            ReportOverview reportOverview = new ReportOverview(r.getReportId(),r.getReportName());
            reportOverviews.add(reportOverview);
        }
        return reportOverviews;
    }
    public Report getReport(int id) {
        return reportRepository.findById(id).orElseThrow(()-> new NullPointerException());
    }

    public Report getReport(String reportName) {
        return reportRepository.findByReportName(reportName).orElseThrow(()-> new NullPointerException());
    }

    public String addReport(Report report) {
        try {
            reportRepository.save(report);
            return Integer.toString(report.getReportId());
        }catch (Exception e){
            return e.getMessage();
        }
    }

    public String updateReport(Report report){
        try {
            Report reportInDB = reportRepository.findById(report.getReportId()).orElseThrow(()-> new NullPointerException());
            //update sheets data (raw inputs and keys data type)
            reportInDB.setReportName(report.getReportName());
            ArrayList<Sheet> updatedSheets = report.getSheets();
            reportInDB.setSheets(updatedSheets);
            reportRepository.save(reportInDB);
            return Integer.toString(reportInDB.getReportId());
        }catch (Exception e){
            return e.getMessage();
        }
    }

    public String updateReportById(Report report, int id){
        try {
            Report reportInDB = reportRepository.findById(id).orElseThrow(()-> new NullPointerException());
            //update sheets data (raw inputs and keys data type)
            reportInDB.setReportName(report.getReportName());
            ArrayList<Sheet> updatedSheets = report.getSheets();
            reportInDB.setSheets(updatedSheets);
            reportRepository.save(reportInDB);
            return "Report (ID:" + reportInDB.getReportId() + ") updated successfully";
        }catch (Exception e){
            return e.getMessage();
        }
    }


    public String deleteReport(int id) {
        try{
            reportRepository.deleteById(id);
            return "Report deleted successfully";
        } catch (Exception e){
            return "Error deleting report: " + e.getMessage();
        }
    }


}

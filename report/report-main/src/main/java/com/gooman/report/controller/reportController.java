package com.gooman.report.controller;

import com.gooman.report.entity.Report;

import com.gooman.report.entity.ReportOverview;
import com.gooman.report.service.reportService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*", allowedHeaders = "*", methods = {RequestMethod.GET, RequestMethod.POST, RequestMethod.PUT, RequestMethod.DELETE})
@RestController
public class reportController {

    @Autowired
    private reportService reportService;

    @GetMapping(path = "/test")
    public String test(){
        return reportService.test();
    }

    @GetMapping(path = "/all")
    public List<ReportOverview> getAllReportsOverview(){
        try{
            return reportService.getReportOverview();
        } catch (Exception e){
            return null;
        }
    }
    @GetMapping(path = "/all/detailed")
    public List<Report> getAllReports(){
        try{
            return reportService.getAllReports();
        } catch (Exception e){
            return null;
        }
    }

    @GetMapping(path = "/id={id}")
    public Report getReport(@PathVariable int id){
        return reportService.getReport(id);
    }

    @GetMapping(path = "/reportName={title}")
    public Report getReport(@PathVariable String title){
        return reportService.getReport(title);
    }

    @PostMapping
    public String addReport(@RequestBody Report report){
        return reportService.addReport(report);
    }

    @CrossOrigin(origins = "*", allowedHeaders = "*")
    @PutMapping(path="/update")
    public String updateReport(@RequestBody Report report){
        return reportService.updateReport(report);
    }

    @CrossOrigin(origins = "*", allowedHeaders = "*")
    @PutMapping(path="/id={id}")
    public String updateReport(@RequestBody Report report, @PathVariable int id){
        return reportService.updateReportById(report, id);
    }

    @CrossOrigin(origins = "*", allowedHeaders = "*")
    @DeleteMapping(path = "/id={id}")
    public String deleteReport(@PathVariable int id){
        return reportService.deleteReport(id);
    }
}

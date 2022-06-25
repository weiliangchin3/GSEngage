package com.gooman.report.repository;

import com.gooman.report.entity.Report;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface reportRepository extends MongoRepository<Report, Integer> {
    Optional<Report> findByReportName(String reportName);
}

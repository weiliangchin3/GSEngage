 package com.gooman.report;

 import static org.junit.jupiter.api.Assertions.assertEquals;
 import static org.junit.jupiter.api.Assertions.assertNotNull;

 import static org.mockito.ArgumentMatchers.any;
 import static org.mockito.Mockito.verify;
 import static org.mockito.Mockito.when;

 import java.util.ArrayList;
 import java.util.Arrays;
 import java.util.Optional;

 import com.gooman.report.entity.Report;
 import com.gooman.report.entity.Sheet;
 import com.gooman.report.repository.reportRepository;
 import com.gooman.report.service.reportService;
 import org.junit.jupiter.api.BeforeEach;
 import org.junit.jupiter.api.Test;
 import org.junit.jupiter.api.extension.ExtendWith;
 import org.mockito.InjectMocks;
 import org.mockito.Mock;
 import org.mockito.junit.jupiter.MockitoExtension;

 @ExtendWith(MockitoExtension.class)
 public class reportUnitTest {
//     public Report report;
//     public Sheet sheet;
//     public String json = "{\n" +
//             "    \"reportName\" : \"financial_report\",\n" +
//             "    \"sheets\" : [\n" +
//             "        {\n" +
//             "         \"sheetName\": \"test_sheet\",\n" +
//             "         \"rows\" : [\n" +
//             "             [\"A1\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row1\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row2\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row3\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row4\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row5\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row6\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row7\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row8\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row9\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row10\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA\"],\n" +
//             "             [\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"row11\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"\",\"AA11\"]\n" +
//             " \n" +
//             "             ]\n" +
//             "        }\n" +
//             "    ]\n" +
//             " }";
//
//
     @Mock
     private reportRepository reportRepository;

     @InjectMocks
     private reportService reportService = new reportService();
//
//     @BeforeEach
//     void createReport(){
//        ArrayList rows = new ArrayList();
//        String[] rowArray =  {"A1","","","","","","","","","","","","","row1","","","","","","","","","","","","",""};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"", "", "", "", "", "", "", "", "", "", "", "", "", "row2", "", "", "", "", "", "", "", "", "", "", "", "", "AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row3","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row4","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row5","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row6","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row7","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row8","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row9","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row10","","","","","","","","","","","","","AA"};
//        rows.add(Arrays.asList(rowArray));
//        rowArray = new String[]{"","","","","","","","","","","","","","row11","","","","","","","","","","","","","AA11"};
//        rows.add(Arrays.asList(rowArray));
//        sheet = new Sheet("test_sheet", rows);
//        ArrayList<Sheet> sheets = new ArrayList<>();
//        sheets.add(sheet);
//        report = new Report("SIMPLE_REPORT", sheets);
//     }
//
     @Test
     void healthCheck(){
         String actual = reportService.test();
         String expected = "Test Successful: ";
         assertEquals(expected, actual.substring(0, expected.length()));
     }
//     @Test
//     void deleteReport(){
//         int id = 0;
//         reportService.deleteReport(id);
//         verify(reportRepository).deleteById(id);
//     }
//
//     @Test
//     void getReportFromId(){
//         int id = 0;
//
//         when(reportRepository.findById(any(Integer.class))).thenReturn(Optional.of(report));
//
//         Report returnedReport = reportService.getReport(id);
//
//         assertNotNull(returnedReport);
//         verify(reportRepository).findById(id);
//     }
//
//     @Test
//     void getReportFromTitle(){
//         String title = "SIMPLE_REPORT";
//
//         when(reportRepository.findByReportName(any(String.class))).thenReturn(Optional.of(report));
//
//         Report returnedReport = reportService.getReport(title);
//
//         assertNotNull(returnedReport);
//         verify(reportRepository).findByReportName(any(String.class));
//     }
//
//     @Test
//     void addReport(){
//         reportService.addReport(json);
//
//         verify(reportRepository).save(any(Report.class));
//     }

 }

package com.gooman.template;

import com.gooman.template.entity.Cell;
import com.gooman.template.entity.Sheet;
import com.gooman.template.entity.Template;
import com.gooman.template.repository.templateRepository;
import com.gooman.template.service.templateService;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

@ExtendWith(MockitoExtension.class)
public class templateUnitTest {
    public Template template;

    @Mock
    public templateRepository templateRepository;

    @InjectMocks
    public templateService templateService = new templateService();

    @Test
    void healthCheck(){
        String actual = templateService.test();
        String expected = "Test Successful";
        assertEquals(expected, actual);
    }
//    @BeforeEach
//    void createTemplate(){
//        ArrayList<Sheet> sheets = new ArrayList<>();
//
//        HashMap<String, String> keys = new HashMap<>();
//        keys.put("instrumentType","Instrument Type");
//        keys.put("ticker", "Ticker");
//        keys.put("coupon", "Coupon");
//        ArrayList<ArrayList<Cell>> rows = new ArrayList<>();
//        ArrayList<Cell> row1 = new ArrayList<>();
//        row1.add(new Cell("Instrument Type", "x_0_y_0", true, "column"));
//        row1.add(new Cell("Ticker", "x_0_y_1 center_align bold", true, "column"));
//        row1.add(new Cell("Coupon", "x_0_y_2", true, "column"));
//        rows.add(row1);
//        Sheet sheet = new Sheet("simple_report", keys, rows);
//        template = new Template("simple_template","simple_report", sheets);
//
//    }
//
//    @Test
//    void getTemplateByName(){
//        String title = "simple_report";
//
//        when(templateRepository.findByTemplateName("simple_report")).thenReturn(Optional.of(template));
//
//        Template returnedReport = templateService.getTemplateByTemplateName(title);
//
//        assertNotNull(returnedReport);
//        verify(templateRepository).findByTemplateName(any(String.class));
//    }
//
//
//    @Test
//    void getTemplateById(){
//
//    }



}

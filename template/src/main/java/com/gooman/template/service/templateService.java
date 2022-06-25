package com.gooman.template.service;

import com.gooman.template.entity.Sheet;
import com.gooman.template.entity.Template;
import com.gooman.template.repository.templateRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;
import java.util.Optional;

@Service
public class templateService {

    @Autowired
    private templateRepository templateRepository;

    public Template getTemplateById(int templateId) {
        return templateRepository.findById(templateId).orElseThrow(()->new NullPointerException());
    }

    public Template getTemplateByTemplateName(String templateName) {
        return templateRepository.findByTemplateName(templateName).orElseThrow(()->new NullPointerException());
    }
    public List<Template> getTemplates(){
        return templateRepository.findAll();
    }

    public String addTemplate(Template template) {
        templateRepository.save(template);
        return Integer.toString(template.getTemplateId());
    }

    public String updateTemplate(Template template) {
        try {
            Template templateInDB = templateRepository.findById(template.getTemplateId()).orElseThrow(()-> new NullPointerException());
            //update sheets data (raw inputs and keys data type)
            templateInDB.setTemplateName(template.getTemplateName());
            ArrayList<Sheet> updatedSheets = template.getSheets();
            templateInDB.setSheets(updatedSheets);
            templateInDB.setReportName(template.getReportName());
            templateRepository.save(templateInDB);
            return Integer.toString(templateInDB.getTemplateId());
        }catch (Exception e){
            return e.getMessage();
        }
    }

    public String deleteTemplate(int templateId) {
        templateRepository.deleteById(templateId);
        return "Template is deleted";

    }

    public String test() {
        return "Test Successful";
    }
}

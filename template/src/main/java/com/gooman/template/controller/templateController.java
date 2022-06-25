package com.gooman.template.controller;

import com.gooman.template.service.templateService;
import com.gooman.template.entity.Template;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@CrossOrigin(origins = "*", allowedHeaders = "*")
@RestController
@RequestMapping(path="api/v1/templates")
public class templateController {
    //the API endpoints
    @Autowired
    private templateService templateService;


    @GetMapping(path="/test")
    public String test(){
        return templateService.test();
    }

    @GetMapping(path="/all")
    public List<Template> getAllTemplates(){
        return templateService.getTemplates();
    }

    @GetMapping(path="/id={templateId}")
    public Template getTemplateById(@PathVariable int templateId) {
        return templateService.getTemplateById(templateId);
    }

    @GetMapping(path="/name={templateName}")
    public Template getTemplateByTemplateName(@PathVariable String templateName){
        return templateService.getTemplateByTemplateName(templateName);
    }

    @PostMapping
    public String postTemplate(@RequestBody Template template) {
        return templateService.addTemplate(template);
    }

    @PutMapping
    public String updateTemplate(@RequestBody Template template){
        return templateService.updateTemplate(template);
    }

    @DeleteMapping(path="/{templateId}")
    public String deleteTemplate(@PathVariable int templateId){ return templateService.deleteTemplate(templateId); }
}

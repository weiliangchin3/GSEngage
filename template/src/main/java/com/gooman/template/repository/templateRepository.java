package com.gooman.template.repository;

import com.gooman.template.entity.Template;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.data.mongodb.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface templateRepository extends MongoRepository<Template, Integer> {

    Optional<Template> findByTemplateName(String templateName);
}

from config.windchill_objects import OBJECTS
from core.java.builders.output_mapper_builder import OutputMapperBuilder
from models.project_model import ProjectModel


class BusinessLogicGenerator:
    """
    Generates the STARTING content of <Name>BusinessLogic.java.

    ProjectGenerator only calls this the first time a project is generated
    (see the "onceOnly" handling in template.json / ProjectGenerator.generate).
    Once the file exists on disk, later "Generate Project" runs skip it
    entirely, so hand-written business logic here is never overwritten.
    """

    @staticmethod
    def generate(project: ProjectModel) -> str:

        method = project.methods[0]
        windchill_object = OBJECTS[method.root_object]

        mapping = OutputMapperBuilder.generate(method)

        return f"""package {project.java_package};

import java.util.ArrayList;
import java.util.List;

import org.apache.olingo.commons.api.data.ComplexValue;
import org.apache.olingo.commons.api.data.Property;
import org.apache.olingo.commons.api.data.ValueType;

import {windchill_object.package};
import {project.java_package}.model.{method.return_type};

/**
 * Your business logic. Generated ONCE as a working starting point --
 * "Generate Project" never overwrites this file again once it exists, so
 * it is safe to hand-edit (add real queries, filtering, effectivity
 * checks, or whatever the actual requirement needs).
 *
 * If you add or remove output attributes for this project later, update
 * the mapping below by hand -- regenerating will not touch this file.
 */
public class {project.project_name}BusinessLogic {{

    public static Property buildResult({method.root_object} {windchill_object.variable_name}, String oDataObjectType) throws Exception {{

        {mapping}
    }}
}}
"""

from core.java_method_generator import JavaMethodGenerator
from core.java.builders.helper_method_builder import HelperMethodBuilder
from models.project_model import ProjectModel
from config.windchill_objects import OBJECTS


class JavaClassGenerator:

    @staticmethod
    def generate(project: ProjectModel) -> str:

        business_methods = []
        helper_methods = []

        for method in project.methods:
            business_methods.append(JavaMethodGenerator.generate(method))
            helper_methods.append(HelperMethodBuilder.generate(project, method))

        business_methods_text = "\n".join(business_methods)
        helper_methods_text = "\n".join(helper_methods)

        first_method = project.methods[0]
        windchill_object = OBJECTS[first_method.root_object]

        imports = f"""import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Map;

import org.apache.olingo.commons.api.data.ComplexValue;
import org.apache.olingo.commons.api.data.Parameter;
import org.apache.olingo.commons.api.data.Property;
import org.apache.olingo.commons.api.data.ValueType;
import org.apache.olingo.server.api.ODataApplicationException;

import com.ptc.odata.core.entity.function.FunctionProcessorData;

import wt.fc.PersistenceHelper;
import wt.fc.QueryResult;
import wt.query.QuerySpec;
import wt.query.SearchCondition;
import wt.util.WTException;

import {windchill_object.package};
import {project.java_package}.model.{first_method.return_type};"""

        return f"""package {project.java_package};

{imports}

public class {project.java_class} {{

{business_methods_text}

{helper_methods_text}

}}
"""

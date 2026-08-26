from core.java_method_generator import JavaMethodGenerator
from core.retrieval.registry import STRATEGIES
from models.project_model import ProjectModel
from config.windchill_objects import OBJECTS


class JavaClassGenerator:
    """
    Generates <Name>ODataHelper.java -- the OData entry-point plumbing only
    (signature, parameter extraction, retrieval, error handling). This file
    is always regenerated and must never contain business logic: that lives
    in <Name>BusinessLogic.java (see BusinessLogicGenerator), which is
    generated once and never touched again.
    """

    @staticmethod
    def generate(project: ProjectModel) -> str:

        business_methods = []
        helper_methods = []

        for method in project.methods:
            strategy = STRATEGIES[method.retrieval_strategy]
            business_methods.append(JavaMethodGenerator.generate(project, method))
            helper_methods.append(strategy.helper_method_java(project, method))

        business_methods_text = "\n".join(business_methods)
        helper_methods_text = "\n".join(helper_methods)

        first_method = project.methods[0]
        windchill_object = OBJECTS[first_method.root_object]

        imports = f"""import java.util.Locale;
import java.util.Map;

import org.apache.olingo.commons.api.data.Parameter;
import org.apache.olingo.commons.api.data.Property;
import org.apache.olingo.server.api.ODataApplicationException;

import com.ptc.odata.core.entity.function.FunctionProcessorData;

import wt.fc.PersistenceHelper;
import wt.fc.QueryResult;
import wt.query.QuerySpec;
import wt.query.SearchCondition;
import wt.util.WTException;

import {windchill_object.package};"""

        return f"""package {project.java_package};

{imports}

/**
 * GENERATED FILE -- rewritten every time "Generate Project" runs.
 * Business logic lives in {project.project_name}BusinessLogic.java instead,
 * which is generated once and never touched again. Do not hand-edit this
 * file; changes here will be lost on the next regeneration.
 */
public class {project.java_class} {{

{business_methods_text}

{helper_methods_text}

}}
"""

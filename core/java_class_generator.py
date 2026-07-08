from core.java_method_generator import JavaMethodGenerator
from core.java.builders.helper_method_builder import HelperMethodBuilder
from models.project_model import ProjectModel
from config.windchill_objects import OBJECTS


class JavaClassGenerator:

    @staticmethod
    def generate(project: ProjectModel) -> str:

        business_methods = ""
        helper_methods = ""

        for method in project.methods:

            business_methods += JavaMethodGenerator.generate(method) + "\n"

            helper_methods += HelperMethodBuilder.generate(project, method) + "\n"

            method = project.methods[0]
            windchill_object = OBJECTS[method.root_object]

            imports = f"""
            import wt.fc.PersistenceHelper;
            import wt.fc.QueryResult;
            import wt.query.QuerySpec;
            import wt.query.SearchCondition;
            import wt.util.WTException;

            import {windchill_object.package};
            """

            return f"""package {project.java_package};

            {imports}

            public class {project.java_class} {{

            {business_methods}

            {helper_methods}

            }}
            """

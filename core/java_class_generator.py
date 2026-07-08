from core.java_method_generator import JavaMethodGenerator
from models.project_model import ProjectModel


class JavaClassGenerator:

    @staticmethod
    def generate(project: ProjectModel) -> str:

        methods = ""

        for method in project.methods:
            methods += JavaMethodGenerator.generate(method)

        return f"""package {project.java_package};

public class {project.java_class} {{

{methods}

}}
"""

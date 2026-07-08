from config.constants import Placeholders
from models.project_model import ProjectModel


class PlaceholderEngine:
    """
    Replaces placeholders inside template files.
    """

    @staticmethod
    def replace(template_content: str, project: ProjectModel) -> str:
        """
        Replace all placeholders with project values.
        """

        replacements = {
            Placeholders.PROJECT_NAME: project.project_name,
            Placeholders.JAVA_PACKAGE: project.java_package,
            Placeholders.JAVA_CLASS: project.java_class,
            Placeholders.FUNCTION_NAME: project.function_name,
            Placeholders.INPUT_LABEL: project.input_label,
            Placeholders.INPUT_PARAMETER: project.input_parameter,
            Placeholders.OUTPUT_SCHEMA: project.output_schema,
            Placeholders.PROJECT_NAME_LOWER: project.project_name.lower(),
            Placeholders.PROJECT_NAME_UPPER: project.project_name.upper(),
        }

        output = template_content

        for placeholder, value in replacements.items():
            output = output.replace(placeholder, value)

        return output

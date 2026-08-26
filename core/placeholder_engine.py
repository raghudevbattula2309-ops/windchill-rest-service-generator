from config.constants import Placeholders
from config.windchill_objects import OBJECTS
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

        # Version 1 supports one REST method.
        # Future versions will iterate through project.methods.
        method = project.methods[0]

        root_object = OBJECTS[method.root_object]

        replacements = {
            Placeholders.PROJECT_NAME: project.project_name,
            Placeholders.PROJECT_NAME_LOWER: project.project_name.lower(),
            Placeholders.PROJECT_NAME_UPPER: project.project_name.upper(),
            Placeholders.JAVA_PACKAGE: project.java_package,
            Placeholders.JAVA_CLASS: project.java_class,
            Placeholders.FUNCTION_NAME: method.name,
            Placeholders.INPUT_LABEL: method.input_parameters[0].description,
            Placeholders.INPUT_PARAMETER: method.input_parameters[0].name,
            Placeholders.OUTPUT_SCHEMA: method.return_type,
            Placeholders.ROOT_OBJECT: method.root_object,
            Placeholders.NUMBER_ATTRIBUTE: root_object.number_attribute,
            Placeholders.ROOT_OBJECT_PACKAGE: root_object.package,
        }

        output = template_content

        for placeholder, value in replacements.items():
            output = output.replace(placeholder, str(value))

        return output

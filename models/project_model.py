from dataclasses import dataclass


@dataclass
class ProjectModel:
    """
    Stores all information required to generate
    a Windchill REST Service project.
    """

    project_name: str
    java_package: str
    java_class: str
    function_name: str
    input_label: str
    input_parameter: str
    output_schema: str
    output_directory: str

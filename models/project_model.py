from dataclasses import dataclass
from models.input_parameter import InputParameter
from models.method_model import MethodModel


@dataclass
class ProjectModel:
    """
    Stores all information required to generate
    a Windchill REST Service project.
    """

    project_name: str
    java_package: str
    java_class: str
    output_directory: str
    methods: list[MethodModel]

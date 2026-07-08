from core.project_generator import ProjectGenerator
from models.project_model import ProjectModel
from models.input_parameter import InputParameter
from models.method_model import MethodModel
from models.input_parameter import InputParameter
from config.windchill_objects import OBJECTS

method = MethodModel(
    name="getFinalTest",
    input_parameters=[
        InputParameter(name="number", type="String", description="Change Order Number")
    ],
    root_object="WTChangeOrder2",
    retrieval_strategy="NUMBER",
    return_type="ModificationListSchema",
    output_attributes=[
        OBJECTS["WTChangeOrder2"].get_attribute("Number"),
        OBJECTS["WTChangeOrder2"].get_attribute("Name"),
        OBJECTS["WTChangeOrder2"].get_attribute("State"),
    ],
)


project = ProjectModel(
    project_name="FinalTest",
    java_package="ext.geode.finaltest.spsquery",
    java_class="FinalTestODataHelper",
    methods=[method],
    output_directory="output",
)

ProjectGenerator.generate(project)

from core.project_generator import ProjectGenerator
from models.project_model import ProjectModel
from models.input_parameter import InputParameter
from models.method_model import MethodModel
from models.input_parameter import InputParameter
from models.output_attribute import OutputAttribute

method = MethodModel(
    name="getFinalTest",
    input_parameters=[
        InputParameter(name="number", type="String", description="Change Order Number")
    ],
    root_object="WTChangeOrder2",
    retrieval_strategy="NUMBER",
    return_type="ModificationListSchema",
    output_attributes=[
        OutputAttribute(name="number", java_getter="getNumber()", data_type="String"),
        OutputAttribute(name="name", java_getter="getName()", data_type="String"),
        OutputAttribute(
            name="state",
            java_getter="getLifeCycleState().toString()",
            data_type="String",
        ),
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

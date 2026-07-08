from core.project_generator import ProjectGenerator
from models.project_model import ProjectModel

project = ProjectModel(
    project_name="FinalTest",
    java_package="ext.geode.FinalTest.spsquery",
    java_class="FinalTestODataHelper",
    function_name="getFinalTest",
    input_label="Change Order Number",
    input_parameter="number",
    output_schema="ModificationListSchema",
    output_directory="output",
)

ProjectGenerator.generate(project)

from models.project_model import ProjectModel
from models.method_model import MethodModel
from models.input_parameter import InputParameter


class ProjectBuilder:

    def build(
        self,
        project_name: str,
        root_object: str,
        retrieval_strategy: str,
        output_attributes,
    ):

        method = MethodModel(
            name=f"get{project_name}",
            root_object=root_object,
            retrieval_strategy=retrieval_strategy,
            input_parameters=[
                InputParameter(name="number", type="String", description="Number")
            ],
            output_attributes=output_attributes,
            return_type=f"SPSModificationList{project_name}",
        )

        return ProjectModel(
            project_name=project_name,
            java_package=f"ext.geode.{project_name.lower()}.spsquery",
            java_class=f"{project_name}ODataHelper",
            methods=[method],
            output_directory="output",
        )

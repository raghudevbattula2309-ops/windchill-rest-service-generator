from config.settings import Settings
from config.windchill_objects import OBJECTS
from core.placeholder_engine import PlaceholderEngine
from core.retrieval.retrieval_strategy import RetrievalStrategy
from core.template_engine import TemplateEngine
from models.input_parameter import InputParameter
from models.method_model import MethodModel
from models.project_model import ProjectModel


class ByNumberStrategy(RetrievalStrategy):
    """Looks up a single Windchill object by its Number attribute."""

    key = "NUMBER"
    display_name = "By Number"

    def input_parameters(self) -> list[InputParameter]:

        return [InputParameter(name="number", type="String", description="Number")]

    def helper_method_java(self, project: ProjectModel, method: MethodModel) -> str:

        template_path = (
            Settings.TEMPLATE_FOLDER
            / "odata"
            / "java"
            / "retrievers"
            / "get_by_number.template"
        )

        template = TemplateEngine.read(template_path)

        return PlaceholderEngine.replace(template, project)

    def retrieval_statement(self, project: ProjectModel, method: MethodModel) -> str:

        windchill_object = OBJECTS[method.root_object]

        param_names = ", ".join(parameter.name for parameter in method.input_parameters)

        return (
            f"{method.root_object} {windchill_object.variable_name} = "
            f"get{method.root_object}FromNumber({param_names});"
        )

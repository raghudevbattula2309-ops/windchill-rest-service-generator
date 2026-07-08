from pathlib import Path

from config.settings import Settings
from core.placeholder_engine import PlaceholderEngine
from core.template_engine import TemplateEngine
from models.method_model import MethodModel
from models.project_model import ProjectModel


class RetrieverBuilder:

    @staticmethod
    def generate(project: ProjectModel, method: MethodModel) -> str:

        if method.retrieval_strategy != "NUMBER":
            return ""

        template_path = (
            Settings.TEMPLATE_FOLDER
            / "odata"
            / "java"
            / "retrievers"
            / "get_by_number.template"
        )

        template = TemplateEngine.read(template_path)

        return PlaceholderEngine.replace(template, project)

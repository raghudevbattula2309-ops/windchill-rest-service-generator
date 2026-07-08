import json
from pathlib import Path

from config.settings import Settings
from core.file_generator import FileGenerator
from core.folder_creator import FolderCreator
from core.placeholder_engine import PlaceholderEngine
from core.template_engine import TemplateEngine
from models.project_model import ProjectModel


class ProjectGenerator:

    @staticmethod
    def generate(project: ProjectModel):

        # Create folder structure
        FolderCreator.create(project)

        # Read template manifest
        manifest_path = Settings.TEMPLATE_FOLDER / "odata" / "template.json"

        manifest = json.loads(TemplateEngine.read(manifest_path))

        for template_info in manifest["templates"]:

            template_path = (
                Settings.TEMPLATE_FOLDER / "odata" / template_info["template"]
            )

            template_content = TemplateEngine.read(template_path)

            generated_content = PlaceholderEngine.replace(template_content, project)

            target = PlaceholderEngine.replace(template_info["target"], project)

            output = PlaceholderEngine.replace(template_info["output"], project)

            output_file = Settings.OUTPUT_FOLDER / target / output

            FileGenerator.write(output_file, generated_content)

            print(f"Generated : {output_file}")

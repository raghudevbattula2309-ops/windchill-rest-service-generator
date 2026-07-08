from pathlib import Path

from config.settings import Settings
from models.project_model import ProjectModel


class FolderCreator:
    """
    Creates the complete Windchill folder structure
    for a new REST Service project.
    """

    @staticmethod
    def create(project: ProjectModel):

        root = Path(project.output_directory)

        folders = [
            # Documentation
            root
            / Settings.CODEBASE_FOLDER
            / Settings.REST_FOLDER
            / Settings.CUSTOM_FOLDER
            / Settings.DOC_FOLDER,
            # Domain
            root
            / Settings.CODEBASE_FOLDER
            / Settings.REST_FOLDER
            / Settings.CUSTOM_FOLDER
            / Settings.DOMAIN_FOLDER,
            root
            / Settings.CODEBASE_FOLDER
            / Settings.REST_FOLDER
            / Settings.CUSTOM_FOLDER
            / Settings.DOMAIN_FOLDER
            / project.project_name,
            root
            / Settings.CODEBASE_FOLDER
            / Settings.REST_FOLDER
            / Settings.CUSTOM_FOLDER
            / Settings.DOMAIN_FOLDER
            / project.project_name
            / Settings.VERSION_FOLDER,
            root
            / Settings.CODEBASE_FOLDER
            / Settings.REST_FOLDER
            / Settings.CUSTOM_FOLDER
            / Settings.DOMAIN_FOLDER
            / project.project_name
            / Settings.VERSION_FOLDER
            / Settings.COMPLEXTYPE_FOLDER,
            # Java Source
            root
            / Settings.SRC_FOLDER
            / Settings.EXT_FOLDER
            / Settings.GEODE_FOLDER
            / project.project_name.lower()
            / Settings.SPSQUERY_FOLDER,
        ]

        for folder in folders:
            folder.mkdir(parents=True, exist_ok=True)

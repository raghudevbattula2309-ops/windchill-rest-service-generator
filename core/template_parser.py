import json

from models.template import Template
from models.template_metadata import TemplateMetadata


class TemplateParser:
    """
    Parses a template file.

    Expected format:

    ---
    {
        ...
    }
    ---
    """

    @staticmethod
    def parse(template: str) -> Template:

        if not template.startswith("---"):
            raise ValueError("Template metadata not found.")

        parts = template.split("---", 2)

        if len(parts) != 3:
            raise ValueError("Invalid template format.")

        metadata_json = json.loads(parts[1].strip())

        metadata = TemplateMetadata(
            target=metadata_json["target"],
            output=metadata_json["output"],
            description=metadata_json["description"],
            version=metadata_json["version"],
        )

        content = parts[2].lstrip()

        return Template(metadata=metadata, content=content)

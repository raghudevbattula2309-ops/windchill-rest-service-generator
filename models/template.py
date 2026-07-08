from dataclasses import dataclass

from models.template_metadata import TemplateMetadata


@dataclass
class Template:
    """
    Represents a parsed template.
    """

    metadata: TemplateMetadata
    content: str

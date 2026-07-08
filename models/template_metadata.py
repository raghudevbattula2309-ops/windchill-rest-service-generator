from dataclasses import dataclass


@dataclass
class TemplateMetadata:
    """
    Metadata describing how a template should be generated.
    """

    target: str
    output: str
    description: str
    version: str

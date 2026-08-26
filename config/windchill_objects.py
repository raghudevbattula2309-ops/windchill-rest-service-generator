from dataclasses import dataclass
from pathlib import Path

import yaml
from pydantic import BaseModel, ValidationError

from models.windchill_attribute import WindchillAttribute


@dataclass
class WindchillObject:
    name: str
    package: str
    number_attribute: str
    variable_name: str
    attributes: list[WindchillAttribute]

    def get_attribute(self, display_name: str):

        for attribute in self.attributes:

            if attribute.display_name == display_name:
                return attribute

        raise ValueError(f"Attribute '{display_name}' not found in {self.name}")


class _AttributeSchema(BaseModel):
    """Validates one attribute entry in an object catalog YAML file."""

    display_name: str
    dto_field_name: str
    java_getter: str
    data_type: str = "String"
    odata_type: str = "ValueType.PRIMITIVE"


class _ObjectSchema(BaseModel):
    """Validates one Windchill object catalog YAML file (config/objects/*.yaml)."""

    name: str
    package: str
    number_attribute: str
    variable_name: str
    attributes: list[_AttributeSchema] = []


_CATALOG_FOLDER = Path(__file__).resolve().parent / "objects"


def _load_catalog() -> dict[str, WindchillObject]:
    """
    Loads every *.yaml file in config/objects/ into the OBJECTS dict below.

    Each file is validated against _ObjectSchema so a malformed catalog
    entry (a typo'd field, a missing required key) fails immediately with
    a clear error, rather than surfacing later as a confusing generation
    or compile failure.
    """

    objects: dict[str, WindchillObject] = {}

    for yaml_file in sorted(_CATALOG_FOLDER.glob("*.yaml")):

        raw = yaml.safe_load(yaml_file.read_text(encoding="utf-8"))

        try:
            schema = _ObjectSchema(**raw)
        except ValidationError as error:
            raise ValueError(f"Invalid object catalog file '{yaml_file.name}':\n{error}") from error

        objects[schema.name] = WindchillObject(
            name=schema.name,
            package=schema.package,
            number_attribute=schema.number_attribute,
            variable_name=schema.variable_name,
            attributes=[
                WindchillAttribute(
                    display_name=attribute.display_name,
                    dto_field_name=attribute.dto_field_name,
                    java_getter=attribute.java_getter,
                    data_type=attribute.data_type,
                    odata_type=attribute.odata_type,
                )
                for attribute in schema.attributes
            ],
        )

    return objects


OBJECTS = _load_catalog()

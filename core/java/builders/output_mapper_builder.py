from models.method_model import MethodModel
from config.windchill_objects import OBJECTS


class OutputMapperBuilder:

    @staticmethod
    def generate(method: MethodModel) -> str:

        windchill_object = OBJECTS[method.root_object]

        lines = []

        lines.append(f"{method.return_type} item = new {method.return_type}();")

        lines.append("")

        for output_attribute in method.output_attributes:

            metadata = next(
                (
                    attribute
                    for attribute in windchill_object.attributes
                    if attribute.display_name == output_attribute.display_name
                ),
                None,
            )

            if metadata is None:
                continue

            setter = (
                "set" + metadata.dto_field_name[0].upper() + metadata.dto_field_name[1:]
            )

            lines.append(
                f"item.{setter}"
                f"({windchill_object.variable_name}."
                f"{metadata.java_getter});"
            )

        lines.append("")
        lines.append("return item;")

        return "\n        ".join(lines)

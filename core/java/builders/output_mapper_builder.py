from models.method_model import MethodModel
from config.windchill_objects import OBJECTS


class OutputMapperBuilder:

    @staticmethod
    def generate(method: MethodModel) -> str:

        windchill_object = OBJECTS[method.root_object]

        lines = []

        lines.append(f"{method.return_type} item = new {method.return_type}();")

        lines.append("")

        for attribute in method.output_attributes:

            setter = "set" + attribute.name[0].upper() + attribute.name[1:]

            lines.append(
                f"item.{setter}"
                f"({windchill_object.variable_name}."
                f"{attribute.java_getter});"
            )

        lines.append("")
        lines.append("return item;")

        return "\n        ".join(lines)

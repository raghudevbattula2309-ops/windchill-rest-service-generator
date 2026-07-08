from models.method_model import MethodModel


class DTOGenerator:

    @staticmethod
    def generate_fields(method: MethodModel) -> str:

        lines = []

        for attribute in method.output_attributes:
            lines.append(f"    private {attribute.data_type} {attribute.name};")

        return "\n".join(lines)

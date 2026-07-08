from models.method_model import MethodModel


class FieldBuilder:

    @staticmethod
    def generate(method: MethodModel) -> str:

        fields = []

        for attribute in method.output_attributes:
            fields.append(f"    private {attribute.data_type} {attribute.name};")

        return "\n".join(fields)

from models.method_model import MethodModel


class SignatureBuilder:

    @staticmethod
    def generate(method: MethodModel) -> str:

        parameters = []

        for parameter in method.input_parameters:
            parameters.append(f"{parameter.type} {parameter.name}")

        parameter_string = ", ".join(parameters)

        return (
            f"public static Object {method.name}"
            f"({parameter_string}) throws Exception"
        )

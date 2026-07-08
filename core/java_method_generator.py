from models.method_model import MethodModel


class JavaMethodGenerator:

    @staticmethod
    def generate(method: MethodModel) -> str:

        parameters = []

        for parameter in method.input_parameters:
            parameters.append(f"{parameter.type} {parameter.name}")

        parameter_string = ", ".join(parameters)

        return f"""
    public static Object {method.name}({parameter_string}) throws Exception {{

        // ==========================================
        // Root Object
        // ==========================================

        // {method.root_object}

        // Retrieval Strategy:
        // {method.retrieval_strategy}

        // TODO Retrieve Root Object

        // TODO Business Logic

        return null;
    }}
"""

from config.windchill_objects import OBJECTS
from core.java.builders.output_mapper_builder import OutputMapperBuilder
from models.method_model import MethodModel


class JavaMethodGenerator:

    @staticmethod
    def generate(method: MethodModel) -> str:

        parameters = []

        for parameter in method.input_parameters:
            parameters.append(f"{parameter.type} {parameter.name}")

        parameter_string = ", ".join(parameters)

        windchill_object = OBJECTS[method.root_object]

        retrieval = (
            f"{method.root_object} "
            f"{windchill_object.variable_name} = "
            f"get{method.root_object}FromNumber(number);"
        )

        mapping = OutputMapperBuilder.generate(method)

        return f"""
    public static Object {method.name}({parameter_string}) throws Exception {{

        {retrieval}

        {mapping}

    }}
"""

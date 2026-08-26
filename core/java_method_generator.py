from config.windchill_objects import OBJECTS
from core.retrieval.registry import STRATEGIES
from models.method_model import MethodModel
from models.project_model import ProjectModel


class JavaMethodGenerator:

    @staticmethod
    def generate(project: ProjectModel, method: MethodModel) -> str:

        windchill_object = OBJECTS[method.root_object]
        strategy = STRATEGIES[method.retrieval_strategy]

        param_extraction = []
        param_names = []

        for parameter in method.input_parameters:
            param_extraction.append(
                f'        String {parameter.name} = paramMap.get("{parameter.name}").getValue().toString();'
            )
            param_names.append(parameter.name)

        param_extraction_text = "\n".join(param_extraction)
        param_names_text = ", ".join(param_names)

        retrieval = strategy.retrieval_statement(project, method)

        return f"""
    // OData entry point -- called from import.js as helper.{method.name}(data, params)
    public static Property {method.name}(FunctionProcessorData functionProcessorData, Map<String, Parameter> paramMap) throws Exception {{

{param_extraction_text}

        {retrieval}

        if ({windchill_object.variable_name} == null) {{
            throw new ODataApplicationException(
                "ERREUR : Aucun {method.root_object} trouve pour le numero " + {param_names_text},
                500, Locale.FRENCH, "ERR_NOT_FOUND");
        }}

        String oDataObjectType = functionProcessorData.getReturnType().getType().getFullQualifiedName().getFullQualifiedNameAsString();

        // Business logic lives in {project.project_name}BusinessLogic, which is generated
        // once and never overwritten -- see that class to change what gets returned.
        return {project.project_name}BusinessLogic.buildResult({windchill_object.variable_name}, oDataObjectType);
    }}
"""

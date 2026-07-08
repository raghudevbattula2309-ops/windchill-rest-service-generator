from dataclasses import dataclass

from models.input_parameter import InputParameter


@dataclass
class MethodModel:
    """
    Represents one REST method to be generated.
    """

    name: str

    input_parameters: list[InputParameter]

    root_object: str

    retrieval_strategy: str

    return_type: str

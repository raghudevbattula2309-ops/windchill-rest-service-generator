from dataclasses import dataclass
from models.input_parameter import InputParameter
from models.output_attribute import OutputAttribute


@dataclass
class MethodModel:
    """
    Represents one REST method to be generated.
    """

    name: str

    input_parameters: list[InputParameter]

    output_attributes: list[OutputAttribute]

    root_object: str

    retrieval_strategy: str

    return_type: str

from dataclasses import dataclass
from models.input_parameter import InputParameter
from models.windchill_attribute import WindchillAttribute


@dataclass
class MethodModel:
    """
    Represents one REST method to be generated.
    """

    name: str

    input_parameters: list[InputParameter]

    output_attributes: list[WindchillAttribute]

    root_object: str

    retrieval_strategy: str

    return_type: str

from dataclasses import dataclass


@dataclass
class InputParameter:
    """
    Represents one REST input parameter.
    """

    name: str
    type: str
    description: str

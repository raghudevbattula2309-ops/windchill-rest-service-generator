from dataclasses import dataclass


@dataclass
class OutputAttribute:
    """
    One output attribute selected by the user.
    """

    name: str

    java_getter: str

    data_type: str

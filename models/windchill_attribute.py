from dataclasses import dataclass


@dataclass
class WindchillAttribute:
    """
    Describes one attribute of a Windchill object.
    """

    display_name: str

    java_getter: str

    data_type: str

    dto_field_name: str

from dataclasses import dataclass


@dataclass
class WindchillAttribute:
    """
    Metadata describing a Windchill attribute.
    """

    display_name: str

    dto_field_name: str

    java_getter: str

    data_type: str = "String"

    odata_type: str = "ValueType.PRIMITIVE"

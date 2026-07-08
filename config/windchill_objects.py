from dataclasses import dataclass

from models.windchill_attribute import WindchillAttribute


@dataclass
class WindchillObject:
    name: str
    package: str
    number_attribute: str
    variable_name: str
    attributes: list[WindchillAttribute]

    def get_attribute(self, display_name: str):

        for attribute in self.attributes:

            if attribute.display_name == display_name:
                return attribute

        raise ValueError(f"Attribute '{display_name}' not found in {self.name}")


OBJECTS = {
    "WTChangeOrder2": WindchillObject(
        name="WTChangeOrder2",
        package="wt.change2.WTChangeOrder2",
        number_attribute="NUMBER",
        variable_name="changeOrder",
        attributes=[
            WindchillAttribute(
                display_name="Number",
                java_getter="getNumber()",
                data_type="String",
                dto_field_name="number",
            ),
            WindchillAttribute(
                display_name="Name",
                java_getter="getName()",
                data_type="String",
                dto_field_name="name",
            ),
            WindchillAttribute(
                display_name="State",
                java_getter="getLifeCycleState().toString()",
                data_type="String",
                dto_field_name="state",
            ),
            WindchillAttribute(
                display_name="Version",
                java_getter="getVersionIdentifier().getValue()",
                data_type="String",
                dto_field_name="version",
            ),
        ],
    ),
    "WTPart": WindchillObject(
        name="WTPart",
        package="wt.part.WTPart",
        number_attribute="NUMBER",
        variable_name="part",
        attributes=[],
    ),
    "WTDocument": WindchillObject(
        name="WTDocument",
        package="wt.doc.WTDocument",
        number_attribute="NUMBER",
        variable_name="document",
        attributes=[],
    ),
    "ManagedBaseline": WindchillObject(
        name="ManagedBaseline",
        package="wt.vc.baseline.ManagedBaseline",
        number_attribute="NUMBER",
        variable_name="baseline",
        attributes=[],
    ),
}

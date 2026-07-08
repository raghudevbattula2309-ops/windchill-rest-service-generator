from dataclasses import dataclass


@dataclass
class WindchillObject:
    name: str
    package: str
    number_attribute: str
    variable_name: str


OBJECTS = {
    "WTPart": WindchillObject(
        name="WTPart",
        package="wt.part.WTPart",
        number_attribute="NUMBER",
        variable_name="part",
    ),
    "WTDocument": WindchillObject(
        name="WTDocument",
        package="wt.doc.WTDocument",
        number_attribute="NUMBER",
        variable_name="document",
    ),
    "WTChangeOrder2": WindchillObject(
        name="WTChangeOrder2",
        package="wt.change2.WTChangeOrder2",
        number_attribute="NUMBER",
        variable_name="changeOrder",
    ),
    "ManagedBaseline": WindchillObject(
        name="ManagedBaseline",
        package="wt.vc.baseline.ManagedBaseline",
        number_attribute="NUMBER",
        variable_name="baseline",
    ),
}

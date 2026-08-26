from abc import ABC, abstractmethod

from models.input_parameter import InputParameter
from models.method_model import MethodModel
from models.project_model import ProjectModel


class RetrievalStrategy(ABC):
    """
    One way of locating the Windchill object(s) a REST method builds its
    response from -- e.g. "by its Number", "by OID", "by a related object".

    Each strategy owns everything specific to that lookup: which input
    parameters the REST call needs, the private Java helper method that
    performs the lookup, and the statement that calls that helper from the
    generated entry-point method. Adding a new way to retrieve data means
    adding a new strategy here and registering it in registry.py -- not
    editing the generators that build the rest of the class.

    Subclasses must set the `key` (stored on MethodModel.retrieval_strategy
    and used as the registry lookup key) and `display_name` (shown in the
    UI) class attributes.
    """

    key: str
    display_name: str

    @abstractmethod
    def input_parameters(self) -> list[InputParameter]:
        """The REST input parameters this strategy needs."""

    @abstractmethod
    def helper_method_java(self, project: ProjectModel, method: MethodModel) -> str:
        """The private Java helper method that performs the lookup."""

    @abstractmethod
    def retrieval_statement(self, project: ProjectModel, method: MethodModel) -> str:
        """
        The Java statement(s), inside the entry-point method, that call
        the helper method above and assign its result to the object
        variable used by the rest of that method.
        """

from core.retrievers.wtpart_retriever import WTPartRetriever
from core.retrievers.wtdocument_retriever import WTDocumentRetriever
from core.retrievers.wtchangeorder2_retriever import WTChangeOrder2Retriever
from core.retrievers.managedbaseline_retriever import ManagedBaselineRetriever


class RetrieverFactory:

    @staticmethod
    def get(root_object: str):

        if root_object == "WTPart":
            return WTPartRetriever()

        if root_object == "WTDocument":
            return WTDocumentRetriever()

        if root_object == "WTChangeOrder2":
            return WTChangeOrder2Retriever()

        if root_object == "ManagedBaseline":
            return ManagedBaselineRetriever()

        raise ValueError(f"Unsupported root object: {root_object}")

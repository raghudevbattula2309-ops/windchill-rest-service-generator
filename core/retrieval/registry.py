from core.retrieval.by_number_strategy import ByNumberStrategy
from core.retrieval.retrieval_strategy import RetrievalStrategy

# Every available retrieval strategy, keyed by RetrievalStrategy.key.
# Add a new way to look up data by adding a new RetrievalStrategy
# subclass and listing an instance of it here -- nothing else needs to
# change to make it available in the UI and to the generators.
STRATEGIES: dict[str, RetrievalStrategy] = {
    strategy.key: strategy
    for strategy in [
        ByNumberStrategy(),
    ]
}

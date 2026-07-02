from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class InventoryItem:
    service: str
    resource: str
    metadata: Dict[str, Any]


@dataclass
class InventorySnapshot:
    items: List[InventoryItem]


class InventoryProvider:
    """
    Abstract inventory provider.

    Later we will implement:
    - AWSInventoryProvider (boto3)
    - MockInventoryProvider (tests/dev)
    """

    def collect(self) -> InventorySnapshot:
        raise NotImplementedError("Inventory provider not implemented yet")

from dataclasses import dataclass
from typing import List, Dict, Any


@dataclass
class ServiceResult:
    message: str


@dataclass
class Success:
    value: ServiceResult
    status: str = "success"


@dataclass
class Failure:
    error: str
    status: str = "error"


@dataclass
class InventoryItem:
    service: str
    resource: str
    metadata: Dict[str, Any]


@dataclass
class InventorySnapshot:
    items: List[InventoryItem]

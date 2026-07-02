from __future__ import annotations

from dataclasses import dataclass, field

from platformiq.model.entity import Entity
from platformiq.model.resource import Resource


@dataclass(frozen=True)
class Snapshot(Entity):
    """
    Represents a point-in-time infrastructure snapshot.

    A snapshot contains the resources discovered during a single
    inventory collection.
    """

    resources: tuple[Resource, ...] = field(default_factory=tuple)

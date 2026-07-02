from __future__ import annotations

from dataclasses import dataclass, field

from platformiq.model.resource import Resource


@dataclass(frozen=True)
class DiffResult:
    """
    Represents the result of comparing two infrastructure snapshots.
    """

    created: tuple[Resource, ...] = field(default_factory=tuple)
    deleted: tuple[Resource, ...] = field(default_factory=tuple)
    modified: tuple[Resource, ...] = field(default_factory=tuple)

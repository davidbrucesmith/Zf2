from __future__ import annotations

from typing import List, TypeVar

T = TypeVar("T")

def swap_adjacent_pairs(measures: List[T]) -> List[T]:
    """Swap each adjacent measure pair, leaving an odd tail measure in place."""
    swapped: List[T] = []
    for i in range(0, len(measures), 2):
        if i + 1 < len(measures):
            swapped.extend([measures[i + 1], measures[i]])
        else:
            swapped.append(measures[i])
    return swapped


def retrograde(measures: List[T]) -> List[T]:
    """Return measures in reverse order."""
    return list(reversed(measures))


def permute_by_indices(measures: List[T], index_pattern: List[int]) -> List[T]:
    """
    Reorder measures by an explicit zero-based index pattern.

    Example:
        measures = [m0, m1, m2]
        index_pattern = [2, 0, 1]
        result = [m2, m0, m1]
    """
    if len(index_pattern) != len(measures):
        raise ValueError(
            "index_pattern length must match number of selected measures "
            f"({len(index_pattern)} != {len(measures)})"
        )

    max_valid = len(measures) - 1
    for idx in index_pattern:
        if idx < 0 or idx > max_valid:
            raise IndexError(
                f"Permutation index {idx} is out of bounds for "
                f"{len(measures)} measures"
            )

    return [measures[i] for i in index_pattern]

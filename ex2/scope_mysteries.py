#!/usr/bin/env python3
from typing import Callable


def mage_counter() -> Callable[[], int]:
    count: int = 1

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    def acc(add: int) -> int:
        return add + initial_power
    return acc


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    def formatting(item_name: str) -> str:
        return f"{item_name} {enchantment_type}"
    return formatting


def memory_vault() -> dict[str, Callable:
    vault = {}

    return store

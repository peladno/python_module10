#!/usr/bin/env python3
from typing import Any, Callable


def mage_counter() -> Callable[[], int]:
    """
    Create a counter function that remembers its internal state.

    Returns
    -------
    Callable[[], int]
        A function that increments and returns an internal counter
        each time it is called.

    Notes
    -----
    Demonstrates lexical scoping and closures: the inner function
    captures and mutates the `count` variable from the outer scope.
    """
    count: int = 1

    def counter() -> int:
        nonlocal count
        count += 1
        return count
    return counter


def spell_accumulator(initial_power: int) -> Callable[[int], int]:
    """
    Create a spell accumulator that adds a base power to any input.

    Parameters
    ----------
    initial_power : int
        The base power that will be added to future values.

    Returns
    -------
    Callable[[int], int]
        A function that takes an integer and returns it plus `initial_power`.

    Notes
    -----
    Demonstrates closures: the returned function remembers `initial_power`.
    """
    def acc(add: int) -> int:
        return add + initial_power
    return acc


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:
    """
    Create a function that applies an enchantment type to item names.

    Parameters
    ----------
    enchantment_type : str
        The enchantment descriptor (e.g., "of Fire").

    Returns
    -------
    Callable[[str], str]
        A function that formats item names with the enchantment.
    """
    def formatting(item_name: str) -> str:
        return f"{item_name} {enchantment_type}"
    return formatting


def memory_vault() -> dict[str, Callable[..., Any]]:
    """
    Create a memory storage system using closures.

    Returns
    -------
    dict[str, Callable[..., Any]]
        A dictionary containing:
        - 'store': function to store a key-value pair
        - 'recall': function to retrieve a value or return "Memory not found"

    Notes
    -----
    The internal `vault` dictionary is private and persists thanks to
    lexical scoping. No global variables are used.
    """
    vault: dict[Any, Any] = {}

    def store(key: Any, value: Any) -> None:
        """Store a value under a given key."""
        vault[key] = value

    def recall(key: Any) -> Any:
        """Retrieve a stored value or return 'Memory not found'."""
        if key in vault:
            return vault[key]
        return "Memory not found"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """
    Run demonstrations for all closure-based functions in this module.

    This includes:
    - mage_counter: persistent counter
    - spell_accumulator: power accumulator
    - enchantment_factory: item enchantment formatter
    - memory_vault: private memory storage system
    """
    print("=== Testing mage_counter ===")
    counter1 = mage_counter()
    counter2 = mage_counter()

    print(counter1())   # 2
    print(counter1())   # 3
    print(counter2())   # 2
    print(counter2())   # 3

    print("\n=== Testing spell_accumulator ===")
    acc = spell_accumulator(10)
    print(acc(5))       # 15
    print(acc(20))      # 30

    print("\n=== Testing enchantment_factory ===")
    enchant = enchantment_factory("of Fire")
    print(enchant("Sword"))   # Sword of Fire
    print(enchant("Shield"))  # Shield of Fire

    print("\n=== Testing memory_vault ===")
    vault = memory_vault()

    vault["store"]("name", "Javier")
    vault["store"]("level", 42)

    print(vault["recall"]("name"))     # Javier
    print(vault["recall"]("level"))    # 42
    print(vault["recall"]("missing"))  # Memory not found


if __name__ == "__main__":
    main()

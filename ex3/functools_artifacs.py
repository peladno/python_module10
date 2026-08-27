#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    """Combines a list of spell numerical values using functools.reduce.

    Args:
        spells: A list of integers representing spell values.
        operation: The operation to perform ('add', 'multiply', 'max', 'min').

    Returns:
        The reduced integer result of the operation.

    Raises:
        Exception: If the operation is not supported.
    """
    if not spells:
        return 0

    operacions = {
        "add": reduce(operator.add, spells),
        "multiply": reduce(operator.mul, spells),
        "max": reduce(max, spells),
        "min": reduce(min, spells)
    }

    if operation not in operacions:
        raise Exception("Operation invalid")
    else:
        return operacions[operation]


def reducer_test() -> None:
    """Runs test cases for spell_reducer."""
    print("=== TESTING spell_reducer ===\n")

    # Casos de prueba
    spells1: list[int] = [10, 20, 30]
    spells2: list[int] = [5]
    spells_empty: list[int] = []

    operations = ["add", "multiply", "max", "min", "unknown"]

    for op in operations:
        print(f"Operation: {op}")

        try:
            print("  spells1:", spell_reducer(spells1, op))
            print("  spells2:", spell_reducer(spells2, op))
            print("  empty:  ", spell_reducer(spells_empty, op))
        except Exception as e:
            print("  ERROR:", e)

        print()


def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:
    """Creates a dictionary of specialized enchantment functions using
    functools.partial.

    Args:
        base_enchantment: A callable taking power (int), element (str),
        and item (str).

    Returns:
        A dictionary mapping element names to partial functions
        expecting only an item name.
    """
    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


def partial_test() -> None:
    """Runs test cases for partial_enchanter."""
    print("=== TESTING partial_enchanter ===\n")

    def base_enchantment(power: int, element: str, item: str) -> str:
        return f"{item} enchanted with {element} +{power}"

    spells: dict[
        str, Callable[[str], str]
        ] = partial_enchanter(base_enchantment)

    print(spells["fire"]("Sword"))
    print(spells["ice"]("Shield"))
    print(spells["lightning"]("Bow"))
    print()


@lru_cache
def memoized_fibonacci(n: int) -> int:
    """Computes the n-th Fibonacci number using functools.lru_cache
    for memoization.

    Args:
        n: Non-negative integer index in the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.
    """
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def memo_test() -> None:
    """Runs test cases for memoized_fibonacci."""
    print("=== TESTING memoized_fibonacci ===\n")

    print(memoized_fibonacci(10))


def spell_dispatcher() -> Callable[[Any], str]:
    """Creates a single-dispatch spell caster function using
    functools.singledispatch.

    Returns:
        A function that dispatches execution based on
        the type of the spell argument.
    """
    @singledispatch
    def cast(spell: Any) -> str:
        return f"Unknown spell type: {type(spell).__name__}"

    @cast.register
    def _(spell: int) -> str:
        return f"Damage spell cast! You deal {spell} points of damage."

    @cast.register
    def _(spell: str) -> str:
        return f"Enchantment spell cast! You imbue: '{spell}'."

    @cast.register(list)
    def _(spell: list[Any]) -> str:
        results = [cast(s) for s in spell]
        return "Multi-cast:\n" + "\n".join(results)

    return cast


def dispatch_test() -> None:
    """Runs test cases for spell_dispatcher."""
    print("=== TESTING spell_dispacher ===\n")
    caster = spell_dispatcher()
    print(caster(50))
    print(caster("fire aura"))
    print(caster([10, "ice shard"]))
    print(caster(3.14))


if __name__ == "__main__":
    reducer_test()
    partial_test()
    memo_test()
    dispatch_test()

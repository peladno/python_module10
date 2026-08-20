#!/usr/bin/env python3
from functools import reduce, partial, lru_cache
import operator
from typing import Any, Callable


def spell_reducer(spells: list[int], operation: str) -> int:
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


# def partial_enchanter(
#     base_enchantment: Callable[[str, int, str], str]
# ) -> dict[str, Callable[[str], str]]:

#     def enchant(item: str, power: int, element: str) -> str:
#         return base_enchantment(item, power, element)

#     return {
#         "fire": partial(enchant, power=50, element="fire"),
#         "ice": partial(enchant, power=50, element="ice"),
#         "lightning": partial(enchant, power=50, element="lightning"),
#     }

def partial_enchanter(
    base_enchantment: Callable[[int, str, str], str]
) -> dict[str, Callable[[str], str]]:

    return {
        "fire": partial(base_enchantment, 50, "fire"),
        "ice": partial(base_enchantment, 50, "ice"),
        "lightning": partial(base_enchantment, 50, "lightning"),
    }


def partial_test() -> None:
    print("=== TESTING partial_enchanter ===\n")

    def base_enchantment(power: int, element: str, item: str) -> str:
        return f"{item} enchanted with {element} +{power}"

    spells: dict[
        str, Callable[[str], str]
        ] = partial_enchanter(base_enchantment)

    print(spells["fire"]("Sword"))
    print(spells["ice"]("Shield"))
    print(spells["lightning"]("Bow"))


@lru_cache
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def memo_test() -> None:
    print("=== TESTING memoized_fibonacci ===\n")

    print(memoized_fibonacci(10))


def spell_dispatcher() -> Callable[[Any], str]:
    raise NotImplementedError("Not implemented yet")


if __name__ == "__main__":
    reducer_test()
    partial_test()
    memo_test()

"""Module demonstrating custom decorators: timing and argument validation."""

from functools import wraps
import random
from typing import Any, Callable
from time import time, sleep


def spell_timer(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator that measures and prints the execution time of a function."""
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print(f"Casting function {func.__name__}")
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"{func.__name__} completed in {(t2 - t1):.3f} seconds")
        return result

    return wrapper


@spell_timer
def spell(spell_name: str) -> str:
    """Simulates casting a spell with a delay."""
    sleep(1.5)
    return f"Throw {spell_name}!!!!!"


def power_validator(
        min_power: int
        ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory that validates numerical spell power arguments.

    Args:
        min_power: Minimum power required to cast the spell.

    Returns:
        Decorator function that checks spell arguments before execution.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        ERROR = "Insufficient power for this spell"

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for arg in args:
                if isinstance(arg, (int, float)) and arg < min_power:
                    return ERROR
            for value in kwargs.values():
                if isinstance(value, (int, float)) and value < min_power:
                    return ERROR
            return func(*args, **kwargs)
        return wrapper
    return decorator


@power_validator(50)
def spell2(power: int) -> str:
    """Casts a fire spell with validated power."""
    return f"BURN!!!!!!!!, power: {power}"


def retry_spell(max_attempts: int) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            attemps = 0
            while attemps < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    attemps += 1
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {attemps}/{max_attempts})"
                        )
                    if attemps >= max_attempts:
                        return (
                            f"Spell casting failed after "
                            f"{max_attempts} attempts")
                    sleep(1)
        return wrapper
    return decorator


@retry_spell(3)
def fail_spell(x: int) -> str | None:
    if x < 5:
        raise ValueError("Value too small!")
    return "Fireball!"


@retry_spell(5)
def random_spell() -> str:
    """Spell with a 60% chance of failing on each try."""
    if random.random() < 0.6:
        raise RuntimeError("Spell fizzled out!")
    return "Lighting bolt strike!"


class MageGuild():
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return (
            "Successfully cast spell_name with "
            f"<{spell_name}> {power} power"
            )


if __name__ == "__main__":
    print(spell("fire ball"))
    print()
    print(spell2(100))
    print(spell2(power=30))
    print()
    print(random_spell())
    print()
    print(fail_spell(2))
    print()
    name = "Gandalf"
    print(f"Validating name: {name},", MageGuild.validate_mage_name(name))
    cast = MageGuild()
    print(cast.cast_spell("Fireball", 15))
    print(cast.cast_spell("Fireball", 9))

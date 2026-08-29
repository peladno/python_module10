"""Module demonstrating custom decorators: timing and argument validation."""

from functools import wraps
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


def power_validator(min_power: int) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Decorator factory that validates numerical spell power arguments.

    Args:
        min_power: Minimum power required to cast the spell.

    Returns:
        Decorator function that checks spell arguments before execution.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for arg in args:
                if isinstance(arg, (int, float)) and arg < min_power:
                    raise ValueError("Insufficient power for this spell")
            for value in kwargs.values():
                if isinstance(value, (int, float)) and value < min_power:
                    raise ValueError("Insufficient power for this spell")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@power_validator(50)
def spell2(power: int) -> str:
    """Casts a fire spell with validated power."""
    return f"BURN!!!!!!!!, power: {power}"


if __name__ == "__main__":
    print(spell("fire ball"))
    print(spell2(100))

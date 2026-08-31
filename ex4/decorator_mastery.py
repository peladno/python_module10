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

# TODO
# retry_spell(max_attempts) - Retry decorator:
# • Create a decorator that retries failed spells
# • If function raises an exception, retry up to max_attempts times
# • Print "Spell failed, retrying... (attempt n/max_attempts)"
# • If all attempts fail, return "Spell casting failed after max_attempts attempts"
# • If one attempt succeeds, return its result normally


# CHECK example:
# def do_something():
#     # Simulate a network request or flaky function
#     raise ConnectionError("Server timed out")

# max_retries = 3
# delay = 2  # seconds

# for attempt in range(1, max_retries + 1):
#     try:
#         print(f"Attempt {attempt}: Trying to execute function...")
#         result = do_something()
#         # If successful, break out of the loop
#         print("Success!")
#         break
#     except ConnectionError as e:
#         print(f"Error encountered: {e}")
#         if attempt < max_retries:
#             print(f"Retrying in {delay} seconds...")
#             time.sleep(delay)
#         else:
#             print("All retry attempts failed.")
#             raise e  # Re-raise the error if all attempts exhaust


# TODO
# MageGuild class - Demonstrate staticmethod:
# • validate_mage_name(name) - Static method that checks if name is valid
# • Name is valid if it’s at least 3 characters and contains only letters/spaces
# • cast_spell(self, spell_name, power) - Instance method
# • Should use the power_validator decorator with min_power=10
# • When power is valid, return "Successfully cast spell_name with <power> power"
# • Otherwise return "Insufficient power for this spell"


if __name__ == "__main__":
    print(spell("fire ball"))
    print()
    print(spell2(100))
    print(spell2(power=30))
    print()

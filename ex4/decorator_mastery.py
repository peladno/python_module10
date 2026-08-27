from typing import Any, Callable
from time import time, sleep


def spell_timer(func: Callable[[Any], Any]) -> Callable[[Any], Any]:

    def wrap_func(*args: Any, **kwargs: Any) -> Any:
        print("Casting function", func.__name__)
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"{__name__} completed in {(t2-t1):.3f} seconds")
        return result

    return wrap_func


@spell_timer
def spell(spell: str) -> str:
    sleep(1.5)
    return f"Throw {spell}!!!!!"


if __name__ == "__main__":
    print(spell("fire ball"))

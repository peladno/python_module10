#!/usr/bin/env python3
from typing import Any, Callable


Spell = Callable[[str, int], str]
test_values = [9, 15, 250]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def heal(target: str, power: int) -> str:
    return f"✨ Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    return f"🔥 Fireball hits {power} to {target}"


def strong_enough(_: str, power: int) -> bool:
    return power >= 50


def spell_combiner(spell1: Spell,
                   spell2: Spell) -> Callable[[str, int], tuple[str, str]]:
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Callable[[str, int], str],
                    multiplier: int) -> Callable[[str, int], str]:
    def amplified_spell(target: str, power: int) -> str:
        amplified_power = power * multiplier
        return base_spell(target, amplified_power)
    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Spell) -> Callable[[str, int], Any]:
    def conditional(target: str, power: int) -> Any:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def test_amplifier() -> None:
    print("=== TESTING SPELL AMPLIFIER ===\n")
    mega_fireball = power_amplifier(fireball, 3)

    for target in test_targets:
        for power in test_values:
            print("Original:", fireball(target, power))
            print("Amplified:", mega_fireball(target, power), end="\n\n")


def test_combiner() -> None:

    combined = spell_combiner(fireball, heal)
    print("=== TESTING SPELL COMBINER ===\n")

    for target in test_targets:
        for power in test_values:
            result = combined(target, power)
            print(f"Target: {target}, Power: {power}")
            print(f"  Fireball: {result[0]}")
            print(f"  Heal:     {result[1]}")
            print()


if __name__ == "__main__":
    test_combiner()
    test_amplifier()

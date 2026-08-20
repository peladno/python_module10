#!/usr/bin/env python3
from typing import Any, Callable


Spell = Callable[[str, int], str]
test_values = [9, 15, 250]
test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']


def heal(target: str, power: int) -> str:
    """
    Cast a healing spell on a target.

    Parameters
    ----------
    target : str
        The entity receiving healing.
    power : int
        The amount of HP restored.

    Returns
    -------
    str
        A formatted healing message.
    """
    return f"✨ Heal restores {target} for {power} HP"


def fireball(target: str, power: int) -> str:
    """
    Cast a fireball spell on a target.

    Parameters
    ----------
    target : str
        The entity being hit.
    power : int
        The damage dealt.

    Returns
    -------
    str
        A formatted fireball attack message.
    """
    return f"🔥 Fireball hits {power} to {target}"


def strong_enough(_: str, power: int) -> bool:
    """
    Check whether a spell's power meets the minimum threshold.

    Parameters
    ----------
    _ : str
        Ignored target parameter.
    power : int
        The power level to evaluate.

    Returns
    -------
    bool
        True if power >= 50, otherwise False.
    """
    return power >= 50


def spell_combiner(spell1: Spell,
                   spell2: Spell) -> Callable[[str, int], tuple[str, str]]:
    """
    Combine two spells into a single dual‑cast spell.

    Parameters
    ----------
    spell1 : Spell
        The first spell to cast.
    spell2 : Spell
        The second spell to cast.

    Returns
    -------
    Callable[[str, int], tuple[str, str]]
        A function that casts both spells on a target with a given power.
    """
    def combined_spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return combined_spell


def power_amplifier(base_spell: Spell,
                    multiplier: int) -> Spell:
    """
    Amplify the power of a base spell by a multiplier.

    Parameters
    ----------
    base_spell : Spell
        The spell to amplify.
    multiplier : int
        The factor by which the spell's power is multiplied.

    Returns
    -------
    Spell
        A new spell function with amplified power.
    """
    def amplified_spell(target: str, power: int) -> str:
        amplified_power: int = power * multiplier
        return base_spell(target, amplified_power)
    return amplified_spell


def conditional_caster(condition: Callable[[str, int], bool],
                       spell: Spell) -> Callable[[str, int], Any]:
    """
    Cast a spell only if a given condition is met.

    Parameters
    ----------
    condition : Callable[[str, int], bool]
        A predicate determining whether the spell should be cast.
    spell : Spell
        The spell to cast if the condition is satisfied.

    Returns
    -------
    Callable[[str, int], Any]
        A function that casts the spell or returns 'Spell fizzled'.
    """
    def conditional(target: str, power: int) -> Any:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Spell]) -> Callable[[str, int], list[str]]:
    """
    Cast a sequence of spells in order.

    Parameters
    ----------
    spells : list[Spell]
        A list of spell functions to cast sequentially.

    Returns
    -------
    Callable[[str, int], list[str]]
        A function that casts all spells on a target with a given power.
    """
    def sequence(target: str, power: int) -> list[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def test_amplifier() -> None:
    """
    Test the power amplifier by comparing original and amplified fireballs.
    """
    print("=== TESTING SPELL AMPLIFIER ===\n")
    mega_fireball = power_amplifier(fireball, 3)

    for target in test_targets:
        for power in test_values:
            print("Original:", fireball(target, power))
            print("Amplified:", mega_fireball(target, power), end="\n\n")


def test_combiner() -> None:
    """
    Test the spell combiner by casting fireball and heal together.
    """
    print("=== TESTING SPELL COMBINER ===\n")
    combined = spell_combiner(fireball, heal)

    for target in test_targets:
        for power in test_values:
            result = combined(target, power)
            print(f"Target: {target}, Power: {power}")
            print(f"  Fireball: {result[0]}")
            print(f"  Heal:     {result[1]}")
            print()


def test_conditional() -> None:
    """
    Test the conditional caster using the strong_enough predicate.
    """
    print("=== TESTING CONDITIONAL CASTER ===\n")
    conditional_fireball = conditional_caster(strong_enough, fireball)

    for target in test_targets:
        for power in test_values:
            result = conditional_fireball(target, power)
            print(f"Target: {target}, Power: {power}")
            print(f"  Result: {result}\n")


def test_sequence() -> None:
    """
    Test the spell sequence caster with heal and fireball.
    """
    print("=== TESTING SEQUENCE CASTER ===\n")
    spell_list: list[Spell] = [heal, fireball]
    sequense = spell_sequence(spell_list)

    for target in test_targets:
        for power in test_values:
            result = sequense(target, power)
            print(f"Target: {target}, Power: {power}")
            print(f"  Result: {result}\n")


if __name__ == "__main__":
    test_combiner()
    test_amplifier()
    test_conditional()
    test_sequence()

#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Sort artifacts by their 'power' attribute in descending order.

    Parameters
    ----------
    artifacts : list[dict[str, Any]]
        A list of artifact dictionaries,
        each containing at least a 'power' key.

    Returns
    -------
    list[dict[str, Any]]
        The artifacts sorted from highest to lowest power.
    """
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    """
    Filter mages whose power is greater than or equal to a minimum threshold.

    Parameters
    ----------
    mages : list[dict[str, Any]]
        A list of mage dictionaries containing a 'power' key.
    min_power : int
        The minimum power required for a mage to be included.

    Returns
    -------
    list[dict[str, Any]]
        A list of mages meeting or exceeding the power requirement.
    """
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transform a list of spell names by wrapping each one with
    decorative markers.

    Parameters
    ----------
    spells : list[str]
        A list of spell names.

    Returns
    -------
    list[str]
        A list of transformed spell names, each wrapped with '* ... *'.
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    """
    Compute basic statistics (max, min, average power) for a list of mages.

    Parameters
    ----------
    mages : list[dict[str, Any]]
        A list of mage dictionaries containing a 'power' key.

    Returns
    -------
    dict[str, float]
        A dictionary with:
        - 'max_power': highest mage power
        - 'min_power': lowest mage power
        - 'avg_power': average mage power rounded to 2 decimals
    """
    max_power = max(mages, key=lambda mage: mage['power'])
    min_power = min(mages, key=lambda mage: mage['power'])
    avg = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {
        'max_power': max_power['power'],
        'min_power': min_power['power'],
        'avg_power': avg
    }


def lambda_spells() -> None:
    """
    Demonstrate the use of artifact sorting, mage filtering,
    spell transformation, and mage statistics.

    This function builds sample datasets and prints the results
    of applying the utility functions defined above.
    """
    artifacts: list[dict[str, Any]] = [
        {'name': 'Aegis Flame', 'power': 120, 'type': 'weapon'},
        {'name': 'Wind Amulet', 'power': 45, 'type': 'accessory'},
        {'name': 'Titan Breastplate', 'power': 200, 'type': 'armor'},
        {'name': 'Ring of Stealth', 'power': 30, 'type': 'accessory'},
        {'name': "Oracle's Staff", 'power': 150, 'type': 'weapon'},
        {'name': 'Ether Vial', 'power': 80, 'type': 'consumable'},
        {'name': 'Gauntlets of Strength', 'power': 95, 'type': 'equipment'},
        {'name': 'Star Map', 'power': 10, 'type': 'tool'},
        {'name': 'Scepter of Ruin', 'power': 175, 'type': 'weapon'},
        {'name': 'Guardian Plate', 'power': 110, 'type': 'armor'},
    ]

    spells: list[str] = [
        "Fireball",
        "Ice Lance",
        "Healing Light",
        "Stone Skin",
        "Thunderclap",
        "Windwalk",
        "Mana Shield",
        "Curse of Weakness",
        "Blessing",
        "Meteor Storm",
    ]

    mages: list[dict[str, Any]] = [
        {"name": "Arin", "power": 120, "element": "fire"},
        {"name": "Selene", "power": 95, "element": "water"},
        {"name": "Borin", "power": 150, "element": "earth"},
        {"name": "Lyra", "power": 110, "element": "air"},
        {"name": "Tharos", "power": 175, "element": "lightning"},
        {"name": "Eira", "power": 130, "element": "ice"},
        {"name": "Mordai", "power": 160, "element": "shadow"},
        {"name": "Kael", "power": 140, "element": "arcane"},
        {"name": "Ivy", "power": 85, "element": "nature"},
        {"name": "Lumina", "power": 155, "element": "light"},
    ]

    print(artifact_sorter(artifacts))
    print()
    print(power_filter(mages, 110))
    print()
    print(spell_transformer(spells))
    print()
    print(mage_stats(mages))


if __name__ == "__main__":
    lambda_spells()

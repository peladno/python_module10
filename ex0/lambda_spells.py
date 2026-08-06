#!/usr/bin/env python3
from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(artifacts, key=lambda x: x['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]],
                 min_power: int) -> list[dict[str, Any]]:
    return list(filter(lambda x: x['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, float]:
    max_power = max(mages, key=lambda mage: mage['power'])
    min_power = min(mages, key=lambda mage: mage['power'])
    avg = round(sum(map(lambda m: m['power'], mages)) / len(mages), 2)

    return {'max_power': max_power['power'],
            'min_power': min_power['power'],
            'avg_power': avg}


def lambda_spells() -> None:

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

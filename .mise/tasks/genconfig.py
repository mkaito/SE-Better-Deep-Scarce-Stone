#!/usr/bin/env python3
# fmt: off
#MISE description="Regenerate pog-config.json.template from this script's source-of-truth dicts."
# fmt: on
"""Source of truth for BDSS ore distribution. See doc/ore-design.md and doc/pog.md."""

from __future__ import annotations

import json
from pathlib import Path

# id_base = lowest of 5 consecutive variant IDs. colour drives POG hint maps; optional.
BASE_ORES = {
    # T1 (Fe / Ni / Si) — IDs 1-30
    "iron": dict(type="Iron_02", id_base=1, surfaceArea=270, startDepth=50, depth=150, colour="fc0707"),
    "heazlewoodite": dict(type="Heazlewoodite_01", id_base=6, surfaceArea=180, startDepth=60, depth=150),
    "taenite": dict(type="Taenite_01", id_base=11, surfaceArea=170, startDepth=50, depth=150, colour="914a34"),
    "hapkeite": dict(type="Hapkeite_01", id_base=16, surfaceArea=240, startDepth=50, depth=120, colour="914a34"),
    "sinoite": dict(type="Sinoite_01", id_base=21, surfaceArea=75, startDepth=70, depth=150),
    "quartz": dict(type="Quartz_01", id_base=26, surfaceArea=200, startDepth=50, depth=180),
    # 2H (modded, special) — IDs 40-49
    "deuterium": dict(type="Deuterium", id_base=40, surfaceArea=684, startDepth=800, depth=600, colour="d812ea"),
    "denseDeuterium": dict(type="DenseDeuterium", id_base=45, surfaceArea=657, startDepth=1000, depth=700, colour="d812ea"),
    # Caixirite (OPC 3719884258) IDs 50-54. Voxel MinedOreRatio=0.01 (300× lower than LTP=3) → oversized deposits.
    "caixirite": dict(type="Caixirite_Raw", id_base=50, surfaceArea=1200, startDepth=900, depth=1300, colour="ff6b9a"),
    # T2 (Co / Mg / Ag) — IDs 100-149
    "akimotoite": dict(type="Akimotoite_01", id_base=100, surfaceArea=270, startDepth=120, depth=180, colour="68fc0c"),
    "wadsleyite": dict(type="Wadsleyite_01", id_base=105, surfaceArea=235, startDepth=120, depth=180, colour="68fc0c"),
    "olivine": dict(type="Olivine_01", id_base=110, surfaceArea=115, startDepth=130, depth=200, colour="68fc0c"),
    "dolomite": dict(type="Dolomite_01", id_base=115, surfaceArea=110, startDepth=140, depth=200, colour="68fc0c"),
    "cattierite": dict(type="Cattierite_01", id_base=120, surfaceArea=215, startDepth=140, depth=200, colour="7db9e8"),
    "cohenite": dict(type="Cohenite_01", id_base=125, surfaceArea=217, startDepth=130, depth=200),
    "kamacite": dict(type="Kamacite_01", id_base=130, surfaceArea=270, startDepth=120, depth=180, colour="7db9e8"),
    "glaucodot": dict(type="Glaucodot_01", id_base=135, surfaceArea=220, startDepth=120, depth=200, colour="7db9e8"),
    "galena": dict(type="Galena_01", id_base=140, surfaceArea=110, startDepth=150, depth=200),
    "chlorargyrite": dict(type="Chlorargyrite_01", id_base=145, surfaceArea=320, startDepth=180, depth=220),
    # T3 (Au) — IDs 150-169
    "electrum": dict(type="Electrum_01", id_base=150, surfaceArea=500, startDepth=715, depth=585, colour="d6ab20"),
    "porphyry": dict(type="Porphyry_01", id_base=155, surfaceArea=500, startDepth=727, depth=571, colour="FFD26B"),
    "petzite": dict(type="Petzite_01", id_base=160, surfaceArea=500, startDepth=730, depth=545, colour="d6ab20"),
    "pyrite": dict(type="Pyrite_01", id_base=165, surfaceArea=894, startDepth=645, depth=894, colour="d6ab20"),
    # T4 (U / Pt) — IDs 170-199
    "carnotite": dict(type="Carnotite_01", id_base=170, surfaceArea=415, startDepth=800, depth=670, colour="2d9929"),
    "autunite": dict(type="Autunite_01", id_base=175, surfaceArea=375, startDepth=850, depth=700, colour="2d9929"),
    "uraniaurite": dict(type="Uraniaurite_01", id_base=180, surfaceArea=420, startDepth=880, depth=550, colour="2d9929"),
    "niggliite": dict(type="Niggliite_01", id_base=185, surfaceArea=600, startDepth=823, depth=846, colour="fcfa6c"),
    "cooperite": dict(type="Cooperite_01", id_base=190, surfaceArea=675, startDepth=800, depth=688, colour="fcfa6c"),
    "sperrylite": dict(type="Sperrylite_01", id_base=195, surfaceArea=685, startDepth=864, depth=846, colour="fcfa6c"),
}

# V3 is the baseline.
VARIANT_MULTIPLIERS = [0.5, 0.75, 1.0, 1.25, 1.5]

PLANETS = {
    "EarthLike": dict(seed=1, surfaceHintColour=144, variants=[1, 2, 3]),
    "Moon": dict(seed=2, surfaceHintColour=176, variants=[2, 3, 4]),
    "Mars": dict(seed=3, variants=[2, 3, 4, 5]),
    "Europa": dict(seed=4, variants=[2, 3, 4]),
    # V5 of deep T4 ores clips Alien voxel volume. See doc/pog.md.
    "Alien": dict(seed=5, surfaceHintColour=160, variants=[3, 4]),
    "Titan": dict(seed=6, variants=[2, 3, 4, 5]),
    "Triton": dict(seed=8, surfaceHintColour=144, variants=[4, 5]),
    "Pertam": dict(seed=6, surfaceHintColour=144, variants=[1, 2, 3, 4]),
}

# Min reliable per-ore p; smaller values split into per-variant slices POG can roll to 0.
TRACE = 1.5

PLANET_ORES = {
    "EarthLike": {
        "kamacite": 50,
        "glaucodot": 50,
        "hapkeite": 50,
        "sinoite": 5,
        "taenite": 5,
        "iron": 5,
        "cattierite": 5,
        "cohenite": 5,
        "akimotoite": TRACE,
        "wadsleyite": TRACE,
    },
    "Moon": {
        "quartz": 50,
        "heazlewoodite": 50,
        "galena": 5,
        "pyrite": 5,
        "porphyry": 5,
        "petzite": TRACE,
        "electrum": TRACE,
        "deuterium": TRACE,
        "caixirite": TRACE,
    },
    "Mars": {
        "quartz": 10,
        "hapkeite": 10,
        "taenite": 10,
        "iron": TRACE,
        "niggliite": 10,
        "cooperite": 10,
        "sperrylite": 10,
        "akimotoite": TRACE,
        "kamacite": TRACE,
        "glaucodot": TRACE,
    },
    "Europa": {
        "hapkeite": 50,
        "taenite": 50,
        "galena": 50,
        "chlorargyrite": 5,
        "porphyry": 5,
        "petzite": TRACE,
        "electrum": TRACE,
        "deuterium": TRACE,
        "caixirite": TRACE,
    },
    "Alien": {
        "heazlewoodite": TRACE,
        "hapkeite": TRACE,
        "taenite": TRACE,
        "iron": TRACE,
        "carnotite": 10,
        "autunite": 10,
        "uraniaurite": 10,
        "deuterium": 10,
        "denseDeuterium": 10,
        "caixirite": 10,
        "wadsleyite": TRACE,
        "kamacite": TRACE,
        "glaucodot": TRACE,
    },
    "Titan": {
        "pyrite": 50,
        "quartz": 50,
        "taenite": 50,
        "hapkeite": 5,
        "electrum": 5,
        "porphyry": 5,
        "petzite": 5,
        "deuterium": TRACE,
        "caixirite": TRACE,
    },
    "Triton": {
        "iron": 10,
        "heazlewoodite": 10,
        "wadsleyite": 50,
        "dolomite": 15,
        "olivine": 15,
        "akimotoite": 15,
        "kamacite": TRACE,
        "glaucodot": TRACE,
    },
    "Pertam": {
        "kamacite": 30,
        "glaucodot": 30,
        "hapkeite": 30,
        "sinoite": 5,
        "taenite": 10,
        "iron": 15,
        "cattierite": 5,
        "cohenite": 5,
        "akimotoite": 5,
        "wadsleyite": 5,
        "quartz": 40,
        "heazlewoodite": 35,
        "galena": 5,
        "pyrite": 5,
        "petzite": TRACE,
        "electrum": TRACE,
        "deuterium": TRACE,
        "caixirite": TRACE,
    },
}

# Shallow-bias split: take first N, normalize to planet budget.
VARIANT_WEIGHTS = [5, 4, 3, 2, 1]


def round_int(x: float) -> int:
    # POG fields are int (Java parser).
    return int(round(x))


def round_p(x: float) -> float | int:
    # Collapse to int when exact, else keep 2 decimals.
    r = round(x, 2)
    return int(r) if r == int(r) else r


def build_ore_templates() -> list[dict]:
    templates = []
    for ore in BASE_ORES.values():
        for i, mult in enumerate(VARIANT_MULTIPLIERS):
            entry = {
                "id": ore["id_base"] + i,
                "type": ore["type"],
                "surfaceArea": round_int(ore["surfaceArea"] * mult),
                "startDepth": round_int(ore["startDepth"] * mult),
                "depth": round_int(ore["depth"] * mult),
            }
            if "colour" in ore:
                entry["testColourHex"] = ore["colour"]
            templates.append(entry)
    return templates


def build_planet_ores(planet_name: str) -> list[dict]:
    planet = PLANETS[planet_name]
    chosen_variants = planet["variants"]  # 1-indexed
    weights = VARIANT_WEIGHTS[: len(chosen_variants)]
    weight_sum = sum(weights)

    entries = []
    for ore_name, budget in PLANET_ORES[planet_name].items():
        ore = BASE_ORES[ore_name]
        for variant_idx, w in zip(chosen_variants, weights):
            p = budget * w / weight_sum
            entries.append(
                {
                    "id": ore["id_base"] + (variant_idx - 1),
                    "p": round_p(p),
                }
            )
    return entries


def build_config() -> dict:
    config = {
        "planetDataPath": "${SE_DATA}/PlanetDataFiles",
        "planetGeneratorDefinitionsPathArray": ["${SE_DATA}/PlanetGeneratorDefinitions.sbc"],
        "makeColouredMaps": True,
        "surfaceHintMaps": True,
        "shape": 1,
        "density": 0.7,
        "oreTemplates": build_ore_templates(),
        "planets": [],
    }
    for name, p in PLANETS.items():
        entry = {"name": name, "seed": p["seed"]}
        if "surfaceHintColour" in p:
            entry["surfaceHintColour"] = p["surfaceHintColour"]
        entry["ores"] = build_planet_ores(name)
        config["planets"].append(entry)
    return config


def main():
    config = build_config()
    out = Path("pog-config.json.template")
    out.write_text(json.dumps(config, indent=2) + "\n")
    n_templates = len(config["oreTemplates"])
    n_planet_entries = sum(len(p["ores"]) for p in config["planets"])
    print(f"Wrote {out} ({n_templates} ore templates, {n_planet_entries} per-planet entries)")


if __name__ == "__main__":
    main()

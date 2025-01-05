#!/usr/bin/env python

import json
from enum import IntEnum
from typing import TypedDict

BASE_CONFIG = {
    "planetDataPath": "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SpaceEngineers\\Content\\Data\\PlanetDataFiles",  # noqa: E501
    "planetGeneratorDefinitionsPathArray": [
        "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SpaceEngineers\\Content\\Data\\PlanetGeneratorDefinitions.sbc",  # noqa: E501
        "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SpaceEngineers\\Content\\Data\\Pertam.sbc",  # noqa: E501
        "C:\\Program Files (x86)\\Steam\\steamapps\\common\\SpaceEngineers\\Content\\Data\\Triton.sbc",  # noqa: E501
    ],
    "makeColouredMaps": True,
    "surfaceHintMaps": True,
    "shape": 1,
    "density": 0.7,
}


class OreTier(IntEnum):
    STARTER = 1
    MIDGAME = 2
    LATEGAME = 3
    ADVANCED = 4


class Ingot(TypedDict):
    name: str
    tier: OreTier


class Ore(TypedDict):
    name: str
    contents: list[Ingot]


class OreGroup(TypedDict):
    name: str
    ores: list[Ore]


def genPlanetConfig(name: str, seed: int, ore_config: str): ...


def getOreTemplate(name: str, tier: int, shallow: bool = False):
    return {
        "id": 241,
        "type": "DenseDeuterium",
        "surfaceArea": 657,
        "startDepth": 645,
        "depth": 894,
        "testColourHex": "d812ea",
    }


def renderTemplates(): ...


config = json.dumps(BASE_CONFIG)

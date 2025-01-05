#!/usr/bin/env python

import json

CONFIG = {
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


# {
#     "id": 1,
#     "type": "Iron_02",
#     "surfaceArea": 270,
#     "startDepth": 450,
#     "depth": 270,
#     "testColourHex": "fc0707"
# },

ORES = {"Iron_02": {}}

PLANETS = {}


def genPlanetConfig(name: str, ores: str): ...


config = json.dumps(CONFIG)

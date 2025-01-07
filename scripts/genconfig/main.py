import json
import random

import toml
from deepmerge import always_merger

VANILLA_PLANETS = {
    "planetDataPath": r"C:\Program Files (x86)\Steam\steamapps\common\SpaceEngineers\Content\Data\PlanetDataFiles",
    "planetGeneratorDefinitionsPathArray": [
        r"C:\Program Files (x86)\Steam\steamapps\common\SpaceEngineers\Content\Data\PlanetGeneratorDefinitions.sbc",
        r"C:\Program Files (x86)\Steam\steamapps\common\SpaceEngineers\Content\Data\Pertam.sbc",
        r"C:\Program Files (x86)\Steam\steamapps\common\SpaceEngineers\Content\Data\Triton.sbc",
    ],
}


profile = toml.load("ore_profiles/deepscarcity.toml")

config = {}

config = always_merger.merge(config, profile.get("Static", {}))

if profile.get("Global", {}).get("use_vanilla_planets", False):
    config = always_merger.merge(config, VANILLA_PLANETS)

planet_defaults = profile.get("Global", {}).get("Planet", {})

config_ore_templates = []
ore_index = 1

if planets := profile.get("Planets"):
    for planet in planets:
        # Generate the ore templates
        # Append any new templates to the config
        config["planets"].append({})


print(json.dumps(config))

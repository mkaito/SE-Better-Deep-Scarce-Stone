#!/usr/bin/env python

import json

import toml

profile = toml.load("ore_profiles/deepscarcity.toml")

# FIXME: Implement config generator

print(json.dumps(profile))

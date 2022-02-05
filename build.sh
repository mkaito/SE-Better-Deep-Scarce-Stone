#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# WSL2 Paths
GAMEDATA='/mnt/c/Program Files (x86)/Steam/steamapps/common/SpaceEngineers/Content/Data'

# Linux Paths
# GAMEDATA="$HOME/.steam/steam/steamapps/common/SpaceEngineers/Content/Data"

# Generate ore maps
# NOTE: Does not run on Linux
pushd Procedural_Ore_Generator
  java.exe -Xms2G -Xmx16G -jar Procedural_Ore_Generator.jar
popd

# Reset output folder
rm -rf ./Upload
mkdir -p ./Upload/Data

# Base game data files
echo '** Copying vanilla planet data files'
rsync -rt \
      --exclude='*Tutorial/' \
      --exclude='SystemTestMap/' \
      "$GAMEDATA/PlanetDataFiles" ./Upload/Data/

# Ore Generator Output
echo '** Merging ore generator output'
rsync -rt --exclude='*_coloured.png' \
  Procedural_Ore_Generator/PlanetDataFiles ./Upload/Data/
cp Procedural_Ore_Generator/*.sbc ./Upload/Data

# Manual overrides
echo '** Merging manual overrides'
rsync -rtL ./Assets/ ./Upload/
rsync -rtL ./Data/ ./Upload/

echo '** Done'

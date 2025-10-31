#!/usr/bin/bash
set -euo pipefail
IFS=$'\n\t'

# Linux Paths
GAMEDATA="/mnt/steamone/SteamLibrary/steamapps/common/SpaceEngineers/Content/Data"

# Generate ore maps
pushd Procedural_Ore_Generator
  bash run.sh
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

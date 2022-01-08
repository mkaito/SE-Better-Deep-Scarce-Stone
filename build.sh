#!/usr/bin/bash
set -x
set -euo pipefail
IFS=$'\n\t'

# WSL2 Paths
GAMEDATA='/mnt/c/Program Files (x86)/Steam/steamapps/common/SpaceEngineers/Content/Data'
GAMEMODS='/mnt/c/Users/chris/AppData/Roaming/SpaceEngineers/Mods'

# Generate ore maps
# NOTE: Runs the windows version of java because reasons
pushd Procedural_Ore_Generator
  java.exe -Xms512M -Xmx8G -jar Procedural_Ore_Generator.jar
popd

# Reset output folder
rm -rf ./Upload
mkdir -p ./Upload/Data

# Base game data files
rsync -av \
	--filter='- **/*Tutorial/' \
	--filter='- **/SystemTestMap/' \
	"$GAMEDATA/PlanetDataFiles" ./Upload/Data/

# POG Output
rsync -av \
	--filter='- **/*_coloured.png' \
	Procedural_Ore_Generator/PlanetDataFiles ./Upload/Data/

cp -v Procedural_Ore_Generator/PlanetGeneratorDefinitions.sbc ./Upload/Data
cp -v Procedural_Ore_Generator/Triton.sbc ./Upload/Data
cp -v Procedural_Ore_Generator/Pertam.sbc ./Upload/Data

# Manual overrides
rsync -aL ./Output/ ./Upload/

# Install mod locally
rsync -avL --delete ./Upload/ "$GAMEMODS/UDSEBetterDeepScarceStone/"

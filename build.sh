#!/usr/bin/bash
set -x
set -euo pipefail
IFS=$'\n\t'

# WSL2 Paths
GAMEDATA='$HOME/.steam/steam/steamapps/common/SpaceEngineers/Content/Data'
GAMEMODS='$HOME/.steam/steam/steamapps/compatdata/244850/pfx/drive_c/users/steamuser/AppData/Roaming/SpaceEngineers/Mods'

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

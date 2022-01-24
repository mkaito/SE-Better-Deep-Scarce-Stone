#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

rm -f mod.vdf
cat << EOF > mod.vdf
"workshopitem"
{
  "appid"             "244850"
  "publishedfileid"   "2724252237"
  "contentfolder"     "$PWD/Upload"
}
EOF

"$(command -v steamcmd)" +login mkaito "$(gopass show games/steam)" +workshop_build_item "$(readlink -f ./mod.vdf)" +quit

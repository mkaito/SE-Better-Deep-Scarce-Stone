#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

rm -f mod.vdf
rm -f description.bb

pandoc -f markdown -t ./vendor/2bbcode/bbcode_steam.lua <readme.md >|description.bb

description_size=$(wc -c < description.bb)
if [[ $description_size -gt 7999 ]]; then
  echo "Description size too big: $description_size. Limit 8000."
  exit 1
fi

cat << EOF > mod.vdf
"workshopitem"
{
  "appid"             "244850"
  "publishedfileid"   "2724252237"
  "contentfolder"     "$PWD/Upload"
  "description"       "$(cat $PWD/description.bb)"
}
EOF

"$(command -v steamcmd)" +login mkaito "$STEAMPASSWORD" +workshop_build_item "$(readlink -f ./mod.vdf)" +quit

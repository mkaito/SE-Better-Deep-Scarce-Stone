#!/usr/bin/env bash
set -euo pipefail
IFS=$'\n\t'

"$(command -v steamcmd)" +login mkaito "$(gopass show games/steam)" +workshop_build_item "$(readlink -f ./mod.vdf)" +quit

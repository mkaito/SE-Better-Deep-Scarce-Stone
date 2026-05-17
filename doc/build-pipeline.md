# Build, Test, Publish Pipeline

## Tooling

- [mise](https://mise.jdx.dev) drives tasks. `mise.toml` declares tools
  (`pandoc`, `python` 3.12) + env defaults.
- Java + steamcmd from system packages (Gentoo: `dev-java/openjdk`,
  `games-server/steamcmd`).
- Tasks under `.mise/tasks/`. Shebang determines interpreter. mise reads
  `#MISE description=` from any comment line.

## Tasks

```sh
mise run genconfig   # rebuild pog-config.json.template from Python source of truth
mise run oregen      # regenerate ore maps with POG (depends on genconfig)
mise run build       # stage Upload/ for Steam Workshop (call after oregen)
mise run publish     # bbcode-ify readme, build mod.vdf, ship via steamcmd (depends on build)
```

Dependency chain on fresh publish: `genconfig → oregen → build → publish`.
`oregen` is **not** a dependency of `build` or `publish` — ore-map
regeneration is a deliberate step.

Retune flow:

1. Edit `.mise/tasks/genconfig`.
2. `mise run oregen`.
3. Inspect `vendor/POG/PlanetDataFiles/<planet>/*_coloured.png` + BBCode
   table tail of `vendor/POG/generator.log`.
4. `mise run build` to stage `Upload/`.
5. In-game test (local mod dir is symlink to `Upload/`).
6. `mise run publish` when satisfied.

## Environment variables

In `mise.toml` `[env]`. Override per-machine via `mise.local.toml`
(gitignored).

- `SE_DATA` — path to local SE install `Content/Data/`. Required by
  `oregen` (POG reads vanilla planet data) and `build` (rsyncs vanilla
  `PlanetDataFiles` + case-fixed sky textures into `Upload/`).
- `STEAMCMD` — path to `steamcmd.sh`. Required by `publish`.
- `STEAMPASSWORD` — must be exported in shell before `publish`. Not
  stored in repo or mise config.

## What `build` does

1. `rm -rf ./Upload && mkdir -p ./Upload/Data`.
2. rsync vanilla `$SE_DATA/PlanetDataFiles/*` → `Upload/Data/` (exclude
   `*Tutorial/`, `SystemTestMap/`).
3. rsync POG `vendor/POG/PlanetDataFiles/*` → `Upload/Data/` (exclude
   `*_coloured.png`).
4. cp POG `vendor/POG/*.sbc` → `Upload/Data/`.
5. rsync `Assets/` → `Upload/` root (modinfo, metadata, preview).
6. rsync `Data/` → `Upload/Data/` (hand-authored SBC overrides).
7. Copy case-fixed sky textures (see below).

## SE Linux quirks worked around in `build`

### Sky texture case-sensitivity

Vanilla SBCs reference `Sky/AlienSky.dds`. SE constructs lookup paths by
appending `_cm.dds` and `_alphamask.dds`. Vanilla has
`AlienSky_cm.dds` (lowercase cm) but `AlienSky_Alphamask.dds` (capital
A). Linux is case-sensitive, lookup fails.

Mod-folder texture lookup precedes game-folder lookup. `build` copies
referenced sky textures from local SE install into
`Upload/Textures/Models/Environment/Sky/` with lowercase suffix names.

Repo never contains these (copyrighted vanilla assets). Sourced fresh
from local SE install at each build, included in Workshop upload.

Stems derived from `<Texture>` refs in staged
`PlanetGeneratorDefinitions.sbc`. Typically 16 files (~85MB): 8 sky
stems × 2 suffixes.

Some `_cm.dds` (Landsky_texture, TritonAurora) also fail game-folder
lookup. Mod-folder copies work around Pulsar/SE path quirk.

### Vanilla generic asteroid ores

Vanilla SE defines `Nickel_01`, `Cobalt_01`, `Magnesium_01`, `Silicon_01`,
`Silver_01`, `Gold_01`, `Platinum_01`, `Uraninite_01` with
`SpawnsInAsteroids=true` implicit. Not overridden by BS.

`Data/Mod-VoxelMaterials_asteroids.sbc` contains minimal overrides for
these 8 subtypes with `SpawnsInAsteroids=false`. Texture refs preserved
for non-asteroid renders.

### Deuterium voxel material

BDSS used to redefine `Deuterium` voxel material to override
`AsteroidGeneratorSpawnProbabilityMultiplier` from LTP's 5 to 1.
Override referenced LTP textures BDSS doesn't ship → MOD_ERROR.

Redefinition removed. LTP owns the voxel material. Without LTP, BDSS
Deuterium ore tiles render as stone (POG places tiles for SubtypeId
`Deuterium`, no voxel def = fallback).

## `publish` flow

1. `sed '/^## Development$/,$d' readme.md` — strip Development section.
2. Pipe through pandoc with Steam BBCode lua filter
   (`vendor/2bbcode/bbcode_steam.lua`).
3. Size-check `description.bb`. Steam Workshop cap: 8000 bytes.
4. Template `mod.vdf` with `appid=244850`,
   `publishedfileid=2724252237`, `contentfolder=$PWD/Upload`, bbcode
   description inlined.
5. `$STEAMCMD +login mkaito $STEAMPASSWORD +workshop_build_item ... +quit`.

## Generated files (gitignored)

- `pog-config.json.template` — genconfig output
- `vendor/POG/config.json` — envsubst-rendered POG input
- `vendor/POG/PlanetDataFiles/` — POG output
- `vendor/POG/PlanetGeneratorDefinitions.sbc` — POG output
- `vendor/POG/generator.log` — POG runtime log
- `Upload/` — staged mod
- `description.bb` — pandoc output
- `mod.vdf` — steamcmd input
- `mise.local.toml` — per-machine overrides

## Versions / dependencies

- **POG**: 2021-era build vendored in `vendor/POG/` (jar + libs). Bump
  manual.
- **Better Stone**: tested v7.1.0. Refining ratios in
  [better-stone-ores.md](better-stone-ores.md) reflect that. Re-parse on
  major bump.
- **Life'Tech-Powers**: workshop id 2558149005. Optional. BDSS
  references `Deuterium` and `DenseDeuterium` voxel subtypes.
- **Python**: 3.12 via mise. Generator uses stdlib only (`json`,
  `pathlib`). No `requirements.txt`.

## Local dev symlink

```
~/.config/SpaceEngineers/Mods/BetterDeepScarceStone → ./Upload
```

After `mise run build`, mod is live for any SE world with BDSS in mod
list.

## Smoke test

1. New creative world. Mods: BDSS + Better Stone + (optional)
   Life'Tech-Powers. BDSS above Better Stone in load order.
2. Spawn on target planet.
3. Creative ore detector (or long-range detector mod) to verify deposits
   appear at configured depths.
4. Drill, verify ore subtype matches config.

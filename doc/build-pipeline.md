# Build, Test, Publish Pipeline

## Setup

```sh
mise install        # tools
mise run setup      # git hooks
```

System: java + steamcmd via portage (Gentoo: `dev-java/openjdk`,
`games-server/steamcmd`).

## Tasks

```sh
mise run genconfig   # pog-config.json.template from genconfig.py
mise run oregen      # ore maps via POG (chains genconfig)
mise run build       # stage Upload/
mise run publish     # pandoc readme → bbcode, push via steamcmd (chains build)
mise run format      # ruff + prettier + xmllint
```

`build` does **not** chain `oregen` — ore-map regen is deliberate.

Retune: edit `genconfig.py` → `oregen` → inspect coloured maps +
`doc/ore-deposit-counts.md` → `build` → in-game test (local mod dir
symlinks `Upload/`) → `publish`.

## Environment

`mise.toml` `[env]`, override per-machine in `mise.local.toml`.

- `SE_DATA` — local SE `Content/Data/`. Used by `oregen` + `build`.
- `STEAMCMD` — `steamcmd.sh` path. Used by `publish`.
- `STEAMPASSWORD` — exported in shell before `publish`. Never in repo.

## `build` steps

1. Wipe + recreate `Upload/Data/`.
2. rsync vanilla `$SE_DATA/PlanetDataFiles/*` (drop tutorial maps).
3. rsync POG output (drop `*_coloured.png`) + POG `.sbc`.
4. rsync `Assets/` → `Upload/`, `Data/` → `Upload/Data/`.
5. Copy case-fixed sky textures (see below).

## SE Linux quirks

**Sky texture case.** SE appends `_cm.dds` / `_alphamask.dds` to
`<Texture>` refs. Vanilla ships `AlienSky_cm.dds` lowercase but
`AlienSky_Alphamask.dds` capitalized → Linux case-sensitive lookup
fails. `build` copies referenced textures from local SE install into
the mod folder with lowercase suffixes (mod folder overrides game).
Sources are copyrighted vanilla; never in repo. Some `_cm.dds`
(Landsky_texture, TritonAurora) also need the workaround.

**Vanilla generic asteroid ores.** `Nickel_01`/`Cobalt_01`/`Magnesium_01`/
`Silicon_01`/`Silver_01`/`Gold_01`/`Platinum_01`/`Uraninite_01` default
to `SpawnsInAsteroids=true`, BS doesn't override. BDSS sets them to
`false` in `Data/Mod-VoxelMaterials_asteroids.sbc`.

**Deuterium voxel.** BDSS used to override LTP's `Deuterium` to drop
spawn multiplier 5→1, but the override referenced LTP textures we don't
ship → MOD_ERROR. Removed; LTP owns the voxel. Without LTP, POG-placed
Deuterium tiles fall back to stone.

## `publish` steps

1. pandoc `readme.md` through `vendor/2bbcode/bbcode_steam.lua` →
   `description.bb`.
2. Size-check (Workshop cap 8000 bytes).
3. Template `mod.vdf` (appid 244850, publishedfileid 2724252237).
4. `steamcmd +workshop_build_item …`.

## Generated (gitignored)

- `pog-config.json.template`, `vendor/POG/{config.json,PlanetDataFiles/,PlanetGeneratorDefinitions.sbc,generator.log}`
- `Upload/`, `description.bb`, `mod.vdf`, `mise.local.toml`

## Versions

- **POG** 2021 vendored, manual bump.
- **Better Stone** tested v7.1.0 — re-parse refining table on major bump.
- **Life'Tech-Powers** (2558149005) — optional. References `Deuterium`,
  `DenseDeuterium`.
- **Outer Planets Consolidation** (3719884258) — optional. References
  `Caixirite_Raw`.
- **Python** 3.12, stdlib only.

## Local dev symlink

```
~/.config/SpaceEngineers/Mods/BetterDeepScarceStone → ./Upload
```

## Smoke test

New creative world: BDSS + BS + optional LTP/OPC, BDSS above BS in load
order. Spawn target planet, detector for depths, drill to verify subtype.

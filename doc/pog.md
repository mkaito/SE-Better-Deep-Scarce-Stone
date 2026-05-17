# Procedural Ore Generator (POG)

[POG](https://github.com/asrbic/Procedural_Ore_Generator). Java tool. Paints
ore tiles into vanilla SE planet maps. Vendored at `vendor/POG/`. Invoked
via `mise run oregen`. See [build-pipeline.md](build-pipeline.md).

## How POG fits in

1. Reads vanilla `PlanetDataFiles/<planet>/*.png` cube-face material maps.
2. Paints ore tiles into blue channel. Each tile value (1–254) corresponds
   to an `<Ore>` entry in `<OreMappings>` of `PlanetGeneratorDefinitions.sbc`.
3. Writes modified PNGs to `vendor/POG/PlanetDataFiles/` and regenerated
   `vendor/POG/PlanetGeneratorDefinitions.sbc`.
4. `build` task rsyncs vanilla first, overlays POG output, merges
   `Data/` overrides.

## ID space

8-bit blue channel. Max usable: 200 (upper range reserved by SE for biome
modifiers etc.).

Allocation (5 variants per base ore):

| Range | Tier | Base ores |
| --- | --- | --- |
| 1–30 | T1 | Iron_02, Heazlewoodite, Taenite, Hapkeite, Sinoite, Quartz |
| 40–49 | 2H / 2H+ | Deuterium, DenseDeuterium |
| 100–149 | T2 | Akimotoite, Wadsleyite, Olivine, Dolomite, Cattierite, Cohenite, Kamacite, Glaucodot, Galena, Chlorargyrite |
| 150–169 | T3 (Au) | Electrum, Porphyry, Petzite, Pyrite |
| 170–199 | T4 (U/Pt) | Carnotite, Autunite, Uraniaurite, Niggliite, Cooperite, Sperrylite |

5 consecutive IDs per ore. Iron_02 = 1–5, Heazlewoodite = 6–10, etc. 140
used IDs, 200 cap.

## Variant system

Each base ore expanded into 5 variants:

| Variant | startDepth × | depth × | surfaceArea × |
| --- | --- | --- | --- |
| V1 | 0.5 | 0.5 | 0.5 |
| V2 | 0.75 | 0.75 | 0.75 |
| V3 | 1.0 (baseline) | 1.0 | 1.0 |
| V4 | 1.25 | 1.25 | 1.25 |
| V5 | 1.5 | 1.5 | 1.5 |

Each planet picks variant subset. See [ore-design.md](ore-design.md). Subset
shifts within-planet deposit profile, ore palette unchanged.

### p budget per planet

Per-ore `p` budget splits across chosen variants using weights `5:4:3:2:1`
(truncated to N), shallowest variant gets largest slice.

EarthLike Iron p=5, variants V1/V2/V3, weights 5/4/3 (sum 12):

- V1: 5/12 × 5 ≈ 2.08
- V2: 4/12 × 5 ≈ 1.67
- V3: 3/12 × 5 = 1.25

## Generator script

`.mise/tasks/genconfig` — Python source of truth, also a mise task (mise
picks up shebang). Editing JSON output (`pog-config.json.template`) is
overwritten on next run.

Knobs:

- `BASE_ORES` — baseline `(surfaceArea, startDepth, depth)` per ore type
- `VARIANT_MULTIPLIERS` — 5 spread factors
- `PLANETS` — per-planet variant subset + seed
- `PLANET_ORES` — per-planet ore presence + p budget
- `VARIANT_WEIGHTS` — shallow-bias ratio for splitting p

After edit: `mise run oregen` regenerates template, fills `${SE_DATA}`,
runs POG.

## Quirks

### Determinism

POG is deterministic given identical input. Per-planet `seed` controls
placement. Current seeds: 1, 2, 3, 4, 5, 6, 8 for named planets, 6 reused
for Pertam. Changing a seed reshuffles positions, tile counts unchanged.

### maxOreTiles / maxOrePatches

POG defaults: `maxOreTiles=100000`, `maxOrePatches=1000` per planet.

All BDSS planets except Pertam hit the 100k cap. Pertam tops around 71k
(more ores in palette, denser distribution doesn't crowd as tight).

Cap distributes by p weight. Rare ores (Uraniaurite p=0.5 against ~172.5
total weight on Alien) sometimes get 0 tiles via statistical edge cases.
To force spawn: raise base `p` or bump `maxOrePatches`.

### Variant depths can exceed planet voxel space

POG drops patches silently if vertical extent doesn't fit voxel volume.
T4 V4/V5 variants likely exceed limits on most planets (Uraniaurite V5
bottom = 2145m, DenseDeuterium V5 bottom = 2550m). Other variants of same
ore spawn normally.

For reliable T4 ore presence: lean on V3/V4, treat V5 as bonus.

### Interactive exit prompt

POG's `Main` calls `Scanner.nextLine()` for "press ENTER". oregen task
feeds empty stdin (`<<<""`) so it exits cleanly under mise.

### Coloured maps

`makeColouredMaps: true` (default) produces `<face>_coloured.png` for
visualization. `build` rsync excludes `*_coloured.png` from Upload to
keep Workshop upload smaller.

## Surface hints

`surfaceHintMaps: true` (default) generates surface hints (small coloured
tiles above ore patches). Hint colour per-planet via `surfaceHintColour`.

Hints reliably visible only for ores within ~50m of surface. Deeper ores
need ore detector mod.

## Unused POG fields

- `centreOreTile` — places a specific ore variant as patch centre. Used
  for "shallow hint tile above deep patch" pattern.
- `planetFaces` — biases ore spawn to specific cube faces. Could
  restrict e.g. uranium to one side of Alien.

Neither wired into `.mise/tasks/genconfig`.

## Verifying POG output

`mise run oregen` prints BBCode table at end with per-planet per-ore tile
counts. Also in `vendor/POG/generator.log`.

```sh
sed -n '/\[table\]/,/\[\/table\]/p' vendor/POG/generator.log
```

Visual maps: `vendor/POG/PlanetDataFiles/<planet>/*_coloured.png`.

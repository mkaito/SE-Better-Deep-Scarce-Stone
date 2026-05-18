# Procedural Ore Generator (POG)

[POG](https://github.com/asrbic/Procedural_Ore_Generator), vendored at
`vendor/POG/`, invoked via `mise run oregen`.

Reads vanilla cube-face PNGs, paints ore tiles into the blue channel
(1–254 → `<OreMappings>` entries in `PlanetGeneratorDefinitions.sbc`),
writes both to `vendor/POG/`. `build` overlays output on vanilla.

## ID space

8-bit blue channel, 200 usable (rest reserved for biome modifiers). 5
variants per ore, 145 used.

| Range   | Tier      | Base ores                                                                                                   |
| ------- | --------- | ----------------------------------------------------------------------------------------------------------- |
| 1–30    | T1        | Iron_02, Heazlewoodite, Taenite, Hapkeite, Sinoite, Quartz                                                  |
| 40–49   | 2H / 2H+  | Deuterium, DenseDeuterium                                                                                   |
| 50–54   | Cxr       | Caixirite                                                                                                   |
| 100–149 | T2        | Akimotoite, Wadsleyite, Olivine, Dolomite, Cattierite, Cohenite, Kamacite, Glaucodot, Galena, Chlorargyrite |
| 150–169 | T3        | Electrum, Porphyry, Petzite, Pyrite                                                                         |
| 170–199 | T4 (U/Pt) | Carnotite, Autunite, Uraniaurite, Niggliite, Cooperite, Sperrylite                                          |

## Variants

| Variant | × baseline |
| ------- | ---------- |
| V1      | 0.5        |
| V2      | 0.75       |
| V3      | 1.0        |
| V4      | 1.25       |
| V5      | 1.5        |

Per-planet variant subset in [ore-design.md](ore-design.md).

Per-ore `p` splits across the subset by `5:4:3:2:1` (truncated to N),
shallowest gets the largest slice.

Example — EarthLike Iron p=5 over V1/V2/V3 (weights 5/4/3, sum 12):

- V1: 5/12 × 5 ≈ 2.08
- V2: 4/12 × 5 ≈ 1.67
- V3: 3/12 × 5 = 1.25

## Generator

`.mise/tasks/genconfig.py`. Knobs: `BASE_ORES`, `VARIANT_MULTIPLIERS`,
`VARIANT_WEIGHTS`, `PLANETS`, `PLANET_ORES`. Edit, then
`mise run oregen`.

## Quirks

**Deterministic.** Per-planet `seed` controls placement.

**Tile cap.** `maxOreTiles=100000`, `maxOrePatches=1000` per planet.
All BDSS planets hit cap except Pertam (~71k, denser palette).

**Noise floor.** Per-variant slices below ~0.25 can roll 0 tiles. Use
`TRACE = 1.5` minimum for "rare but present".

**V5 voxel clip.** POG drops patches silently if vertical extent
exceeds planet voxel volume. Deep T4 V5 bottoms reach 2145–3300m → too
deep for most planets. Alien caps at V4; other planets accept the
silent loss. When extending: if `startDepth + depth > 1300`, consider
capping variants at V4.

**ENTER prompt.** POG's `Main` blocks on stdin; `oregen` feeds empty
input.

**Coloured maps.** `makeColouredMaps: true` writes `<face>_coloured.png`
for visualization. `build` excludes them.

**Surface hints.** `surfaceHintMaps: true` paints hint tiles above
patches, coloured per `surfaceHintColour`. Visible only ~50m down;
deeper ores need a detector mod.

## Unused POG fields

- `centreOreTile` — specific variant as patch centre (shallow hint
  above deep patch pattern)
- `planetFaces` — biases spawn to cube faces (e.g. U on one side of
  Alien)

## Verifying output

`mise run oregen` auto-writes
[`ore-deposit-counts.md`](ore-deposit-counts.md). Visual:
`vendor/POG/PlanetDataFiles/<planet>/*_coloured.png`.

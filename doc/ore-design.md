# Ore Distribution Design

## Inspiration

Modelled on [Scarce
Resources](https://steamcommunity.com/sharedfiles/filedetails/?id=831739660)
by Chrido / Darian Stephens. Scarce headline rule: spread ore across
planets, force inter-planet travel. Progression: orbit (Ag medbays) → moon
(Au jump drive) → Mars (Pt) → Alien (U).

BDSS additions:

1. Better Stone ore subtypes. Refine to mineral *blends* not single
   ingots. Names encode composition (Hapkeite = Fe+Si, Kamacite = Fe+Ni+Co,
   Carnotite = U+Ice). See [better-stone-ores.md](better-stone-ores.md).
2. Deuterium / Dense Deuterium from [Life'Tech-Powers
   (Multilingual)](https://steamcommunity.com/sharedfiles/filedetails/?id=2558149005)
   as Alien-only endgame energy. Without LTP, Deuterium voxels fall back
   to stone.

## Tier system

| Tier | Minerals | Gameplay role |
| --- | --- | --- |
| T1 | Fe, Ni, Si | Surface-up basics. All planets. |
| T2 | Co, Mg, Ag | Combat (Mg = ammo/explosives), medical (Ag), conveyor + advanced (Co) |
| T3 | Au | Jump drives, gravity gen |
| T4 | U, Pt, 2H, 2H+ | Endgame power + late tech |

### Max-tier rule

Ore tier = highest tier of any mineral it yields.

| Ore | Yields | Tier |
| --- | --- | --- |
| Heazlewoodite | Ni + Ice | T1 |
| Taenite | Fe + Ni | T1 |
| Kamacite | Fe + Ni + Co | T2 |
| Glaucodot | Fe + Co | T2 |
| Pyrite | Fe + Au | T3 |
| Carnotite | U + Ice | T4 |
| Cooperite | Ni + Pt | T4 |

Ore tier determines depth band. Generator (`.mise/tasks/genconfig`) does
not enforce the rule. Baselines are hand-set to respect it. When adding a
new ore: classify by max-tier first, pick baseline depth from tier band.

## Depth bands

Variant spread is ±50% around baseline. See [pog.md](pog.md).

| Tier | startDepth range |
| --- | --- |
| T1 | 25–105m |
| T2 | 60–300m |
| T3 | 320–700m+ |
| T4 (Pt/U) | 400–900m+ |
| T4 (2H) | 400–1200m |
| T4+ (2H+) | 500–1500m |

1200m-range detector covers T1, T2, T3, and shallow T4. Deep T4 needs
fancier detector mod or exploratory drilling.

## Per-planet character

Each planet picks a variant subset (see [pog.md](pog.md)). Subset shifts
deposit feel; ore palette unchanged.

| Planet | Variants | Character |
| --- | --- | --- |
| EarthLike | V1, V2, V3 | Starter |
| Pertam | V1, V2, V3, V4 | Mixed starter (no moon) |
| Moon | V2, V3, V4 | Mid-game |
| Europa | V2, V3, V4 | Mid-game (Ag-focused) |
| Mars | V2, V3, V4, V5 | Mid-late (Pt) |
| Titan | V2, V3, V4, V5 | Mid-late (Au) |
| Alien | V3, V4, V5 | Endgame (U + 2H) |
| Triton | V4, V5 | Expert (no Co source) |

Within a planet's subset, per-ore `p` budget splits across variants using
ratios `5:4:3:2:1` (truncated to N), shallowest gets largest slice.

## Per-planet ore palette

Source of truth: `PLANET_ORES` dict in `.mise/tasks/genconfig`.

### EarthLike

T1 abundant: Kamacite (Fe+Ni+Co) p=50, Glaucodot (Fe+Co) p=50, Hapkeite
(Fe+Si) p=50. Secondary p=5: Iron_02, Taenite, Sinoite, Cattierite,
Cohenite. Trace Mg p=0.5: Akimotoite, Wadsleyite.

Co supplied by bridge ores. No precious metals, no uranium.

### Pertam

T1 mix mirrors EarthLike, p rebalanced (15–40 vs 50). T2 Mg at p=5
(higher than EarthLike — no moon to head to). Rare T3: Pyrite p=5, Galena
p=5, Petzite + Electrum p=0.5.

### Moon

Si: Quartz p=50. Ni: Heazlewoodite p=50. Ag: Galena p=5. Au: Pyrite p=5
(Fe+Au), Porphyry p=5 (pure Au), trace Petzite/Electrum p=0.5. Fe via
Pyrite only.

### Europa

Fe: Hapkeite p=50. Ni: Taenite p=50. Si: Hapkeite. Ag: Galena p=50,
Chlorargyrite p=5. Au: Porphyry p=5, trace Petzite/Electrum.

### Mars

T1: Quartz p=50, Hapkeite p=50, Taenite p=50, Iron_02 p=5. Pt: Niggliite
p=5, Cooperite p=5, Sperrylite p=5. Trace Akimotoite/Kamacite/Glaucodot
p=0.5.

### Alien

T1: Heazlewoodite p=50, Hapkeite p=50, Taenite p=50, Iron_02 p=5. U:
Carnotite p=5, Autunite p=5, Uraniaurite p=0.5. 2H: Deuterium p=5,
DenseDeuterium p=0.5. Trace Wadsleyite/Kamacite/Glaucodot p=0.5.

Carnotite yields more Ice than Uranium per tile.

### Titan

Pyrite p=50, Quartz p=50, Taenite p=50, Hapkeite p=5. Au: Porphyry p=5,
Electrum p=5, Petzite p=5.

### Triton

Iron_02 p=50, Wadsleyite p=50 (Si+Mg), Heazlewoodite p=50. Mg sources
p=5: Dolomite (pure Mg), Olivine, Akimotoite. Trace Kamacite/Glaucodot
p=0.5. No primary Co source.

## Magnesium availability

Mg = combat resource (ammo + explosives). Scarce on starters, abundant on
Triton.

| Planet | Deep Mg | Boulder Mg |
| --- | --- | --- |
| EarthLike | Trace (p=0.5 Akimotoite, Wadsleyite) | Yes (uniform 10%) |
| Pertam | p=5 Akimotoite, Wadsleyite | No boulders |
| Triton | p=50 Wadsleyite + p=5 Dolomite/Olivine/Akimotoite | No boulders |
| Alien | Trace (p=0.5 Wadsleyite) | Yes (10%) |
| Mars, Moon, Europa, Titan | None | Yes (10%) |

Mg yield per tile is 0.003–0.008 across all sources (BS spreadsheet).
Triton stacking required for usable amounts.

## Boulders

`Data/VoxelMaterialChanges.sbc`. Per boulder-bearing biome, Iron surface
boulder outcomes:

- 15% Iron unchanged
- 15% Heazlewoodite (Ni + Ice)
- 15% Taenite (Fe + Ni)
- 15% Hapkeite (Fe + Si)
- 15% Sinoite (Si + Ice)
- 15% Quartz (Si + Ice)
- 10% Dolomite (Mg)

`grass01` biome: 20% Iron → Ice (early-game water).

Triton and Pertam have no boulders at SE planet-def level. No entries
needed in VoxelMaterialChanges for those two.

## Asteroids

`Data/Mod-VoxelMaterials_asteroids.sbc`. BS named ores spawn; vanilla
generic ores (Nickel_01, Cobalt_01, Magnesium_01, Silicon_01, Silver_01,
Gold_01, Platinum_01, Uraninite_01) overridden to `SpawnsInAsteroids=false`.

Dense Deuterium absent from asteroids — Alien-exclusive.

BS ore asteroid spawn multipliers:

| Group | Multiplier | Ores |
| --- | --- | --- |
| Common basics | ×100 | Iron_01, Hapkeite, Heazlewoodite, Sinoite, Quartz, Taenite |
| Fe variant | ×50 | Iron_02 |
| Bridge | ×30 | Kamacite |
| Mid (T2) | ×10 | Dolomite, Cattierite, Cohenite, Akimotoite, Wadsleyite, Olivine, Glaucodot |
| Silver | ×20 | Galena, Chlorargyrite |
| Rare (T3/T4) | ×1 | Au/Pt/U ores; Pyrite; Deuterium |

Iron_01 = "icy iron" per BS (Iron + Ice). ×100 multiplier implements
"asteroids favor icy iron".

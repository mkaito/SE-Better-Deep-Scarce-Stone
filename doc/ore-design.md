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
   as endgame energy. Large deposits on Alien; trace deposits on
   Moon/Europa/Titan. Dense Deuterium stays Alien-exclusive. Without LTP,
   Deuterium voxels fall back to stone.
3. Caixirite from [Outer Planets Consolidation
   (OPC)](https://steamcommunity.com/sharedfiles/filedetails/?id=3719884258)
   as alternate endgame fuel. OPC ships the voxel material with no spawn
   rules and an extreme `MinedOreRatio=0.01` (vs LTP Deuterium=3, BS
   ores=0.5); BDSS places it in deep Alien deposits sized to compensate
   for the low ratio, plus trace deposits on Moon/Europa/Titan. Without
   OPC, Caixirite voxels fall back to stone.

## Tier system

| Tier | Minerals | Gameplay role |
| --- | --- | --- |
| T1 | Fe, Ni, Si | Surface-up basics. All planets. |
| T2 | Co, Mg, Ag | Combat (Mg = ammo/explosives), medical (Ag), conveyor + advanced (Co) |
| T3 | Au | Jump drives, gravity gen |
| T4 | U, Pt, 2H, 2H+, Cxr | Endgame power + late tech |

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
| Caixirite | Cxr | T4 |

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
| T4 (Cxr) | 450–1350m |

1200m-range detector covers T1, T2, T3, and shallow T4. Deep T4 needs
fancier detector mod or exploratory drilling.

## Per-planet character & role

Each planet picks a variant subset (see [pog.md](pog.md)). Subset shifts
deposit feel; ore palette is the per-planet entry in `PLANET_ORES`.

| Planet | Variants | Role | Character |
| --- | --- | --- | --- |
| EarthLike | V1, V2, V3 | Starter | T1+T2 abundant, bootstrap viable |
| Pertam | V1, V2, V3, V4 | Starter (mixed, no moon) | T1+T2 + Au/Ag trace + endgame trace |
| Moon | V2, V3, V4 | Transition (mid) | Si/Ni + Au/Ag, trace endgame |
| Europa | V2, V3, V4 | Transition (mid) | Fe/Ni + Ag, trace endgame |
| Titan | V2, V3, V4, V5 | Transition (mid-late) | Si + Au, trace endgame |
| Mars | V2, V3, V4, V5 | Endgame (Pt) | Pt primary, T1 reduced |
| Alien | V3, V4 | Endgame (U + 2H + Cxr) | All endgame ores at peer abundance; T1 trace only |
| Triton | V4, V5 | Expert (Mg, no Co) | Mg primary, T1 reduced, deep |

Within a planet's subset, per-ore `p` budget splits across variants using
ratios `5:4:3:2:1` (truncated to N), shallowest gets largest slice.

## Per-planet ore palette

Source of truth: `PLANET_ORES` dict in `.mise/tasks/genconfig`.

### EarthLike

T1 abundant: Kamacite (Fe+Ni+Co) p=50, Glaucodot (Fe+Co) p=50, Hapkeite
(Fe+Si) p=50. Secondary p=5: Iron_02, Taenite, Sinoite, Cattierite,
Cohenite. Trace Mg via Akimotoite, Wadsleyite (TRACE).

Co supplied by bridge ores. No precious metals, no uranium.

### Pertam

T1 mix mirrors EarthLike, p rebalanced (15–40 vs 50). T2 Mg at p=5
(higher than EarthLike — no moon to head to). Rare T3: Pyrite p=5, Galena
p=5, Petzite + Electrum TRACE. Trace endgame: Deuterium + Caixirite
TRACE (small finds; Pertam plays as a no-moon starter, so endgame trace
mirrors the moons).

### Moon

Si: Quartz p=50. Ni: Heazlewoodite p=50. Ag: Galena p=5. Au: Pyrite p=5
(Fe+Au), Porphyry p=5 (pure Au), trace Petzite/Electrum TRACE. Fe via
Pyrite only. Trace endgame: Deuterium TRACE, Caixirite TRACE (small
moon deposits; main source is Alien).

### Europa

Fe: Hapkeite p=50. Ni: Taenite p=50. Si: Hapkeite. Ag: Galena p=50,
Chlorargyrite p=5. Au: Porphyry p=5, trace Petzite/Electrum TRACE. Trace
endgame: Deuterium TRACE, Caixirite TRACE.

### Mars

T1 support tier: Quartz p=10, Hapkeite p=10, Taenite p=10, Iron_02 TRACE.
Pt primary: Niggliite p=10, Cooperite p=10, Sperrylite p=10. Trace
Akimotoite/Kamacite/Glaucodot TRACE.

### Alien

T1 all TRACE. U primary: Carnotite/Autunite/Uraniaurite p=10. 2H:
Deuterium/DenseDeuterium p=10. Cxr: Caixirite p=10 (OPC). Trace
Wadsleyite/Kamacite/Glaucodot TRACE.

Sole source for Uraniaurite, DenseDeuterium, Caixirite — sole-source
principle pushes them to peer with the basic U/2H sources. All endgame
ores at p=10 (double the mid-tier peer p=5) so the trip pays off.

Carnotite yields more Ice than Uranium per tile. Caixirite ratio is
0.01, so per-deposit yield is trace despite oversized deposit footprint.

### Titan

Pyrite p=50, Quartz p=50, Taenite p=50, Hapkeite p=5. Au: Porphyry p=5,
Electrum p=5, Petzite p=5. Trace endgame: Deuterium TRACE, Caixirite
TRACE.

### Triton

Iron_02 p=10, Heazlewoodite p=10 (T1 support tier). Wadsleyite p=50
(Si+Mg, Mg primary). Dolomite p=15 (pure Mg), Olivine p=15, Akimotoite
p=15. Trace Kamacite/Glaucodot TRACE. No primary Co source.

## Magnesium availability

Mg = combat resource (ammo + explosives). Scarce on starters, abundant on
Triton.

| Planet | Deep Mg | Boulder Mg |
| --- | --- | --- |
| EarthLike | Trace (TRACE Akimotoite, Wadsleyite) | Yes (uniform 10%) |
| Pertam | p=5 Akimotoite, Wadsleyite | No boulders |
| Triton | p=50 Wadsleyite + p=15 Dolomite/Olivine/Akimotoite | No boulders |
| Alien | Trace (TRACE Wadsleyite) | Yes (10%) |
| Mars | Trace (TRACE Akimotoite) | Yes (10%) |
| Moon, Europa, Titan | None | Yes (10%) |

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

Dense Deuterium absent from asteroids — Alien-exclusive. Caixirite voxel
deferred to OPC (BDSS does not redefine); asteroid behaviour governed by
whatever OPC ships (currently no explicit spawn fields).

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

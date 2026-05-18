# Ore Distribution Design

## Inspiration

[Scarce Resources](https://steamcommunity.com/sharedfiles/filedetails/?id=831739660)
by Chrido / Darian Stephens. Spread ore across planets, force travel.
Progression: orbit (Ag) → moon (Au) → Mars (Pt) → Alien (U).

BDSS adds:

1. Better Stone subtypes — refine to mineral _blends_, names encode
   composition. See [better-stone-ores.md](better-stone-ores.md).
2. Deuterium / Dense Deuterium ([Life'Tech-Powers](https://steamcommunity.com/sharedfiles/filedetails/?id=2558149005)),
   primary on Alien, trace on moons. Fall back to stone without LTP.
3. Caixirite ([OPC](https://steamcommunity.com/sharedfiles/filedetails/?id=3719884258)),
   primary on Alien, trace on moons. `MinedOreRatio=0.01` →
   oversized deposits. Fall back to stone without OPC.

## Tier system

| Tier | Minerals            | Role                                 |
| ---- | ------------------- | ------------------------------------ |
| T1   | Fe, Ni, Si          | Surface basics, all planets          |
| T2   | Co, Mg, Ag          | Co (advanced), Mg (combat), Ag (med) |
| T3   | Au                  | Jump drives, gravity gen             |
| T4   | U, Pt, 2H, 2H+, Cxr | Endgame power + late tech            |

Ore tier = max tier of any mineral it yields. Examples:

| Ore       | Yields       | Tier |
| --------- | ------------ | ---- |
| Kamacite  | Fe + Ni + Co | T2   |
| Pyrite    | Fe + Au      | T3   |
| Carnotite | U + Ice      | T4   |
| Cooperite | Ni + Pt      | T4   |

Tier determines depth band. Generator does not enforce; baselines are
hand-set. New ore → classify by max-tier, pick baseline from band.

## Depth bands

Variant spread ±50% around baseline.

| Tier      | startDepth |
| --------- | ---------- |
| T1        | 25–105m    |
| T2        | 60–300m    |
| T3        | 320–700m+  |
| T4 (Pt/U) | 400–900m+  |
| T4 (2H)   | 400–1200m  |
| T4+ (2H+) | 500–1500m  |
| T4 (Cxr)  | 450–1350m  |

1200m detector covers T1–T3 + shallow T4. Deep T4 needs a long-range
detector mod.

## Per-planet character

| Planet    | Variants       | Role                  | Character                    |
| --------- | -------------- | --------------------- | ---------------------------- |
| EarthLike | V1, V2, V3     | Starter               | T1+T2 abundant               |
| Pertam    | V1, V2, V3, V4 | Starter (no moon)     | T1+T2 + Au/Ag/endgame trace  |
| Moon      | V2, V3, V4     | Transition            | Si/Ni + Au/Ag, trace endgame |
| Europa    | V2, V3, V4     | Transition            | Fe/Ni + Ag, trace endgame    |
| Titan     | V2, V3, V4, V5 | Transition (mid-late) | Si + Au, trace endgame       |
| Mars      | V2, V3, V4, V5 | Endgame (Pt)          | Pt primary, T1 reduced       |
| Alien     | V3, V4         | Endgame (U/2H/Cxr)    | Endgame primary, T1 trace    |
| Triton    | V4, V5         | Expert (Mg, no Co)    | Mg primary, T1 reduced, deep |

Per-ore `p` splits across variants `5:4:3:2:1` (truncated to N),
shallowest largest. See [pog.md](pog.md).

## Per-planet ore palette

### EarthLike

Headline p=50: Kamacite (Fe+Ni+Co), Glaucodot (Fe+Co), Hapkeite (Fe+Si).
Secondary p=5: Iron_02, Taenite, Sinoite, Cattierite, Cohenite. Mg
trace: Akimotoite, Wadsleyite. No precious metals.

### Pertam

EarthLike palette at p=15–40. Mg p=5 (no moon to head to). T3 p=5
Pyrite + Galena. TRACE Petzite/Electrum + endgame TRACE Deut/Cxr —
no-moon mirror of the moons.

### Moon

p=50 Quartz, Heazlewoodite. p=5 Galena (Ag), Pyrite (Au+Fe), Porphyry
(Au). TRACE Petzite/Electrum/Deut/Cxr. Fe via Pyrite only.

### Europa

p=50 Hapkeite (Fe+Si), Taenite (Fe+Ni), Galena (Ag). p=5 Chlorargyrite,
Porphyry. TRACE Petzite/Electrum/Deut/Cxr.

### Mars

T1 reduced: p=10 Quartz/Hapkeite/Taenite. Iron_02 TRACE. Pt primary
p=10: Niggliite, Cooperite, Sperrylite. TRACE Akimotoite/Kamacite/
Glaucodot.

### Alien

T1 all TRACE. Endgame primary p=10:
Carnotite/Autunite/Uraniaurite/Deuterium/DenseDeuterium/Caixirite.
TRACE Wadsleyite/Kamacite/Glaucodot.

Sole source for Uraniaurite/DenseDeuterium/Caixirite. p=10 = 2× the
peer p=5 of mid-tier ores; the trip pays off. Carnotite yields more
Ice than U. Caixirite ratio 0.01 → trace yield despite oversized
footprint.

### Titan

p=50 Pyrite, Quartz, Taenite. p=5 Hapkeite + Au (Porphyry, Electrum,
Petzite). TRACE Deut/Cxr.

### Triton

p=50 Wadsleyite (Mg primary). p=15 Dolomite, Olivine, Akimotoite (Mg).
p=10 Iron_02, Heazlewoodite (T1 support). TRACE Kamacite/Glaucodot.
No Co.

## Magnesium

Combat resource. Scarce on starters, abundant on Triton.

| Planet              | Deep Mg                            | Boulder Mg |
| ------------------- | ---------------------------------- | ---------- |
| EarthLike           | TRACE Akimotoite, Wadsleyite       | 10%        |
| Pertam              | p=5 Akimotoite, Wadsleyite         | None       |
| Triton              | p=50 Wadsleyite + p=15 Dol/Oli/Aki | None       |
| Alien               | TRACE Wadsleyite                   | 10%        |
| Mars                | TRACE Akimotoite                   | 10%        |
| Moon, Europa, Titan | None                               | 10%        |

Mg yield/tile 0.003–0.008. Triton stacking needed for usable amounts.

## Boulders

`Data/VoxelMaterialChanges.sbc`. Boulder-bearing biomes, Iron surface
outcomes:

- 15% each: Iron, Heazlewoodite, Taenite, Hapkeite, Sinoite, Quartz
- 10% Dolomite (Mg)

`grass01`: 20% Iron → Ice (early-game water).

Triton + Pertam have no boulders at SE planet-def level.

## Asteroids

`Data/Mod-VoxelMaterials_asteroids.sbc`. Vanilla generics
(Nickel_01/Cobalt_01/Magnesium_01/Silicon_01/Silver_01/Gold_01/
Platinum_01/Uraninite_01) set to `SpawnsInAsteroids=false`. DenseDeut
absent (Alien-exclusive). Caixirite deferred to OPC.

BS ore multipliers:

| Group         | Multiplier | Ores                                                       |
| ------------- | ---------- | ---------------------------------------------------------- |
| Common basics | ×100       | Iron_01, Hapkeite, Heazlewoodite, Sinoite, Quartz, Taenite |
| Fe variant    | ×50        | Iron_02                                                    |
| Bridge        | ×30        | Kamacite                                                   |
| Mid (T2)      | ×10        | Dol/Cat/Coh/Aki/Wad/Oli/Glaucodot                          |
| Silver        | ×20        | Galena, Chlorargyrite                                      |
| Rare (T3/T4)  | ×1         | Au/Pt/U ores; Pyrite; Deuterium                            |

Iron_01 = icy iron (Fe+Ice). ×100 implements "asteroids favor icy iron".

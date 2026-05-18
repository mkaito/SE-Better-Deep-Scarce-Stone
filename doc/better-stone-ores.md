# Better Stone Ores — Refining Reference

Source: "Detailed Ore Data.xlsx" by DranKof. Last parsed 2026-05-17
against [Better Stone v7.1.0](https://steamcommunity.com/sharedfiles/filedetails/?id=406244471).

## Naming convention

BS encodes composition in `MinedOre`:

- `[CM] Iron (Fe)` — Common Mineral
- `[S] Hapkeite (Fe,Si)` — Silicon-family
- `[PM] Porphyry (Au)` — Precious Metal
- `[EI] Carnotite (U)` — Exotic / Industrial

Parentheses = refining output. Most BS ores yield multiple minerals.

## Ore → mineral table

| Ore subtype          | Yields                    | Yield ratios (per unit ore)  |
| -------------------- | ------------------------- | ---------------------------- |
| Iron_01 (Icy Iron)   | Iron + Ice                | Iron 0.4, Ice 0.5            |
| Iron_02 (Dense Iron) | Iron                      | Iron 0.9                     |
| Hapkeite             | Iron + Silicon            | Iron 0.35, Si 0.45           |
| Heazlewoodite        | Nickel + Ice              | Ni 0.4, Ice 0.15             |
| Taenite              | Iron + Nickel             | Iron 0.35, Ni 0.2            |
| Cohenite             | Nickel + Cobalt           | Ni 0.21, Co 0.18             |
| Kamacite             | Iron + Nickel + Cobalt    | Iron 0.284, Ni 0.174, Co 0.1 |
| Glaucodot            | Iron + Cobalt             | Iron 0.234, Co 0.4           |
| Cattierite           | Cobalt                    | Co 0.27                      |
| Sinoite              | Silicon + Ice             | Si 0.62, Ice 0.33            |
| Quartz               | Silicon + Ice             | Si 0.49, Ice 1.12            |
| Akimotoite           | Silicon + Magnesium       | Si 0.22, Mg 0.005            |
| Wadsleyite           | Silicon + Magnesium       | Si 0.3, Mg 0.003             |
| Olivine              | Silicon + Magnesium + Ice | Si 0.18, Mg 0.008, Ice 0.35  |
| Dolomite             | Magnesium                 | Mg 0.007                     |
| Galena               | Silver                    | Ag 0.035                     |
| Chlorargyrite        | Silver + Ice              | Ag 0.064, Ice 0.002          |
| Electrum             | Silver + Gold             | Ag 0.045, Au 0.004           |
| Petzite              | Silver + Gold             | Ag 0.045, Au 0.004           |
| Porphyry             | Gold                      | Au 0.006                     |
| Pyrite               | Iron + Gold               | Iron 0.55, Au 0.001          |
| Carnotite            | Uranium + Ice             | U 0.001, Ice 0.572           |
| Autunite             | Uranium                   | U 0.004                      |
| Uraniaurite          | Uranium + Gold            | U 0.003, Au 0.003            |
| Niggliite            | Platinum                  | Pt 0.003                     |
| Sperrylite           | Platinum                  | Pt 0.003                     |
| Cooperite            | Nickel + Platinum         | Ni 0.36, Pt 0.002            |

## Modded ores (not Better Stone)

| Ore subtype    | Provided by      | Yields                | Yield ratios |
| -------------- | ---------------- | --------------------- | ------------ |
| Deuterium      | Life'Tech-Powers | Deuterium (2H)        | 3.0          |
| DenseDeuterium | Life'Tech-Powers | Dense Deuterium (2H+) | unknown      |

LTP owns the voxel + asteroid spawn (multiplier 5).

## Notes

- Mg 0.003–0.008 across all sources.
- Ice-bearing ores ranked: Quartz 1.12, Carnotite 0.572, Olivine 0.35,
  Sinoite 0.33, Heazlewoodite 0.15.
- Cooperite + Uraniaurite are dual-yield T4 — Cooperite is mostly Ni,
  Pt is the rare bit.

## Re-parsing the spreadsheet

Not in repo (copyright). From BS Workshop discussions or the author:

```sh
python3 -c "
import zipfile, xml.etree.ElementTree as ET, re
# extract xl/worksheets/sheet1.xml + xl/sharedStrings.xml from the .xlsx
# walk rows; section headers in col 0, voxel/ore/ingot in cols 1/2/8
"
```

Sections: `VANILLA`, `OVERWRITES / ADJUSTMENTS`, `MODTASTIC` (BS-added).
Re-check ratios on major BS bumps.

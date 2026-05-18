# BDSS Internal Documentation

Dev reference. Player-facing description is `readme.md` at repo root.

| File                                         | Topic                                                       |
| -------------------------------------------- | ----------------------------------------------------------- |
| [ore-design.md](ore-design.md)               | Tier system, per-planet roles, Scarce Resources lineage     |
| [better-stone-ores.md](better-stone-ores.md) | BS ore → mineral refining table (from author's spreadsheet) |
| [pog.md](pog.md)                             | POG quirks: ID space, tile cap, seeds, variant generation   |
| [build-pipeline.md](build-pipeline.md)       | mise tasks, env, Linux workarounds                          |

Source of truth: `.mise/tasks/genconfig.py`. Edit → `mise run oregen`.

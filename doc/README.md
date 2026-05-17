# BDSS Internal Documentation

Technical and design reference. Player-facing description is `readme.md` at repo root.

| File | Topic |
| --- | --- |
| [ore-design.md](ore-design.md) | Design rules, tier system, per-planet character, Scarce Resources reference |
| [better-stone-ores.md](better-stone-ores.md) | Better Stone ore subtypes → mineral output table (from BS author's spreadsheet) |
| [pog.md](pog.md) | Procedural Ore Generator quirks: ID space, max-tile cap, deterministic seeds, variant generation |
| [build-pipeline.md](build-pipeline.md) | mise tasks, env vars, Linux-specific workarounds (sky textures, vanilla ore overrides) |

## Read order when coming back

1. Repo-root `readme.md` — what mod does.
2. [ore-design.md](ore-design.md) — what ore distribution targets.
3. [build-pipeline.md](build-pipeline.md) — how to build, test, publish.
4. [pog.md](pog.md) — for retuning.
5. [better-stone-ores.md](better-stone-ores.md) — for BS ore → mineral lookups.

Single source of truth for ore distribution: `.mise/tasks/genconfig` (Python). Edit, run `mise run oregen`, inspect `vendor/POG/`.

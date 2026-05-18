# Better Deep Scarce Stone

A scarce-and-deep ore rebalance for Space Engineers. Started as an
update to Better [Deep Scarce
Ores](https://steamcommunity.com/sharedfiles/filedetails/?id=2281727435)
(merging EarthLike and Moon into Pertam), then evolved into its own
rebalance once I started playing with the numbers in earnest.

Supports Deuterium (2H) ore from
[Life'Tech-Powers](https://steamcommunity.com/sharedfiles/filedetails/?id=2558149005),
and Caixirite (Cxr) ore from [Outer Planets
Consolidation](https://steamcommunity.com/sharedfiles/filedetails/?id=3719884258).
Without those mods installed, the corresponding ore patches harmlessly
revert to stone.

The basics (Fe, Ni, Si) are close to the surface, so you can get
started with a hand drill and a basic ore detector. Anything past that
goes deep. SE's voxel scanning is subpar enough that you'll only ever
find the deeper ores by accident without a long-range ore detector mod,
so I strongly recommend getting one before going hunting for the good
stuff.

This project is available on
[GitHub](https://github.com/mkaito/SE-Better-Deep-Scarce-Stone).

## Synopsis

EarthLike has Iron, Nickel, Silicon, Cobalt and small quantities of
Magnesium in surface boulders. You'll want to head to the Moon for Gold
and Silver, Mars for Platinum, Alien for Uranium, Deuterium, and
Caixirite. Magnesium is available in varying small quantities
everywhere, and large quantities on Triton.

Pertam has the same as EarthLike, but also small quantities of Silver
and Gold, since it doesn't have a local moon, as well as actual (rare)
Magnesium deposits, since I have yet to see any boulders on Pertam.

Asteroids can spawn everything, although most of the time you will only
run into ores containing iron, nickel, silicon, cobalt, silver, and ice.
But sometimes, you'll get lucky. Space starts are viable, but you'll
probably want to set up planet-side mines to get more reliable
resources.

Technically, I guess you can start on Triton, since it has all the
basics in some quantity, but I wouldn't recommend it.

Processing stone with a survival kit is slow but yields increased ingots
and less gravel. Doing so with a refinery will yield only trace amounts
of ingots, but much more gravel. This is to help those that start with a
vanilla drop pod, push the player towards finding actual ore rather than
relying on stone for anything but getting started, but also to help with
mods that actually use gravel, such as [AQD
Concrete](https://steamcommunity.com/sharedfiles/filedetails/?id=2298956701).

## Installation

Requires [Better
Stone](https://steamcommunity.com/sharedfiles/filedetails/?id=406244471).
Both mods must be added to your world, with **this mod above Better
Stone** in the mod list (or below it, if you use Dedicated Server load
order). SE's dependency system is unreliable enough that declaring
Better Stone as a workshop dependency actually breaks this mod in game,
so it has to be configured manually.

## Conflicts

1.  Mods that modify the ore maps or vanilla planet definitions will
    likely not get along with this mod at all. Whichever is on top in
    the mod list will have their definitions take effect.
2.  Modded planets are an entirely separate affair from this mod. They
    have their own ore maps and planet defs, and whatever is in them is
    what you will see. This mod does not automatically do anything to
    non-vanilla planets.
3.  Modded ores almost certainly ship with planet defs, so see point 1
    about that.
4.  Pretty much any other kind of mod should have zero issues with this,
    but please let me know if you run into issues. Preferrably on
    GitHub, so I can keep track of it.

### Notable Conflicts

- [Bring Back
  Cyberhounds](https://steamcommunity.com/workshop/filedetails/?id=945655546)
  overrides the EarthLike def to adjust the creature spawn radius. Make
  sure the Cyberhounds mod is placed below (above on DS) in the mod
  list.

## Planets and Ores Summary

If I'm on X, what will I find?

- EarthLike: Fe, Fe+, Ni, Si, Co
- Moon: Fe, Ni, Si, Au, Ag, trace 2H/Cxr
- Europa: Fe, Ni, Si, Au, Ag, trace 2H/Cxr
- Mars: Fe, Fe+, Ni, Si, Co, Pt
- Alien: Fe, Fe+, Ni, Si, Mg, Au, U, 2H, 2H+, Cxr
- Titan: Fe, Ni, Si, Au, Ag, trace 2H/Cxr
- Triton: Fe, Fe+, Ni, Co, Mg
- Pertam: Fe, Fe+, Ni, Si, Co, Mg, Au, Ag

If I want X, where is it most plentiful?

- Fe, Fe+: Triton
- Ni: Europa
- Si: EarthLike, Moon
- Co: Pertam, EarthLike
- Mg: Triton
- Ag: Europa
- Au: Titan
- Pt: Mars
- U: Alien
- 2H: Alien
- 2H+: Alien
- Cxr: Alien

## Ore Deposits

One of the main principles behind this mod is that ore deposits should
be quite rich. When you find one, you'll probably want to set up a
permanent mining operation on top of it. To compensate for this bounty,
deposits are less frequent than vanilla, and the higher tiers are much
deeper.

The basics stay shallow so you can get off the ground without much
fuss, but by the time you're after gold, platinum, uranium, deuterium,
or caixirite, you'll be running a proper mining ship, not a hand drill.
Half the fun is figuring out which planet has what — see the summary
above for the rough shape of it.

## Intended Gameplay Scenario

Here are some notes and recommendations for you:

- I recommend a long range ore detector mod. You probably won't find any
  T3 deposits without one. My personal favourites are [Ore Detector
  Reforged](https://steamcommunity.com/sharedfiles/filedetails/?id=2790047923&searchtext=)
  and [Seismic
  Surveying](https://steamcommunity.com/sharedfiles/filedetails/?id=2821219378).
- I would suggest you spawn with something mobile, like the [New Spawn
  Pods
  mod](https://steamcommunity.com/sharedfiles/filedetails/?id=2471313282).
- If you don't start yourself with a large grid ship or rover, I would
  suggest [Wasteland
  Encounters](https://steamcommunity.com/sharedfiles/filedetails/?id=2539299261),
  and your first step being finding a large wreck to get you started.

## Appreciation & Hugs

- Lemmiwinks for creating the [Procedural Ore
  Generator](https://github.com/asrbic/Procedural_Ore_Generator), which
  is how I created the ore maps.
- Chrido and Darian Stephens for creating [Scarce
  Resources](https://steamcommunity.com/sharedfiles/filedetails/?id=831739660),
  and introducing me to the idea that having everything within 300m of
  literally anywhere is boring.
- DranKof for [Better
  Stone](https://steamcommunity.com/sharedfiles/filedetails/?id=406244471),
  and introducing me to the idea that more ores are more fun.
- Ghost722nd for [Deep
  Ores](https://steamcommunity.com/sharedfiles/filedetails/?id=1540170706),
  and introducing me to actual large mining operations, rather than just
  a small mining ship.
- Cak for the original [Better Deep Scarce
  Ores](https://steamcommunity.com/sharedfiles/filedetails/?id=2281727435),
  which served as a foundation and motivation for creating this mod.
- Kuvat for his work on the
  [Life'Tech](https://steamcommunity.com/sharedfiles/filedetails/?id=2558149005)
  mods.

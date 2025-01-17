# Better Deep Scarce Stone

This mod began life as an effort to update Better [Deep Scarce
Ores](https://steamcommunity.com/sharedfiles/filedetails/?id=2281727435),
whose author appears to be on a bit of a break. I took his ore values
and just merged EarthLike and Moon into Pertam, called it a day. After
playing with the resulting mod, I began to feel the need to adjust the
numbers a bit, to better suit my usual scenario. The result is this mod.
I hope you'll find it enjoyable.

Supports Deuterium (2H) ore from
[Life'Tech-Powers](https://steamcommunity.com/sharedfiles/filedetails/?id=2558149005).
If you don't use the mod, that's fine. Any Deuterium patches will just
turn back into stone.

I began the project with ore depths up to 1200m, but very quickly found
myself wrestling with the limitations of SE's subpar voxel scanning
code. The result was that, no matter the range of your modded ore
detector, you would only find the deeper ores by accident, never on
purpose. I decided to make the ores much more shallow, and hope Keen
will eventually get around to optimizing this much neglected bit of
their game.

This project is available on
[GitHub](https://github.com/mkaito/SE-Better-Deep-Scarce-Stone).

## Synopsis

EarthLike has Iron, Nickel, Silicon, Cobalt and small quantities of
Magnesium in surface boulders. You'll want to head to the Moon for Gold
and Silver, Mars for Platinum, Alien for Uranium and Deuterium.
Magnesium is available in varying small quantities everywhere, and large
quantities on Triton.

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

Since the dependency system in SE is kinda broken, this mod does not
explicitly depend on [Better
Stone](https://steamcommunity.com/sharedfiles/filedetails/?id=406244471).
You do, however, need both installed, added to your world, AND THIS MOD
ABOVE Better Stone (below if DS). Please make sure you get that right.
There's nothing I can do to make any of this automatic, I'm sorry.

In fact, adding it as a dependency on the workshop, breaks it in game.
Thanks, Keen.

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
- Moon, Europa: Fe, Ni, Si, Au, Ag
- Mars: Fe, Fe+, Ni, Si, Co, Pt
- Alien: Fe, Fe+, Ni, Si, Mg, Au, U, 2H
- Titan: Fe, Ni, Si, Au, Ag, Pt
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

## Ore Deposits

One of the main principles behind this mod is that ore deposits should
be quite rich. When you find one, you'll probably want to set up a
permanent mining operation on top of it. To compensate for this bounty,
you'll be searching far longer for them. Deposits are both less
frequent, and much deeper.

- T1 (Fe, Ni, Si) at 50m
- T2 (Co, Mg, Ag) at 150m
- T3 (Au, Pt, U, 2H) at 300m
- T4 (2H+) at 400m

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

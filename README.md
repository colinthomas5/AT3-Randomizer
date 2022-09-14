# AT3 Randomizer

Item randomizer for Adventure Time: Secret of the Nameless Kingdom.

## Getting Started

In preparation to randomize your AT3 copy, backup your vanilla data folder from your AT3 installation for when you wish to return to a vanilla game state. Alternatively, you may clone your AT3 installation and dedicate one installation to the vanilla game and one installation to randomizer.

## Randomization (Alpha Releases)

To randomize your AT3 copy using one of the alpha releases...

```
• Run at3_random.exe
• Point the program to the data folder you wish to randomize
• Give seed and spoiler log preferences
• The program will randomize the item location data within the data folder
```

# Randomization (Recent Python Script)

To randomize your AT3 copy using the current at3_random.py, launch parameters are required to be set to allow the randomizer script to know the randomization preferences:

```
-f (data folder path) -> Selects the AT3 data folder to be randomized
-s (seed) -> Seed; if not included, chooses a random seed which is provided in the spoiler log
-spl -> Spoiler log (if not included within launch parameters, spoiler log will not be generated)
Item Randomization:
-nir -> No item randomization
-sir -> Standard item randomization
-eir -> Expanded item randomization (replaces randomized keys with key items noramlly not in the randomized item pool)
Item Logic:
-nl -> No logic (not recommended without expanded item randomization as gives higher chance for no logic seed to be beatable)
-sl -> Standard logic (no gauntlets under rocks, no flambo/grabby hands under dead trees)
NPC Randomization:
-nnr -> No NPC randomization
-snr -> Standard NPC randomization
```

## Contact

If you have any feature suggestions or find any bugs, here is where you can find me

```
• Twitter: @chatterteethsrc
• Discord: colin#0615
```

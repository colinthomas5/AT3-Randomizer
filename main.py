import argparse
import constants

from options import parseOptions
from randomizer import randomize

prefs = {}

# List of local item pool
itemLocal = []

# List of local NPC pool
NPCLocal = []

# List of item pool based on launch parameters
itemList = []

# Choose data folder to randomize, initializes seed and spoiler log
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--folder", help="The AT3 data folder to randomize", type=str, required=True)
parser.add_argument("-s", "--seed", help="The custom seed to randomize with", type=str, required=False)
item_group = parser.add_argument_group("Item randomization")
ir = item_group.add_mutually_exclusive_group(required=True)
ir.add_argument("-nir", "--no-items-randomization", help="Do not randomize items", action="store_true")
ir.add_argument("-sir", "--standard-items-randomization", help="Use standard method of randomizing items", action="store_true")
ir.add_argument("-eir", "--expanded-items-randomization", help="Use expanded method of randomizing items", action="store_true")
ir.add_argument("-cir", "--custom-items-randomization", help="Use custom item pool to randomize items", action="store_true")
item_group.add_argument("-ci", "--custom-items", help="The custom item pool to use (comma terminated)", type=str, required=False)
il = item_group.add_mutually_exclusive_group(required=True)
il.add_argument("-nl", "--no-logic", help="Do not randomize item logic", action="store_true")
il.add_argument("-sl", "--standard-logic", help="Use standard method of randomizing item logic", action="store_true")
npc_group = parser.add_argument_group("NPC randomization")
nr = npc_group.add_mutually_exclusive_group(required=True)
nr.add_argument("-nnr", "--no-npcs-randomization", help="Do not randomize NPCs", action="store_true")
nr.add_argument("-snr", "--standard-npcs-randomization", help="Use standard method of randomizing NPCs", action="store_true")
nr.add_argument("-cnr", "--custom-npcs-randomization", help="Use custom NPC pool to randomize NPCs", action="store_true")
nr.add_argument("-gunt", "--gunter-insanity", help="Turns the NPCs to be randomized into Gunter", action="store_true", required=False)
npc_group.add_argument("-cn", "--custom-npcs", help="The custom NPC pool to use (comma terminated)", type=str, required=False)
parser.add_argument("-spl", "--spoiler-log", help="Output a spoiler log", action="store_true", default=False)
parser.add_argument("-lsp", "--lsp-cave-randomization", help="Randomize the LSP Cave area", action="store_true", default=False)
parser.add_argument("-ntmr", "--nightmare-castle-randomization", help="Randomize the Nightmare Castle area", action="store_true", default=False)
parser.add_argument("-bsmt", "--castle-basement-randomization", help="Randomize the Castle Basement area", action="store_true", default=False)
parser.add_argument("-hl", "--headless", help = "Run the randomizer in headless mode", action="store_true", default=False)

prefs, log, spoilerLog, itemList = parseOptions(parser.parse_args(), constants.defaultItemList, constants.fileList, constants.itemListExpanded)

randomize(prefs["dir"], prefs, sorted(constants.fileList), spoilerLog, itemList, itemLocal, constants.itemListExpanded, constants.NPCList, constants.NPCList2, NPCLocal)

if prefs["headless"] != 1:
    input("Randomization complete! Press enter or exit the window to close.")
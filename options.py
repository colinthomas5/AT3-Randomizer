import os
import random
import sys

def parseOptions(args, defaultItemList, fileList, itemListExpanded):
	prefs = {}
	print("Randomizing " + args.folder + "...")
	prefs["dir"] = args.folder
	if args.seed == "":
		args.seed = random.random()
		prefs["customSeed"] = args.seed
	else:
		prefs["customSeed"] = args.seed
	if args.no_items_randomization == True:
		prefs["itemRandomization"] = 0
	elif args.standard_items_randomization == True:
		prefs["itemRandomization"] = 1
	elif args.expanded_items_randomization == True:
		prefs["itemRandomization"] = 2
	elif args.custom_items_randomization == True:
		prefs["itemRandomization"] = 3
		if args.custom_items == "":
			print("Error: Custom item pool not specified")
			sys.exit(1)
		else:
			itemList = args.custom_items.split(",")
	if args.custom_items == None:
		itemList = defaultItemList
	if args.no_logic == True:
		prefs["itemLogic"] = 0
	if args.standard_logic == True:
		prefs["itemLogic"] = 1
	if args.no_npcs_randomization == True:
		prefs["npcRandomization"] = 0
	if args.standard_npcs_randomization == True:
		prefs["npcRandomization"] = 1
	if args.custom_npcs_randomization == True:
		prefs["npcRandomization"] = 2
		# not implemented yet
	if args.gunter_insanity == True:
		prefs["npcRandomization"] = 3
	if args.spoiler_log == True:
		prefs["spoilerLog"] = 1
		logPath = os.getcwd() + "\\spoiler.log"
		log = open(logPath, 'w')
		logSeed = "seed: " + prefs["customSeed"] + "\n \n"
		spoilerLog = []
		spoilerLog.append(logSeed)
	else:
		prefs["spoilerLog"] = 0
	if args.lsp_cave_randomization == True:
		prefs["lspCaveRando"] == 1
		fileList.append("\\overworld_lsp_cave.pak")
	if args.nightmare_castle_randomization == True:
		fileList.append("\\castle_nightmare_master.pak")
		itemListExpanded.remove[itemListExpanded.index	("PickupSweater\0\0\0\0\0\0")]
	if args.castle_basement_randomization == True:
		fileList.append("\\castle_basement_master.pak")
	return prefs, log, spoilerLog, itemList
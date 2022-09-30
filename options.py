import os
import random
import sys

def parseOptions(args, defaultItemList, fileList, itemListExpanded):
	prefs = {}
	logSettingsMap = "Extra Maps: "
	logSettingsMapCount = 0
	print("Randomizing " + args.folder + "...")
	prefs["dir"] = args.folder
	if args.seed == "":
		args.seed = random.random()
		prefs["customSeed"] = args.seed
	else:
		prefs["customSeed"] = args.seed
	if args.no_items_randomization == True:
		prefs["itemRandomization"] = 0
		itemRandoText = "None"
	elif args.standard_items_randomization == True:
		prefs["itemRandomization"] = 1
		itemRandoText = "Standard"
	elif args.expanded_items_randomization == True:
		prefs["itemRandomization"] = 2
		itemRandoText = "Expanded"
	elif args.custom_items_randomization == True:
		prefs["itemRandomization"] = 3
		# itemRandoText for custom items to be implemented further
		itemRandoText = "Custom"
		if args.custom_items == "":
			print("Error: Custom item pool not specified")
			sys.exit(1)
		else:
			itemList = args.custom_items.split(",")
	if args.custom_items == None:
		itemList = defaultItemList
	if args.no_logic == True:
		prefs["itemLogic"] = 0
		itemLogicText = "None"
	if args.standard_logic == True:
		prefs["itemLogic"] = 1
		itemLogicText = "Standard"
	if args.no_npcs_randomization == True:
		prefs["npcRandomization"] = 0
		npcRandoText = "None"
	if args.standard_npcs_randomization == True:
		prefs["npcRandomization"] = 1
		npcRandoText = "Standard"
	if args.custom_npcs_randomization == True:
		prefs["npcRandomization"] = 2
		# not implemented yet
	if args.gunter_insanity == True:
		prefs["npcRandomization"] = 3
		npcRandoText = "Guntsanity"
	if args.lsp_cave_randomization == True:
		prefs["lspCaveRando"] = 1
		fileList.append("\\overworld_lsp_cave.pak")
		logSettingsMap += "LSP Cave"
		logSettingsMapCount += 1
	if args.nightmare_castle_randomization == True:
		fileList.append("\\castle_nightmare_master.pak")
		itemListExpanded.remove[itemListExpanded.index("PickupSweater\0\0\0\0\0\0")]
		if logSettingsMapCount > 0:
			logSettingsMap += ", Nightmare Castle"
		else:
			logSettingsMap += "Nightmare Castle"
		logSettingsMapCount += 1
	if args.castle_basement_randomization == True:
		fileList.append("\\castle_basement_master.pak")
		if logSettingsMapCount > 0:
			logSettingsMap += ", Castle Basement"
		else:
			logSettingsMap += "Castle Basement"
		logSettingsMapCount += 1
	if args.spoiler_log == True:
		prefs["spoilerLog"] = 1
		logPath = os.getcwd() + "\\spoiler.log"
		log = open(logPath, 'w')
		logSeed = "Seed: " + prefs["customSeed"] + "\n"
		logSettingsItem = "Item Randomization Mode: " + itemRandoText + "\n"
		logSettingsNPC = "NPC Randomization Mode: " + npcRandoText + "\n"
		if logSettingsMapCount == 0:
			logSettingsMap = "Standard Map Pool \n\n"
		else:
			logSettingsMap += "\n\n"
		spoilerLog = []
		spoilerLog.append(logSeed)
		spoilerLog.append(logSettingsItem)
		if prefs["itemRandomization"] != 0:
			logSettingsItemLogic = "Item Randomization Logic: " + itemLogicText + "\n"
			spoilerLog.append(logSettingsItemLogic)
		spoilerLog.append(logSettingsNPC)
		spoilerLog.append(logSettingsMap)
	else:
		prefs["spoilerLog"] = 0
	return prefs, log, spoilerLog, itemList
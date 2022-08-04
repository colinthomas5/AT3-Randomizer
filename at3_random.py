import promptlib
import random
import os

prompter = promptlib.Files()

# List of files to be randomized within data folder
fileList = ["\\castle_basement_master.pak", "\\castle_nightmare_master.pak", "\\overworld_forest_cave_2.pak", "\\overworld_forest_master.pak", "\\overworld_iceking_cave.pak",
			"\\overworld_kingdom_master.pak", "\\overworld_mountain_cave_3.pak", "\\overworld_mountain_cave_4.pak", "\\overworld_mountain_master.pak", "\\overworld_swamp_master.pak",
			"\\overworld_wasteland_cave_1.pak", "\\temple_dream_master.pak", "\\temple_fear_master.pak", "\\temple_song_master.pak"]

# Files that could be in fileList but are currently excluded
#fileListExtras = ["\\overworld_lsp_cave.pak", "\\global.pak",]

# Used for debugging, lists most files within data folder to scout for files that can be added to pooling and randomizing but aren't due to lack of items found by program
#fileListComplete = ["\\arena_hairapes.pak", "\\autoload.pak", "\\15boss_crabdemon.pak", "\\boss_hairapes.pak", "\\boss_nightmare.pak", "\\boss_shadowfinn.pak", "\\castle_basement_master.pak",
#			"\\castle_nightmare_master.pak", "\\caves.pak", "\\dreamtemple.pak", "\\fearcastle.pak", "\\feartemple.pak", "\\gym_crabdemon.pak", "\\gym_nprincess.pak",
#			"\\gym_quests.pak", "\\gym_shadowfinn.pak", "\\npc_choose_goose.pak", "\\npc_coalman.pak", "\\npc_iceking.pak", "\\npc_magicman.pak", "\\npc_marceline.pak", "\\npc_mr_pig.pak",
#			"\\npc_partypat.pak", "\\npc_potteryshopguy.pak", "\\npc_rattleballs.pak", "\\npc_shelby.pak", "\\npc_starchy.pak", "\\npc_treetrunks.pak", "\\overworld.pak", "\\overworld_forest.pak",
#			"\\overworld_forest_cave.pak", "\\overworld_forest_cave_2.pak", "\\overworld_forest_master.pak", "\\overworld_iceking_cave.pak", "\\overworld_kingdom.pak", "\\overworld_kingdom_cave_01.pak",
#			"\\overworld_kingdom_master.pak", "\\overworld_lsp_cave.pak", "\\overworld_mountain.pak", "\\overworld_mountain_cave_1.pak", "\\overworld_mountain_cave_2.pak", "\\overworld_mountain_cave_3.pak",
#			"\\overworld_mountain_cave_4.pak", "\\overworld_mountain_master.pak", "\\overworld_swamp.pak", "\\overworld_swamp_master.pak", "\\overworld_wasteland_cave_1.pak", "\\songtemple.pak",
#			"\\temple_dream_master.pak", "\\temple_fear_master.pak", "\\temple_song_master.pak", "\\temples.pak"]

# List of items to check randomization; Null char added to each entry to maintain a consistent length of 19
itemList = ["PickupChestItemKey\0", "PickupTreasureHuge\0", "PickupTrailMix\0\0\0\0\0", "PickupSpareThumps\0\0", "PickupTrailMix3\0\0\0\0", "PickupMeat\0\0\0\0\0\0\0\0\0", "PickupHeartPiece\0\0\0", 
			"PickupPencil\0\0\0\0\0\0\0", "PickupSweater\0\0\0\0\0\0", "PickupMapPaper\0\0\0\0\0", "PickupPieFairy\0\0\0\0\0", "PickupChestItemRBK\0", "PickupTreasureSmall", "PickupTreasureBig\0\0", "PickupDemonHeart\0\0\0", "PickupNuts\0\0\0\0\0\0\0\0\0", 
			"PickupFruits\0\0\0\0\0\0\0", "PickupGumGlobe\0\0\0\0\0", "PickupWoodPlank\0\0\0\0", "PickupPlasticBag\0\0\0", "PickupFruitStack\0\0\0", "PickupHeroGauntlet\0", "PickupTrailMix1\0\0\0\0", "PickupTrailMix2\0\0\0\0", "PickupGrabbyHand\0\0\0",
			"PickupFlambo\0\0\0\0\0\0\0", "PickupBananarang\0\0\0"]

# List of items within global_shop.txt in global.pak; currently unsupported due to the forced file size change and Choose Goose not selling you items that he doesn't sell in vanilla
shopList = ["PickupTrailMix1", "PickupTrailMix2", "PickupTrailMix3", "PickupBananarang", "PickupPlasticBag", "PickupHeartPiece", "PickupMeat", "PickupCyclopsTears", "PickupGumGlobe", "PickupDynaMIGHT"]

# Items that could be in itemList but are currently excluded
#itemListExtras = ["PickupHealthOne\0\0\0\0"]

# List of local item pool
itemLocal = []

# Choose data folder to randomize, initializes seed and spoiler log
print("Choose the AT3 data folder that you wish to randomize.")
dir = prompter.dir()
seed = input("Type the seed you wish to use (Leave blank to enter a random seed): ")
customSeed = 2
if seed == "":
	seed = random.random()
	random.seed(seed)
	customSeed = 0
else:
	random.seed(seed, version=1)
	customSeed = 1
spoiler = 2
while spoiler is 2:
	createLog = input("Do you want a spoiler log to be generated? (Y/N): ")
	if createLog == "Y" or createLog == "y":
		logPath = os.getcwd() + "\\spoiler.log"
		log = open(logPath, 'w')
		logSeed = "seed: " + str(seed) + "\n \n"
		spoilerLog = []
		spoilerLog.append(logSeed)
		spoiler = 1
	if createLog == "N" or createLog == "n":
		spoiler = 0



# Builds local item pool while replacing items with placeholder text to be changed into randomized items; placeholder text named to have length of 19
for area in fileList:
	path = dir + area
	print("Now generating pool from: ", path)
	openFile = open(path, "r+", encoding="latin-1", newline='')
	line = openFile.readlines()
	areaClean = area.lstrip("\\").rstrip(".pak") + ": \n"
	c = 0
	lines = []
	if spoiler is 1:
		spoilerLog.append(areaClean)
	for location in line:
		if area == "\\castle_nightmare_master.pak":
			while "PickupSweater\0\0\0\0\0\0" in location:
				itemLocal.append("PickupSweater\0\0\0\0\0\0")
				replacement = line[c].replace("PickupSweater\0\0\0\0\0\0", "placeholdertextomg!", 1)
				line[c] = replacement.lstrip('')
				location = line[c]
				print("Replaced PickupSweater\0\0\0\0\0\0 with placeholder")
				if spoiler is 1:
					spoilerLog.append("PickupSweater\0\0\0\0\0\0 -> ")
#		elif area == "\\global.pak":
#			for item in shopList:
#				while item in location:
#					itemLocal.append(item.ljust(19, "\0"))
#					replacement = line[c].replace(item, "placeholdertextomg!", 1)
#					line[c] = replacement.lstrip('')
#					location = line[c]
#					print("Added ", item, " to item pool")
#					if spoiler is 1:
#						i = item.ljust(19, "\0") + " ->  "
#						spoilerLog.append(i)
		else:
			for item in itemList:
				while item in location:
					itemLocal.append(item.ljust(19))
					replacement = line[c].replace(item, "placeholdertextomg!", 1)
					line[c] = replacement.lstrip('')
					location = line[c]
					print("Added ", item, " to item pool")
					if spoiler is 1:
						i = item + " ->  "
						spoilerLog.append(i)
		lines.append(line[c])
		c += 1
	if spoiler is 1:
		spoilerLog.append( "\n")
	openFile.seek(0)
	openFile.truncate(0)
	for line in lines:
		openFile.write(line)
	openFile.close()
	print("Successfully pooled from ", path)

# Replaces placeholders with actual items from local item pool
for area in fileList:
	path = dir + area
	print("Now randomizing ", path)
	openFile = open(path, "r+", encoding="latin-1", newline='')
	line = openFile.readlines()
	areaClean = area.lstrip("\\").rstrip(".pak") + ": \n"
	flamboTree = "placeholdertextomg!\0\0\0\0\0dry_tree.wf3d"
	heroRock = "global:forest_pickup_heavy_1.wf3d\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0" + bytes.fromhex("01").decode("latin-1") + "\0\0\0placeholdertextomg!"
	c = 0
	s = 0
	lines = []
	for location in line:
		if area == "\\castle_nightmare_master.pak":
			while "placeholdertextomg!" in location:
				length = len(itemLocal)
				randomNumber = random.randint(0, length-1)
				while itemLocal[randomNumber] == "PickupGrabbyHand\0\0\0" or itemLocal[randomNumber] == "PickupHeroGauntlet\0":
					randomNumber = random.randint(0, length-1)
				replacement = line[c].replace("placeholdertextomg!", itemLocal[randomNumber], 1)
				line[c] = replacement.lstrip(' ')
				location = line[c]
				print("Replaced placeholder with ", itemLocal[randomNumber])
				if spoiler is 1:
					for entry in spoilerLog:
						if entry == areaClean:
							s += 1
							logIndex = int(spoilerLog.index(entry) + s)
							logEntry = spoilerLog[logIndex] + itemLocal[randomNumber] + "\n"
							spoilerLog[logIndex] = logEntry
				itemLocal.remove(itemLocal[randomNumber])
#		elif area == "\\global.pak":
#			while "placeholdertextomg!" in location:
#				length = len(itemLocal)
#				randomNumber = random.randint(0, length-1)
#				replacementItem = itemLocal[randomNumber].rstrip("\0")
#				replacement = line[c].replace("placeholdertextomg!", replacementItem, 1)
#				line[c] = replacement.lstrip(' ')
#				location = line[c]
#				print("Replaced placeholder with ", itemLocal[randomNumber])
				if spoiler is 1:
					for entry in spoilerLog:
						if entry == areaClean:
							s += 1
							logIndex = int(spoilerLog.index(entry) + s)
							logEntry = spoilerLog[logIndex] + itemLocal[randomNumber] + "\n"
							spoilerLog[logIndex] = logEntry
				itemLocal.remove(itemLocal[randomNumber])
		else:
			while flamboTree in location:
				length = len(itemLocal)
				randomNumber = random.randint(0, length-1)
				while itemLocal[randomNumber] == "PickupGrabbyHand\0\0\0":
					randomNumber = random.randint(0, length-1)
				replacement = line[c].replace("placeholdertextomg!", itemLocal[randomNumber], 1)
				line[c] = replacement.lstrip(' ')
				location = line[c]
#				print("Replaced placeholder with ", itemLocal[randomNumber])
#				print("Dry tree worky")
				if spoiler is 1:
					for entry in spoilerLog:
						if entry == areaClean:
							s += 1
							logIndex = int(spoilerLog.index(entry) + s)
							logEntry = spoilerLog[logIndex] + itemLocal[randomNumber] + "\n"
							spoilerLog[logIndex] = logEntry
			while heroRock in location:
				length = len(itemLocal)
				randomNumber = random.randint(0, length-1)
				while itemLocal[randomNumber] == "PickupHeroGauntlet\0":
					randomNumber = random.randint(0, length-1)
				replacement = line[c].replace("placeholdertextomg!", itemLocal[randomNumber], 1)
				line[c] = replacement.lstrip(' ')
				location = line[c]
#				print("Replaced placeholder with ", itemLocal[randomNumber])
#				print("Heavy rock worky")
				if spoiler is 1:
					for entry in spoilerLog:
						if entry == areaClean:
							s += 1
							logIndex = int(spoilerLog.index(entry) + s)
							logEntry = spoilerLog[logIndex] + itemLocal[randomNumber] + "\n"
							spoilerLog[logIndex] = logEntry
			while "placeholdertextomg!" in location:
				length = len(itemLocal)
				randomNumber = random.randint(0, length-1)
				replacement = line[c].replace("placeholdertextomg!", itemLocal[randomNumber], 1)
				line[c] = replacement.lstrip(' ')
				location = line[c]
#				print("Replaced placeholder with ", itemLocal[randomNumber])
				if spoiler is 1:
					for entry in spoilerLog:
						if entry == areaClean:
							s += 1
							logIndex = int(spoilerLog.index(entry) + s)
							logEntry = spoilerLog[logIndex] + itemLocal[randomNumber] + "\n"
							spoilerLog[logIndex] = logEntry
				itemLocal.remove(itemLocal[randomNumber])
		lines.append(line[c])
		c += 1
	openFile.seek(0)
	openFile.truncate(0)
	for line in lines:
		openFile.write(line)
	openFile.close()
	print("Successfully randomized ", path)
if customSeed is 0:
	print("Your seed is: ", seed)
if spoiler is 1:
	logPath = os.getcwd() + "\\spoiler.log"
	log = open(logPath, 'w')
	for entry in spoilerLog:
		log.write(str(entry))
	print("Log saved to ", os.getcwd(), "\\spoiler.log")
	log.close()
input("Randomization complete! Press enter or exit the window to close.")


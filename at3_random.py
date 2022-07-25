import promptlib
import random

prompter = promptlib.Files()

# List of files to be randomized within data folder
fileList = ["\\castle_basement_master.pak", "\\castle_nightmare_master.pak", "\\global.pak", "\\overworld_forest_cave_2.pak", "\\overworld_forest_master.pak", "\\overworld_iceking_cave.pak",
			"\\overworld_kingdom_master.pak", "\\overworld_mountain_cave_3.pak", "\\overworld_mountain_cave_4.pak", "\\overworld_mountain_master.pak", "\\overworld_swamp_master.pak",
			"\\overworld_wasteland_cave_1.pak", "\\temple_dream_master.pak", "\\temple_fear_master.pak", "\\temple_song_master.pak"]

# Files that could be in fileList but are currently excluded
#fileList = ["\\overworld_lsp_cave.pak"]

# Used for debugging, lists most files within data folder to scout for files that can be added to pooling and randomizing
#fileList = ["\\arena_hairapes.pak", "\\autoload.pak", "\\boss_crabdemon.pak", "\\boss_hairapes.pak", "\\boss_nightmare.pak", "\\boss_shadowfinn.pak", "\\castle_basement_master.pak",
#			"\\castle_nightmare_master.pak", "\\caves.pak", "\\dreamtemple.pak", "\\fearcastle.pak", "\\feartemple.pak", "\\global.pak", "\\gym_crabdemon.pak", "\\gym_nprincess.pak",
#			"\\gym_quests.pak", "\\gym_shadowfinn.pak", "\\npc_choose_goose.pak", "\\npc_coalman.pak", "\\npc_iceking.pak", "\\npc_magicman.pak", "\\npc_marceline.pak", "\\npc_mr_pig.pak",
#			"\\npc_partypat.pak", "\\npc_potteryshopguy.pak", "\\npc_rattleballs.pak", "\\npc_shelby.pak", "\\npc_starchy.pak", "\\npc_treetrunks.pak", "\\overworld.pak", "\\overworld_forest.pak",
#			"\\overworld_forest_cave.pak", "\\overworld_forest_cave_2.pak", "\\overworld_forest_master.pak", "\\overworld_iceking_cave.pak", "\\overworld_kingdom.pak", "\\overworld_kingdom_cave_01.pak",
#			"\\overworld_kingdom_master.pak", "\\overworld_lsp_cave.pak", "\\overworld_mountain.pak", "\\overworld_mountain_cave_1.pak", "\\overworld_mountain_cave_2.pak", "\\overworld_mountain_cave_3.pak",
#			"\\overworld_mountain_cave_4.pak", "\\overworld_mountain_master.pak", "\\overworld_swamp.pak", "\\overworld_swamp_master.pak", "\\overworld_wasteland_cave_1.pak", "\\songtemple.pak",
#			"\\temple_dream_master.pak", "\\temple_fear_master.pak", "\\temple_song_master.pak", "\\temples.pak"]


# List of items in item pool [DEPRICATED, NOW BUILDS ITEM POOL WITH itemLocal]
#itemPool = ["PickupChestItemKey", "PickupTreasureHuge", "PickupHealthOne", "PickupHealthOne", "PickupTrailMix", "PickupTreasureHuge", "PickupTreasureHuge", "PickupTreasureHuge", "PickupSpareThumps", 
#			"PickupTreasureHuge", "PickupTrailMix3", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemKey", "PickupMeat", "PickupHeartPiece", 
#			"PickupPencil", "PickupSweater", "PickupMapPaper", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemKey", "PickupPieFairy", "PickupChestItemRBK", "PickupPieFairy", 
#			"PickupHealthOne", "PickupTreasureSmall", "PickupTreasureSmall", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupTreasureSmall", "PickupHealthOne", 
#			"PickupHealthOne", "PickupHealthOne", "PickupTreasureBig", "PickupDemonHeart", "PickupNuts", "PickupFruits", "PickupHealthOne", "PickupTreasureBig", "PickupHealthOne", "PickupHealthOne", 
#			"PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", 
#			"PickupHealthOne", "PickupHealthOne", "PickupFruits", "PickupNuts", "PickupDemonHeart", "PickupTreasureBig", "PickupNuts", "PickupFruits", "PickupHealthOne", "PickupNuts", "PickupTreasureBig", 
#			"PickupFruits", "PickupGumGlobe", "PickupGumGlobe", "PickupGumGlobe", "PickupGumGlobe", "PickupGumGlobe", "PickupWoodPlank", "PickupHeartPiece", "PickupHeartPiece", "PickupGumGlobe", "PickupGumGlobe", 
#			"PickupGumGlobe", "PickupHeartPiece", "PickupPlasticBag", "PickupWoodPlank", "PickupGumGlobe", "PickupGumGlobe", "PickupPieFairy", "PickupGumGlobe", "PickupGumGlobe", "PickupGumGlobe", "PickupGumGlobe", 
#			"PickupGumGlobe", "PickupGumGlobe", "PickupWoodPlank", "PickupHeartPiece", "PickupGumGlobe", "PickupPieFairy", "PickupWoodPlank", "PickupGumGlobe", "PickupGumGlobe", "PickupGumGlobe", "PickupTreasureHuge", 
#			"PickupGumGlobe", "PickupWoodPlank","PickupGumGlobe ", "PickupPencil", "PickupMapPaper", "PickupTreasureHuge", "PickupChestItemKey", "PickupChestItemKey", "PickupSpareThumps", "PickupTreasureHuge", "PickupFruitStack", 
#			"PickupTreaureHuge", "PickupHeroGauntlet", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemKey", "PickupChestItemRBK", "PickupChestItemKey", "PickupGumGlobe", "PickupPieFairy", 
#			"PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", 
#			"PickupHealthOne", "PickupTrailMix1", "PickupHealthOne", "PickupHealthOne", "PickupChestItemKey", "PickupTreasureHuge", "PickupChestItemKey", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", 
#			"PickupHealthOne", "PickupHealthOne", "PickupDemonHeart", "PickupNuts", "PickupFruits", "PickupTreasureBig", "PickupMapPaper", "PickupChestItemRBK", "PickupPencil", "PickupChestItemKey", "PickupGumGlobe", 
#			"PickupSpareThumps", "PickupFruitStack", "PickupPieFairy", "PickupTrailMix2", "PickupHealthOne", "PickupPieFairy", "PickupFruitStack", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", 
#			"PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", 
#			"PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupHealthOne", "PickupTrailMix3", "PickupChestItemKey", "PickupChestItemKey", "PickupMapPaper", "PickupChestItemRBK", "PickupChestItemKey", 
#			"PickupPencil", "PickupGrabbyHand", "PickupGumGlobe", "PickupTreasureHuge", "PickupTreasureHuge", "PickupChestItemKey", "PickupTreasureSmall", "PickupPieFairy"]


# List of items to check randomization; Null char added to each entry to maintain a consistent length of 19
itemList = ["PickupChestItemKey\0", "PickupTreasureHuge\0", "PickupTrailMix\0\0\0\0\0", "PickupSpareThumps\0\0", "PickupTrailMix3\0\0\0\0", "PickupMeat\0\0\0\0\0\0\0\0\0", "PickupHeartPiece\0\0\0", 
			"PickupPencil\0\0\0\0\0\0\0", "PickupSweater\0\0\0\0\0\0", "PickupMapPaper\0\0\0\0\0", "PickupPieFairy\0\0\0\0\0", "PickupChestItemRBK\0", "PickupTreasureSmall", "PickupTreasureBig\0\0", "PickupDemonHeart\0\0\0", "PickupNuts\0\0\0\0\0\0\0\0\0", 
			"PickupFruits\0\0\0\0\0\0\0", "PickupGumGlobe\0\0\0\0\0", "PickupWoodPlank\0\0\0\0", "PickupPlasticBag\0\0\0", "PickupFruitStack\0\0\0", "PickupHeroGauntlet\0", "PickupTrailMix1\0\0\0\0", "PickupTrailMix2\0\0\0\0", "PickupGrabbyHand\0\0\0",
			"PickupFlambo\0\0\0\0\0\0\0", "PickupBananarang\0\0\0"]

# Items that could be in itemList but are currently excluded
#itemListExtras = ["PickupHealthOne\0\0\0\0"]

# List of local item pool
itemLocal = []

# Choose data folder to randomize
print("Choose the AT3 data folder that you wish to randomize.")
dir = prompter.dir()

# Builds local item pool while replacing items with placeholder text to be changed into randomized items; placeholder text named to have length of 19
for area in fileList:
	path = dir + area
	currently = "Now generating pool from: " + path
	print(currently)
	openFile = open(path, "r+", encoding="latin-1", newline='')
	line = openFile.readlines()
	c = 0
	lines = []
	for index in line:
		if area == "\\castle_nightmare_master.pak":
			while "PickupSweater\0\0\0\0\0\0" in index:
				itemLocal.append("PickupSweater\0\0\0\0\0\0")
				replacement = line[c].replace("PickupSweater\0\0\0\0\0\0", "placeholdertextomg!", 1)
				replaced = "Replaced PickupSweater\0\0\0\0\0\0 with placeholder"
				line[c] = replacement.lstrip('')
				index = line[c]
				print(replaced)
		else:
			for item in itemList:
				while item in index:
					itemLocal.append(item.ljust(19))
					replacement = line[c].replace(item, "placeholdertextomg!", 1)
					replaced = "Replaced " + item + " with placeholder"
					line[c] = replacement.lstrip('')
					index = line[c]
					print(replaced)
		lines.append(line[c])
		c += 1
	openFile.seek(0)
	openFile.truncate(0)
	for line in lines:
		openFile.write(line)
	openFile.close()
	success = "Successfully pooled from " + path
	print(success)

# Replaces placeholders with actual items from local item pool
for area in fileList:
	path = dir + area
	currently = "Now randomizing: " + path
	print(currently)
	openFile = open(path, "r+", encoding="latin-1", newline='')
	line = openFile.readlines()
	c = 0
	lines = []
	for index in line:
		if area == "\\castle_nightmare_master.pak":
			while "placeholdertextomg!" in index:
				length = len(itemLocal)
				randomNumber = random.randint(0, length-1)
				while itemLocal[randomNumber] == "PickupGrabbyHand\0\0\0" or itemLocal[randomNumber] == "PickupHeroGauntlet\0":
					randomNumber = random.randint(0, length-1)
				replacement = line[c].replace("placeholdertextomg!", itemLocal[randomNumber], 1)
				replaced = "Replaced placeholder with " + itemLocal[randomNumber]
				line[c] = replacement.lstrip(' ')
				index = line[c]
				itemLocal.remove(itemLocal[randomNumber])
				print(replaced)
		else:
			while "placeholdertextomg!" in index:
				length = len(itemLocal)
				randomNumber = random.randint(0, length-1)
				replacement = line[c].replace("placeholdertextomg!", itemLocal[randomNumber], 1)
				replaced = "Replaced placeholder with " + itemLocal[randomNumber]
				line[c] = replacement.lstrip(' ')
				index = line[c]
				itemLocal.remove(itemLocal[randomNumber])
				print(replaced)
			lines.append(line[c])
		c += 1
	openFile.seek(0)
	openFile.truncate(0)
	for line in lines:
		openFile.write(line)
	openFile.close()
	success = "Successfully randomized " + path
	print(success)
input("Randomization complete! Press any key to close...")


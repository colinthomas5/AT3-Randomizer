import promptlib
import random
import os


#ADDED NPC RANDO, FIXED BUG THAT CAUSED AN ITEM TO DISAPPEAR FROM LOCAL ITEM POOL

prompter = promptlib.Files()

# List of files to be randomized within data folder
fileList = ["\\castle_basement_master.pak", "\\castle_nightmare_master.pak", "\\overworld_forest_cave.pak", "\\overworld_forest_cave_2.pak", "\\overworld_forest_master.pak", "\\overworld_iceking_cave.pak",
			"\\overworld_kingdom_master.pak", "\\overworld_mountain_cave_1.pak", "\\overworld_mountain_cave_3.pak", "\\overworld_mountain_cave_4.pak", "\\overworld_mountain_master.pak", "\\overworld_swamp_master.pak",
			"\\overworld_wasteland_cave_1.pak", "\\temple_dream_master.pak", "\\temple_fear_master.pak", "\\temple_song_master.pak"]

# Files that could be in fileList but are currently excluded
#fileListExtras = ["\\overworld_lsp_cave.pak", "\\global.pak",]

# Used for debugging, lists most files within data folder to scout for files that can be added to pooling and randomizing but aren't due to lack of items or NPCs
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
			"PickupFruits\0\0\0\0\0\0\0", "PickupGumGlobe\0\0\0\0\0", "PickupWoodPlank\0\0\0\0", "PickupPlasticBag\0\0\0", "PickupFruitStack\0\0\0", "PickupHeroGauntlet\0", "PickupTrailMix1\0\0\0\0", "PickupTrailMix2\0\0\0\0", "PickupTrailMix3\0\0\0\0", "PickupTrailMix4\0\0\0\0", "PickupGrabbyHand\0\0\0",]

# Items that could be in itemList but are currently excluded
#itemListExtras = ["PickupHealthOne\0\0\0\0"]

# Items that could be added to the item pool, but are not found within the game via current methods or are only found in the shop, which can't currently be randomized
#itemListSpecial = ["PickupFlambo\0\0\0\0\0\0\0", "PickupBananarang\0\0\0", "PickupLadyRing\0\0\0\0\0", "PickupLoveNote\0\0\0\0\0", "PickupHeatSignature", "PickupMindGames\0\0\0\0", "PickupFanfiction\0\0\0", "PickupEnergyDrink\0\0", "PickupBugMilk\0\0\0\0", "PickupEnchiridion"]

# List of NPCs to check randomization; Null char added to each entry to maintain consistent length of 57
NPCList = ["Gunter\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_gunter.pak\0\0\0\0\0\0\0\0\0\0\0", "PartyPat\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_partypat.pak\0\0\0\0\0\0\0\0\0", "Demon\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_nightospheredemon.pak"
		   "TinyManticore\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_manticore.pak\0\0\0\0\0\0\0\0", "Rattleballs\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_rattleballs.pak\0\0\0\0\0\0", "IceKing\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_iceking.pak\0\0\0\0\0\0\0\0\0\0",
		   "Shelby\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_shelby.pak\0\0\0\0\0\0\0\0\0\0\0", "MrPig\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_mr_pig.pak\0\0\0\0\0\0\0\0\0\0\0", "TreeTrunks\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_treetrunks.pak\0\0\0\0\0\0\0"
		   "MagicMan\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_magicman.pak\0\0\0\0\0\0\0\0\0", "Stanley\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_stanely.pak\0\0\0\0\0\0\0\0\0\0", "Witch\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_witch.pak\0\0\0\0\0\0\0\0\0\0\0\0"
		   "CoalMan\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_coalman.pak\0\0\0\0\0\0\0\0\0\0", "WizardTheif\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_wizardthief.pak\0\0\0\0\0\0"]

# List of certain NPCs in their hex values, due to a bug that has them not be found with the method used in NPCList
NPCList2 = [bytes.fromhex("44656D6F6E0000000000000000000000000000000000000000000000000000006E70635F6E696768746F73706865726564656D6F6E2E70616B").decode("latin-1"), # Nightosphere Demon entry in NPCList
			bytes.fromhex("54696E794D616E7469636F7265000000000000000000000000000000000000006E70635F6D616E7469636F72652E70616B0000000000000000").decode("latin-1"), # Tiny Manticore entry in NPCList
			bytes.fromhex("4D616769634D616E0000000000000000000000000000000000000000000000006E70635F6D616769636D616E2E70616B000000000000000000").decode("latin-1"), # Magic Man entry in NPCList
			bytes.fromhex("547265655472756E6B73000000000000000000000000000000000000000000006E70635F747265657472756E6B732E70616B00000000000000").decode("latin-1"), # Tree Trunks entry in NPCList
			bytes.fromhex("57697A61726454686965660000000000000000000000000000000000000000006E70635F77697A61726474686965662E70616B000000000000").decode("latin-1"), # Wizard Thief entry in NPCList
			bytes.fromhex("436F616C4D616E000000000000000000000000000000000000000000000000006E70635F636F616C6D616E2E70616B00000000000000000000").decode("latin-1")] # Coal Man entry in NPCList

# Files that could be in NPCList but are currently excluded
#NPCListExtras = ["PartyBear1\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_partybear1.pak\0\0\0\0\0\0\0", "PartyBear2\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_partybear2.pak\0\0\0\0\0\0\0", "PartyBear3\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_partybear3.pak\0\0\0\0\0\0\0",
#			"CinnamonBun\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_cinnamonbun.pak\0\0\0\0\0\0", "Keyper\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_keyper.pak\0\0\0\0\0\0\0\0\0\0\0", "Snail\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_snail.pak\0\0\0\0\0\0\0\0\0\0\0\0",
#			"ChooseGoose\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_choose_goose.pak\0\0\0\0\0", "PotShopGuy\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_potteryshopguypak", "PootCloud\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_pootcloud.pak\0\0\0\0\0\0\0\0",]	

# List of items within global_shop.txt in global.pak; currently unsupported due to the forced file size change and Choose Goose not selling you items that he doesn't sell in vanilla
shopList = ["PickupTrailMix1", "PickupTrailMix2", "PickupTrailMix3", "PickupBananarang", "PickupPlasticBag", "PickupHeartPiece", "PickupMeat", "PickupCyclopsTears", "PickupGumGlobe", "PickupDynaMIGHT"]


# List of local item pool
itemLocal = []

# List of local NPC pool
NPCLocal = []

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
npc = 2
while npc is 2:
	randomNPC = input("Do you want to randomize NPC locations? (Y/N): ")
	if randomNPC == "Y" or randomNPC == "y":
		npc = 1
	if randomNPC == "N" or randomNPC == "n":
		npc = 0
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
			if npc is 1:
				for nonplay in NPCList:
					while nonplay in location:
						NPCLocal.append(nonplay)
						replacement = line[c].replace(nonplay, "creatingafiftysevencharacterplaceholderisnotveryfunforme!")
						line[c] = replacement.lstrip('')
						location = line[c]
						print("Added ", nonplay[:19], " to NPC pool")
						if spoiler is 1:
							n = nonplay[:19] + " ->  "
							spoilerLog.append(n)
				for nonplay in NPCList2:
					while nonplay in location:
						NPCLocal.append(nonplay)
						replacement = line[c].replace(nonplay, "creatingafiftysevencharacterplaceholderisnotveryfunforme!")
						line[c] = replacement.lstrip('')
						location = line[c]
						print("Added ", nonplay[:19], " to NPC pool")
						if spoiler is 1:
							n = nonplay[:19] + " ->  "
							spoilerLog.append(n)
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
#				if spoiler is 1:
#					for entry in spoilerLog:
#						if entry == areaClean:
#							s += 1
#							logIndex = int(spoilerLog.index(entry) + s)
#							logEntry = spoilerLog[logIndex] + itemLocal[randomNumber] + "\n"
#							spoilerLog[logIndex] = logEntry
#				itemLocal.remove(itemLocal[randomNumber])
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
			if npc is 1:
					while "creatingafiftysevencharacterplaceholderisnotveryfunforme!" in location:
						length = len(NPCLocal)
						randomNumber = random.randint(0, length-1)
						replacement = line[c].replace("creatingafiftysevencharacterplaceholderisnotveryfunforme!", NPCLocal[randomNumber], 1)
						line[c] = replacement.lstrip(' ')
						location = line[c]
#						print("Replaced placeholder with ", NPCLocal[randomNumber])
						if spoiler is 1:
							for entry in spoilerLog:
								if entry == areaClean:
									s += 1
									logIndex = int(spoilerLog.index(entry) + s)
									logEntry = spoilerLog[logIndex] + NPCLocal[randomNumber][:19] + "\n"
									spoilerLog[logIndex] = logEntry
						NPCLocal.remove(NPCLocal[randomNumber])
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


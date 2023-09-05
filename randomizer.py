import os
import random
import constants
import re

from fileHandler import readFiles, writeFiles, writeLog

# Builds local item pool while replacing items with placeholder text to be changed into randomized items; placeholder text named to have length of 19
def randomize(dir, prefs, fileList, spoilerLog, itemList, itemLocal, itemListExpanded, NPCList, NPCList2, NPCLocal):
	random.seed(prefs["customSeed"])
	files = readFiles(dir, fileList)
	fileNumber = 0
	spoilerLogCMD = ""
	for settings in spoilerLog:
		spoilerLogCMD += settings.replace("\n", " | ")
	print(spoilerLogCMD)
	for key in files:
		while (fileNumber == 0 and key != "\\castle_basement_master.pak") or (fileNumber == 1 and key != "\\castle_nightmare_master.pak") or (fileNumber == 7 and key != "\\overworld_lsp_cave.pak"):
			fileNumber += 1
		lineList = files[key]
		areaClean = key.lstrip("\\").rstrip(".pak") + ": \n"
		lineNumber = 0
		placeholderCountItem = 0
		placeholderCountNPC = 0
		placeholder = "placeholder"
		if prefs["spoilerLog"] == 1:
			spoilerLog.append(areaClean)
		if prefs["itemRandomization"] != 0:

# Takes items from desired items to be randomized and replaces them with a placeholder while adding them to the item pool
			print("Now generating item pool from:", dir + key)
			lineNumber = 0
			for line in lineList:
				for item in itemList:
					while item in line:
						if placeholderCountItem >= 10:
							placeholder = "daplaceholdertext" + str(placeholderCountItem)
						else:
							placeholder = "daplaceholdertext0" + str(placeholderCountItem)
						itemLocal.append(item.ljust(19))
						replacement = lineList[lineNumber].replace(item, placeholder, 1)
						lineList[lineNumber] = replacement.lstrip('')
						line = lineList[lineNumber]
						print("Added", item, "to item pool")
						if prefs["spoilerLog"] == 1:
							logEntryReadable = constants.logListMaster[fileNumber][placeholderCountItem] + "  ->  "
							#print(logEntryReadable)
							i = item + str(placeholderCountItem) + " ->  "
							spoilerLog.append(logEntryReadable)
						placeholderCountItem += 1
				lineNumber += 1
			itemLocal.sort()
			#print(str(placeholderCountItem) + ", " + str(placeholderCountNPC))
# Takes NPCs and replaces them with a placeholder while adding them to the item pool
		if prefs["npcRandomization"] != 0:
			print("Now generating NPC from:", dir + key)
			lineNumber = 0
			NPCListMaster = NPCList + NPCList2
			for line in lineList:
				for nonplay in NPCListMaster:
					while nonplay in line:
						if placeholderCountNPC >= 10:
							placeholder = "creatingafiftysevencharacterplaceholderisnotveryfunlolz" + str(placeholderCountNPC)
						else:
							placeholder = "creatingafiftysevencharacterplaceholderisnotveryfunlolz0" + str(placeholderCountNPC)
						NPCLocal.append(nonplay)
						replacement = lineList[lineNumber].replace(nonplay, placeholder, 1)
						lineList[lineNumber] = replacement.lstrip('')
						line = lineList[lineNumber]
						print("Added", nonplay[:19], "to NPC pool")
						if prefs["spoilerLog"] == 1:
							n = nonplay[:19] + "  ->  "
							spoilerLog.append(n)
						placeholderCountNPC += 1
				lineNumber += 1
			NPCLocal.sort()

		#print(str(placeholderCountItem) + ", " + str(placeholderCountNPC)) #debug purposes
# Writing to files
		if prefs["spoilerLog"] == 1:
			spoilerLog.append( "\n")
		print("Successfully pooled from", dir + key)
		fileNumber += 1

# Uses expanded item pool if selected
	if prefs["itemRandomization"] == 2:
		print("Adding expanded items to pool")
		while len(itemListExpanded) != 0:
			fillerSpot = itemLocal.index("PickupChestItemKey\0")
			fillerReplace = itemListExpanded[random.randint(0, len(itemListExpanded)-1)]
			replacement = itemLocal[fillerSpot].replace("PickupChestItemKey\0", fillerReplace)
			itemLocal[fillerSpot] = replacement
			itemListExpanded.remove(fillerReplace)
		print("Successfully added expanded items to pool")

# If Guntsanity is enabled, replaces all NPCs within pool with Gunter
	if prefs["npcRandomization"] == 3:
		print("wenk?")
		lineNumber = 0
		for npc in NPCLocal:
			NPCLocal[lineNumber] = "Gunter\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0npc_gunter.pak\0\0\0\0\0\0\0\0\0\0\0"
			lineNumber += 1
		print("wenk!")

# Replaces placeholders with actual items from local item pool
	for key in files:
		lineList = files[key]
		areaClean = key.lstrip("\\").rstrip(".pak") + ": \n"
		#flamboTreeList = ["placeholdertextomg0\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg1\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg2\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg3\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg4\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg5\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg6\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg7\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg8\0\0\0\0\0dry_tree.wf3d", "placeholdertextomg9\0\0\0\0\0dry_tree.wf3d"]
		fireTree = "\0\0\0\0\0dry_tree.wf3d"
		heroRock = "global:forest_pickup_heavy_1.wf3d\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0" + bytes.fromhex("01").decode("latin-1") + "\0\0\0"
		lineNumber = 0
		spoilerLogIndex = 0
		standardCheck = 0
		#print("Now distributing items and NPCs in:", dir + key)
		if prefs["itemRandomization"] != 0:
			print("Now distributing items in:", dir + key)
			for line in lineList:

# Item replacement with exceptions for nightmare castle, dry trees and heavy rocks; Exceptions only occur if logic is on
				while "daplaceholdertext" in line:
					if standardCheck >= 10:
						placeholder = "daplaceholdertext" + str(standardCheck)
					else:
						placeholder = "daplaceholdertext0" + str(standardCheck)
					while placeholder in line:
						length = len(itemLocal)
						randomNumber = random.randint(0, length-1)
						heroRockTest = heroRock + placeholder
						if prefs["itemLogic"] != 0 and heroRockTest in line:
							#print("Heavy rock worky")
							while itemLocal[randomNumber] == "PickupHeroGauntlet\0":
								randomNumber = random.randint(0, length-1)
						fireTreeTest = placeholder + fireTree
						if prefs["itemLogic"] != 0 and fireTreeTest in line:
							#print("Dry tree worky")
							while itemLocal[randomNumber] == "PickupGrabbyHand\0\0\0" or itemLocal[randomNumber] == "PickupFlambo\0\0\0\0\0\0\0":
								randomNumber = random.randint(0, length-1)
						if prefs["itemLogic"] != 0 and key == "\\castle_nightmare_master.pak":
							while itemLocal[randomNumber] == "PickupGrabbyHand\0\0\0" or itemLocal[randomNumber] == "PickupHeroGauntlet\0":
								randomNumber = random.randint(0, length-1)
							if prefs["lspCaveRando"] == 1:
								while itemLocal[randomNumber] == "PickupSlammyHand\0\0\0" or itemLocal[randomNumber] == "PickupGrabbyHand\0\0\0" or itemLocal[randomNumber] == "PickupHeroGauntlet\0":
									randomNumber = random.randint(0, length-1)
						replacement = lineList[lineNumber].replace(placeholder, itemLocal[randomNumber], 1)
						lineList[lineNumber] = replacement.lstrip(' ')
						line = lineList[lineNumber]
						print("Replaced placeholder with", itemLocal[randomNumber])
						#print("Replaced placeholder with item")
						if prefs["spoilerLog"] == 1:
							for entry in spoilerLog:
								if entry == areaClean:
									spoilerLogIndex += 1
									logItemClean = itemLocal[randomNumber].replace("Pickup", "")
									logIndex = int(spoilerLog.index(entry) + spoilerLogIndex)
									logEntry = spoilerLog[logIndex] + logItemClean + "\n"
									spoilerLog[logIndex] = logEntry
						itemLocal.remove(itemLocal[randomNumber])
					standardCheck += 1
				lineNumber += 1
			print("Item distribution completed for ", dir + key)
# NPC randomization, uses similar code to the item replacement without exceptions but with a different placeholder
		if prefs["npcRandomization"] != 0:
			print("Now distributing NPCs in:", dir + key)
			lineNumber = 0
			npcCheck = 0
			for line in lineList:
				while "creatingafiftysevencharacterplaceholderisnotveryfunlolz" in line:
					if npcCheck >= 10:
						placeholder = "creatingafiftysevencharacterplaceholderisnotveryfunlolz" + str(npcCheck)
					else:
						placeholder = "creatingafiftysevencharacterplaceholderisnotveryfunlolz0" + str(npcCheck)
					while placeholder in line:
						length = len(NPCLocal)
						randomNumber = random.randint(0, length-1)
						replacement = lineList[lineNumber].replace(placeholder, NPCLocal[randomNumber], 1)
						lineList[lineNumber] = replacement.lstrip(' ')
						line = lineList[lineNumber]
						#print("Replaced placeholder with", NPCLocal[randomNumber][:19])
						print("Replaced placeholder with NPC")
						if prefs["spoilerLog"] == 1:
							for entry in spoilerLog:
								if entry == areaClean:
									spoilerLogIndex += 1
									logIndex = int(spoilerLog.index(entry) + spoilerLogIndex)
									logEntry = spoilerLog[logIndex] + NPCLocal[randomNumber][:19] + "\n"
									spoilerLog[logIndex] = logEntry
						NPCLocal.remove(NPCLocal[randomNumber])
					npcCheck += 1
				lineNumber += 1
		print("NPC distribution completed for ", dir + key)
		#print("Item and NPC distribution completed for ", dir + key)
	writeFiles(dir, files)
	print("Your seed is: ", prefs["customSeed"])
	if prefs["spoilerLog"] == 1:
		writeLog(spoilerLog)
	else:
		os.remove("spoiler.log")
	return
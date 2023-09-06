# List of files to be randomized within data folder
fileList = ["\\overworld_forest_cave.pak", "\\overworld_forest_cave_2.pak", "\\overworld_forest_master.pak", "\\overworld_iceking_cave.pak",
			"\\overworld_kingdom_master.pak", "\\overworld_mountain_cave_1.pak", "\\overworld_mountain_cave_3.pak", "\\overworld_mountain_cave_4.pak", "\\overworld_mountain_master.pak", "\\overworld_swamp_master.pak",
			"\\overworld_wasteland_cave_1.pak", "\\temple_dream_master.pak", "\\temple_fear_master.pak", "\\temple_song_master.pak"]

# List of items to check randomization; Null char added to each entry to maintain a consistent length of 19
defaultItemList = ["PickupChestItemKey\0", "PickupTreasureHuge\0", "PickupSpareThumps\0\0", "PickupTrailMix3\0\0\0\0", "PickupMeat\0\0\0\0\0\0\0\0\0", "PickupHeartPiece\0\0\0", 
			"PickupPencil\0\0\0\0\0\0\0", "PickupSweater\0\0\0\0\0\0", "PickupMapPaper\0\0\0\0\0", "PickupChestItemRBK\0", "PickupTreasureSmall", "PickupTreasureBig\0\0",
			"PickupGumGlobe\0\0\0\0\0", "PickupWoodPlank\0\0\0\0", "PickupPlasticBag\0\0\0", "PickupFruitStack\0\0\0", "PickupHeroGauntlet\0", "PickupTrailMix1\0\0\0\0", "PickupTrailMix2\0\0\0\0", "PickupTrailMix4\0\0\0\0", "PickupGrabbyHand\0\0\0"]
	
# List of items that work when put into the game, however are not found to be pooled as well as are not worth putting into itemsListExpanded
itemListUnused = ["PickupNutStack\0\0\0\0\0", "PickupJake\0\0\0\0\0\0\0\0\0"]

# Items that are found on in bushes and pots. Although their placements that would be replaced are consistent, they are separated into a different item list so that the user may toggle them off
itemListExtras = ["PickupHealthOne\0\0\0\0", "PickupFruits\0\0\0\0\0\0\0", "PickupDemonHeart\0\0\0", "PickupNuts\0\0\0\0\0\0\0\0\0", "PickupPieFairy\0\0\0\0\0"]

# List of items to be removed in favor of items from itemListExpanded while using expanded item pool; Currently depricated in favor of replacing PickupChestItemKey as they are entirely useless outside of dungeons
itemListReplaced = ["PickupTreasureSmall", "PickupTreasureBig\0\0", "PickupDemonHeart\0\0\0", "PickupNuts\0\0\0\0\0\0\0\0\0", "PickupFruits\0\0\0\0\0\0\0"]

# Items that could be added to the item pool, but are not found within the game via current methods or are only found in the shop, which can't currently be randomized. Used for expanded item pool
itemListExpanded = ["PickupFlambo\0\0\0\0\0\0\0", "PickupBananarang\0\0\0", "PickupLadyRing\0\0\0\0\0", "PickupSlammyHand\0\0\0", "PickupSweater\0\0\0\0\0\0", "PickupLoveNote\0\0\0\0\0", "PickupHeatSignature", "PickupMindGames\0\0\0\0", "PickupFanfiction\0\0\0", "PickupEnergyDrink\0\0", "PickupBugMilk\0\0\0\0\0\0", "PickupEnchiridion\0\0"]

# List of all items that can be toggled on and off when using custom item pool
itemListCustom = ["PickupTreasureSmall", "PickupTreasureBig\0\0", "PickupTreasureHuge\0", "PickupPencil\0\0\0\0\0\0\0", "PickupMapPaper\0\0\0\0\0", "PickupChestItemKey\0", "PickupChestItemRBK\0",
				  "PickupPlasticBag\0\0\0", "PickupTrailMix\0\0\0\0\0", "PickupTrailMix1\0\0\0\0", "PickupTrailMix2\0\0\0\0", "PickupTrailMix3\0\0\0\0", "PickupTrailMix4\0\0\0\0",  "PickupSpareThumps\0\0", 
				  "PickupHeartPiece\0\0\0", "PickupGumGlobe\0\0\0\0\0", "PickupWoodPlank\0\0\0\0", "PickupFruits\0\0\0\0\0\0\0", "PickupFruitStack\0\0\0", "PickupNuts\0\0\0\0\0\0\0\0\0", "PickupDemonHeart\0\0\0", "PickupHealthOne\0\0\0\0",
				  "PickupBananarang\0\0\0", "PickupGrabbyHand\0\0\0", "PickupFlambo\0\0\0\0\0\0\0", "PickupHeroGauntlet\0", "PickupLadyRing\0\0\0\0\0", "PickupSlammyHand\0\0\0", "PickupSweater\0\0\0\0\0\0",  
				  "PickupLoveNote\0\0\0\0\0", "PickupHeatSignature", "PickupMindGames\0\0\0\0", "PickupFanfiction\0\0\0", "PickupEnergyDrink\0\0", "PickupBugMilk\0\0\0\0\0\0", "PickupEnchiridion\0\0"]

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
			bytes.fromhex("436F616C4D616E000000000000000000000000000000000000000000000000006E70635F636F616C6D616E2E70616B00000000000000000000").decode("latin-1"), # Coal Man entry in NPCList
			bytes.fromhex("50617274795061740000000000000000000000000000000000000000000000006E70635F70617274797061742E70616B000000000000000000").decode("latin-1"), # Party Pat entry in NPCList (required for Prismo)
			bytes.fromhex("5374616E6C6579000000000000000000000000000000000000000000000000006E70635F7374616E656C792E70616B00000000000000000000").decode("latin-1")] # Stanley entry in NPCList (required for Prismo)


# List of readable spoiler log entries for \\castle_basement_master.pak
logList0 = ["Nameless Castle Basement Key Chest", "Nameless Castle Basement Treasure Chest"]

# List of readable spoiler log entries for \\castle_nightmare_master.pak
logList1 = ["Nightmare Castle Huge Treasure 1", "Nightmare Castle Huge Treasure 2", "Nightmare Castle TrailMix1", "Nightmare Castle Huge Treasure 3", "Nightmare Castle Huge Treasure 4", "Nightmare Castle Spare Thumps 1", "Nightmare Castle TrailMix3", "Nightmare Castle Key 1", "Nightmare Castle Key 2", "Nightmare Castle Key 3", "Nightmare Castle Key 4", "Nightmare Castle Key 5", "Nightmare Castle Meat", "Nightmare Castle Thump Shard", "Nightmare Castle Pencil Chest", "Nightmare Castle Like Like Sweater Chest", "Nightmare Castle Map Paper Chest", "Nightmare Castle Key 6", "Nightmare Castle Key 7", "Nightmare Castle Key 8", "Nightmare Castle Key 9", "Nightmare Castle Really Big Key Chest", "Nightmare Castle Small Treasure 1", "Nightmare Castle Small Treasure 2", "Nightmare Castle Small Treasure 3", "Nightmare Castle Big Treasure 1", "Nightmare Castle Big Treasure 2", "Nightmare Castle Big Treasure 3", "Nightmare Castle Big Treasure 4"]

# List of readable spoiler log entries for \\overworld_forest_cave.pak; Only in map pool due to presense of NPC, so no spoiler log entries present
logList2 = []

# List of readable spoiler log entries for \\overworld_forest_cave_2.pak; Only in map pool due to presense of NPC, so no spoiler log entries present
logList3 = []

# List of readable spoiler log entries for \\overworld_forest_master.pak
logList4 = ["Song Forest Heavy Rock Chest", "Song Forest South Enchiridion Stone Chest", "Song Forest Dry Tree Chest", "Song Forest Circle Patch Bush", "Song Forest Buncha Bushes Bush", "Song Forest South Tetromino Bush", "Song Forest Wooden Boards Bush", "Song Forest Heavy Rock"]

# List of readable spoiler log entries for \\overworld_iceking_cave.pak
logList5 = ["Ice King Cave Heavy Rock"]

# List of readable spoiler log entries for \\overworld_kingdom_master.pak
logList6 = ["Castle Outskirts Perimeter Chest", "Castle Outskirts North Enchiridion Stone Chest", "Castle Outskirts Fairy Fountain Dry Tree", "Castle Outskirts Broken Bridge Chest", "Castle Outskirts Baggy Cave Chest", "Castle Outskirts Perimeter Dry Tree", "Castle Outskirts Heavy Rock" ]

# List of readable spoiler log entries for \\overworld_lsp_cave.pak
logList7 = ["LSP Cave Key Chest", "LSP Cave Pencil Chest", "LSP Cave Map Paper Chest", "LSP Cave Really Big Key Chest"]

# List of readable spoiler log entries for \\overworld_mountain_cave_1.pak; Only in map pool due to presense of NPC, so no spoiler log entries present
logList8 = []

# List of readable spoiler log entries for \\overworld_mountain_cave_3.pak; Only in map pool due to presense of NPC, so no spoiler log entries present
logList9 = []

# List of readable spoiler log entries for \\overworld_mountain_cave_4.pak
logList10 = ["Dream Mountain South Cave Chest"]

# List of readable spoiler log entries for \\overworld_mountain_master.pak
logList11 = ["Dream Mountain Fairy Fountain Ledge Chest", "Dream Mountain Butt Rock Dry Tree", "Dream Mountain Magic Man House Dry Tree", "Dream Mountain South Enchiridion Stone Dry Tree", "Dream Mountain Broken Bridge Chest", "Dream Mountain North Entrance Heavy Rock", "Dream Mountain Fairy Fountain Outskirts Bush", "Dream Mountain Mountain North Heavy Rock", "Dream Mountain Trail Mix Shop Dry Tree"]

# List of readable spoiler log entries for \\overworld_swamp_master.pak
logList12 = ["Fear Swamp Broken Bridge Chest", "Fear Swamp Temple Outskirts Dry Tree", "Fear Swamp Oceanside Dry Tree", "Fear Swamp Huge Treasure Chest", "Fear Swamp Maze South Dry Tree", "Fear Swamp Maze North Wooden Boards Dry Tree"]

# List of readable spoiler log entries for \\overworld_wasteland_cave_1.pak
logList13 = ["Fear Swamp Gunter Cave Chest"]

# List of readable spoiler log entries for \\temple_dream_master.pak
logList14 = ["Dream Temple 2F Ledge Key Chest", "Dream Temple 2F Dark Room Key Chest", "Dream Temple 1F Switch Room Huge Treasure Chest", "Dream Temple 3F Locked Stairs Huge Treasure Chest ", "Dream Temple 3F Spare Thumps Chest", "Dream Temple 1F Pencil Chest", "Dream Temple 1F Map Paper Chest", "Dream Temple 2F Fruit Stack Chest", "Dream Temple 3F Spike Cage Key Chest", "Dream Temple 1F Main Room Right Key Chest", "Dream Temple 1F Main Room Left Key Chest", "Dream Temple 1F Spike Cage Huge Treasure Chest", "Dream Temple 1F Really Big Key Chest", "Dream Temple 1F Hero Gauntlet Chest", "Dream Temple 1F Hazard Hallway Key Chest", "Dream Temple 4F Gum Globe Chest", "Dream Temple 2F TrailMix1 Chest", "Dream Temple 3F Pressure Plate Room Key Chest", "Dream Temple 3F Dark Room ANNOYING POOL FLOATIE ENEMY Key Chest", "Dream Temple 2F West Huge Treasure Chest", "Dream Temple Big Treasure Chest"]

# List of readable spoiler log entries for \\temple_fear_master.pak
logList15 = ["Fear Temple 3F Key Chest", "Fear Temple B1 Pencil Chest", "Fear Temple F1 Map Paper Chest", "Fear Temple B1 Really Big Key Chest", "Fear Temple F1 Underwater Gum Globe Chest", "Fear Temple B1 Spare Thumps Chest", "Fear Temple Fruit Stack 1", "Fear Temple 1F Underwater TrailMix2 Chest", "Fear Temple Fruit Stack 2", "Fear Temple 1F Underwater TrailMix3 Chest"]

# List of readable spoiler log entries for \\temple_song_master.pak
logList16 = ["Song Temple 1F Ledge Key Chest", "Song Temple 1F Box Room Key Chest", "Song Temple 1B Puzzle Room Key Chest", "Song Temple 1B Pencil Chest", "Song Temple 1F Map Paper Chest", "Song Temple 2F Really Big Key Chest", "Song Temple 1B Grabby Hand Chest", "Song Temple 1F Gum Globe Chest", "Song Temple 2F Huge Treasure Chest", "Song Temple 1F Huge Treasure Chest", "Song Temple 2F Sleeping Magi Room Key Chest", "Song Temple 2F Sleeping Magi Room Small Treasure Chest"]

# List of all log lists
logListMaster = [logList0, logList1, logList2, logList3, logList4, logList5, logList6, logList7, logList8, logList9, logList10, logList11, logList12, logList13, logList14, logList15, logList16]



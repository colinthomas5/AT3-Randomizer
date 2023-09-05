import os

def readFiles(dir, fileList):
	files = {}
	for area in fileList:
		path = dir + area
		openFile = open(path, "r+", encoding="latin-1", newline='')
		files[area] = openFile.readlines()
	return files

def writeFiles(dir, files):
	for key in files:
		path = dir + key
		openFile = open(path, "r+", encoding="latin-1", newline='')
		openFile.seek(0)
		openFile.truncate(0)
		for line in files[key]:
			openFile.write(line)
		openFile.close()
	return

def writeLog(spoilerLog):
	logPath = os.getcwd() + "\\spoiler.log" 
	log = open(logPath, 'w')
	for entry in spoilerLog:
		log.write(str(entry))
	print("Log saved to ", logPath)
	log.close()
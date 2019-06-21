# Access Rename Folder
	# For Each File:
		# Copy to renamed folder
			# Inside renamed folder (all file types)
				# Get date Taken
				# Change name


# Open Rename Folder
import os, sys
from PIL import Image
from shutil import copyfile # copy images to new dest.
	# copyfile(src, dst)
# For Videos:
	# Download crtime
	# pip3 install ~/Downloads/crtime-0.0.6-py2.py3-none-any.whl
from crtime import get_crtimes_in_dir
import datetime
import filecmp


# def getDateAndTime(filePath):
# 	return Image.open(filePath)._getexif()[36867]

def getFileType(file): # USE
	return file.split(".")[-1]

def newFileName(utcTime, file): # use
	fileType = getFileType(file)
	newName = utcTime[0:4] + "_" + utcTime[5:7] + "_" + utcTime[8:10] + "_at_" + utcTime[11:13] + "_" + utcTime[14:16] + "_" + utcTime[17:19] + "." + fileType
	return newName

def getUtcTime(filePath):
	return Image.open(filePath)._getexif()[36867]

def getNewPhotoName(file, filePath):
	fileType = getFileType(file)
	try:
		utcTime = getUtcTime(filePath)
		newName = newFileName(utcTime, file)
	except KeyError:
		newName = "error_img_" + file
	except TypeError:
		newName = "error_img_" + file
	return newName
def getNewVideoName(fullVideoLocation, videoOrigFile):
	for longFile, date in get_crtimes_in_dir(videoOrigFile, raise_on_error=True, as_epoch=True):
		if (filecmp.cmp(longFile, fullVideoLocation)):
			fileType = getFileType(longFile)
			epochTime = str(date)
			utcTime = datetime.datetime.fromtimestamp(float(epochTime)).strftime('%Y-%m-%d %H:%M:%S')
			newName = newFileName(utcTime, longFile)
			return newName
	return 0

def getOrigFilePath(file, fileLocation):
	return fileLocation + "/" + file

def checkForRepeatedFile(newFileName, newLocation):
	directoryFiles = os.listdir(newLocation)
	print(newFileName + " ***************************************** compare files")
	originalNoType = newFileName.split(".")[0]
	extention = 0
	while True:
		extended = 0
		for file in directoryFiles:
			if (str(file) == str(newFileName)):
				print("Repeat ------------------------------------------ ")
				print("\t" + newFileName)
				fileType = getFileType(newFileName)
				noType = newFileName.split(".")[0]
				extention = extention + 1
				newFileName = noType + "_" + str(extention) + "." + fileType
				# print ("Extended: " + newFileName)
				extended = 1
				print ("Extention: " + str(extention) )
				# change name + 1
		if (extended == 0):
			if (extention > 0):
				newFileName = originalNoType + "_" + str(extention) + "." + fileType
				print ("Extended: " + newFileName)
			return newFileName


def moveNewNamedFile(originalFile, originalLocation, newName, newLocation):
	oldDestination = originalLocation + "/" + originalFile
	newName = checkForRepeatedFile(newName, newLocation)
	newDestination = newLocation + "/" + newName
	copyfile(oldDestination, newDestination)


def renameFilesFromRename():
	folderToRenameFrom = "Rename"
	folderToPlaceNewFileIn = "Done"
	directoryFiles = os.listdir(folderToRenameFrom)
	for file in directoryFiles: # For each file in Rename folder:
		fullFileLocation = folderToRenameFrom + "/" + file
		newFileName = 0
		fileType = getFileType(file)
		filePath = getOrigFilePath(file, folderToRenameFrom)
		if (fileType.lower() == "jpg"): # if photo
			newFileName = getNewPhotoName(file, filePath)
		elif (fileType == "m4v" or fileType == "MOV" or fileType == "mp4"):
			newFileName = getNewVideoName(fullFileLocation, folderToRenameFrom)
		if (newFileName != 0): # move new file
			moveNewNamedFile(file, folderToRenameFrom, newFileName, folderToPlaceNewFileIn)
			print(file + " -> " + newFileName)
		if (newFileName == 0 and str(fileType) != "DS_Store"):
			newFileName = "mistake" + file
			moveNewNamedFile(file, folderToRenameFrom, newFileName, folderToPlaceNewFileIn)
			print(file + " -> " + newFileName)
		# getNewPhotoName(file, fielPath)

renameFilesFromRename()
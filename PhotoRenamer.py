# Access Rename Folder
	# For Each File:
		# Copy to renamed folder
			# Inside renamed folder (all file types)
				# Get date Taken
				# Change name


# Open Rename Folder
import os, sys
from PIL import Image


def getDateAndTime(filePath):
    return Image.open(filePath)._getexif()[36867]

def moveRenameablesToDone():
	return "not done"

def renameFilesInDirectory(directoryOfPathToRename):
	directoryFiles = os.listdir(directoryOfPathToRename)
	for file in directoryFiles: # For each file in Rename folder:
		fileName = file # get individual file name
		fileType = fileName.split(".")[-1] # get file type for each photo
		if (fileType == "txt"):
			print (fileName + " - a " + fileType + " file")

		elif (fileType == "jpg"):
			photoPath = directoryOfPathToRename + "/" + file
			date = getDateAndTime(photoPath)
			print ("\t" + fileName + " - a " + fileType + " file -  was created: " + date )
			newName = date[0:4] + "_" + date[5:7] + "_" + date[8:10] + "_at_" + date[11:13] + "_" + date[14:16] + "_" + date[17:19] + "." + fileType
			print ("\t\tYour new file name is " + newName)

renameFilesInDirectory("Rename")
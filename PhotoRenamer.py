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


def getDateAndTime(filePath):
    return Image.open(filePath)._getexif()[36867]

def moveRenameablesToDone(originalFile, newName):
	oldDestination = "Rename/" + originalFile
	newDestination = "Done/" + newName
	copyfile(oldDestination, newDestination)

def renameFilesFromRename():
	directoryFiles = os.listdir("Rename")
	for file in directoryFiles: # For each file in Rename folder:
		fileName = file # get individual file name
		fileType = fileName.split(".")[-1] # get file type for each photo

		if (fileType == "jpg"):
			photoPath = "Rename/" + file
			date = getDateAndTime(photoPath)
			print ("\t" + fileName + " - a " + fileType + " file -  was created: " + date )
			newName = date[0:4] + "_" + date[5:7] + "_" + date[8:10] + "_at_" + date[11:13] + "_" + date[14:16] + "_" + date[17:19] + "." + fileType
			print ("\t\tYour new file name is " + newName)
			moveRenameablesToDone(file, newName)

renameFilesFromRename()

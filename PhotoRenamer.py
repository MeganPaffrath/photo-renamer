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


def getDateAndTime(filePath):
	return Image.open(filePath)._getexif()[36867]

def getFileType(file):
	return file.split(".")[-1]

def moveRenameablesToDone(originalFile, newName):
	oldDestination = "Rename/" + originalFile
	newDestination = "Done/" + newName
	copyfile(oldDestination, newDestination)

def newFileName(utcTime, file):
	fileType = getFileType(file)
	newName = utcTime[0:4] + "_" + utcTime[5:7] + "_" + utcTime[8:10] + "_at_" + utcTime[11:13] + "_" + utcTime[14:16] + "_" + utcTime[17:19] + "." + fileType
	return newName

def renamedAndMovedMSG(originalFile, newName):
	print("\t" + newName + " -- was created from " + originalFile)

def unkFileTypeCopy():
	directoryFiles = os.listdir("Rename")
	for file in directoryFiles: # For each file in Rename folder:
		fileType = file.split(".")[-1] # get file type for each photo
		if (fileType.lower() != "jpg" and fileType != "m4v" and fileType != "MOV" and fileType != "mp4"):
			newName = "error" + file
			moveRenameablesToDone(file, newName)
			renamedAndMovedMSG(file, newName)


def renamePhotos():
	directoryFiles = os.listdir("Rename")
	for file in directoryFiles: # For each file in Rename folder:
		fileName = file # get individual file name
		fileType = fileName.split(".")[-1] # get file type for each photo

		if (fileType.lower() == "jpg"):
			photoPath = "Rename/" + file
			try:
				utcTime = getDateAndTime(photoPath)
				newName = newFileName(utcTime, file)
			except KeyError:
				newName = "error" + file
			except TypeError:
				newName = "error" + file
			moveRenameablesToDone(file, newName)
			renamedAndMovedMSG(file, newName)


def renameVideos():
	for longFile, date in get_crtimes_in_dir("./Rename", raise_on_error=True, as_epoch=True):
		file = longFile.split("./Rename/")[-1]
		fileType = getFileType(file)
		if (fileType == "m4v" or fileType == "MOV" or fileType == "mp4"):
			epochTime = str(date)
			utcTime = datetime.datetime.fromtimestamp(float(epochTime)).strftime('%Y-%m-%d %H:%M:%S')
			newName = newFileName(utcTime, file)
			moveRenameablesToDone(file, newName)
			renamedAndMovedMSG(file, newName)	

def renameFilesFromRename():
	renamePhotos()
	renameVideos()
	unkFileTypeCopy()


renameFilesFromRename()

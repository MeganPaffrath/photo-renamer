# photoRenamer

- Should rename: JPG, jpg, mp4, MOV
- If date not found:
	- File saved as: errorFILENAME.ext
- Invalid files:
	- Fet saved as mistakeFILENAME.ext
	- Current encountered invalid files:
		- HEIG, PNG


1. Save py program in a file called "PhotoRenamer" (or something else if you wish)
2. Within that folder make 2 folders: "Rename" and "Done"
3. Put photos to rename in the "Rename" folder
4. Run from terminal
5. Make sure all of your files got renamed propperly in the Done folder
6. Move files out of both folders to use again

### FORMAT
- Files will be saved as follows:
	- yyyy_mm_dd_at_hh_mm_ss_#.ext
	- '_#' is only added if the time is repeated for a photo.
	- If this occurs, the photos are probably very similar, or even the same
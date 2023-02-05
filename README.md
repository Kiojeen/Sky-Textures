README
Background
The goal of this project is to convert sky textures in the format of .ktx to .png and then crop them using the UV map information.

Steps Involved
Installing required libraries:
The following libraries need to be installed for the code to work: re, PIL, and os. If these libraries are not present, the code will automatically install them for you.

Converting .ktx files to .png files:
The code will search for all files ending with .kts in the folder called "Input". For each .ktx file, it will use the tool "PVRTexToolCLI.exe" to convert it to a .png file. The result will be saved in a folder called "PNG".

Cropping .png files using UV map information:
The code will parse the "UIPackedAtlas.lua" file to extract information about the UV map. This information will be used to crop each .png file and save the result in a separate file with the same name as the image region. The code will also remove the black background from the cropped images if needed.

Cleaning up intermediate files:
After the .png files are successfully cropped, the code will delete all intermediate .pvr files.

Conclusion
This code provides a streamlined solution to convert and crop sky textures. With just a few lines of code, the task of converting and cropping hundreds of images becomes a breeze.

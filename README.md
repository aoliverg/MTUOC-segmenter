# MTUOC-segmenter
Scripts and programs to segment text files and corpora.

## Introduction

The scripts and programs in this repository allows segmenting a text file or all the files in a given directory using a SRX (Segmentation Rules eXchange) file. When segmenting a full directory, the segmented files can be placed in a output directory or in a single file. Command line and GUI versions of the programs are provided. Command line versions accept the option -h to show the help of the program. GUI versions offer a very intuitive interface. The following programs are provided:

* txt2segmentedtext.py: Command line version to segment a single file.
* txt2segmentedtext_GUI.py: GUI version to segment a single file.
* txt2segmentedtextDirDir.py: Command line version to segment all the files of a given directory and place the segmented files in another directory.
* txt2segmentedtextDirDir_GUI.py: GUI version to segment all the files of a given directory and place the segmented files in another directory.
* txt2segmentedtextDirFile.py: Command line version to segment all the files of a given directory and write the segments in a single file.
* txt2segmentedtextDirFile_GUI.py: GUI version to segment all the files of a given directory and write the segments in a single file.

All the files allows to include or not the "<p>" paragraph mark between paragraphs. Including this mark is useful if you plan to align files with hunalign.

GUI versios of the programs are also provided as a Windows executable files. They can be downloaded from the following links:

* txt2segmentedtext_GUI.py: 
* txt2segmentedtextDirDir_GUI.py: 
* txt2segmentedtextDirFile_GUI.py: 

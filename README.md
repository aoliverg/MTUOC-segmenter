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

* txt2segmentedtext_GUI.py: [http://lpg.uoc.edu/MTUOC-segmenter/txt2segmentedtext_GUI.exe](http://lpg.uoc.edu/MTUOC-segmenter/txt2segmentedtext_GUI.exe)
* txt2segmentedtextDirDir_GUI.py: [http://lpg.uoc.edu/MTUOC-segmenter/txt2segmentedtextDirDir_GUI.exe](http://lpg.uoc.edu/MTUOC-segmenter/txt2segmentedtextDirDir_GUI.exe)
* txt2segmentedtextDirFile_GUI.py: [http://lpg.uoc.edu/MTUOC-segmenter/txt2segmentedtextDirFile_GUI.exe](http://lpg.uoc.edu/MTUOC-segmenter/txt2segmentedtextDirFile_GUI.exe)

## Requirements
  
Programs are written in Pyhton version 3, and the following requirements are needed:
```
nltk
PyYAML
regex
```
A requirements.txt file is provided. The requirements can be installed using:
```  
sudo pip3 install -r requirements.txt``
```  
or 
```  
pip install -r requirements.txt``
  
  depending on your Python 3 installation.
  
  ## Usage
  
  The use is very simple, for the command line versions use the -h option and the help will be show. For example:

```
python3 txt2segmentedtext.py -h
usage: txt2segmentedtext.py [-h] -i INPUT_FILE -o OUTPUT_FILE -s SRXFILE -l SRXLANG [-p]

A script to segment all the files in one directory and save the segmented files in another directory.

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
                        The input file to segment.
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
                        The output segmented file.
  -s SRXFILE, --srxfile SRXFILE
                        The SRX file to use
  -l SRXLANG, --srxlang SRXLANG
                        The language as stated in the SRX file
  -p, --paragraph       Add the <p> pararaph mark
```
    
    
  
  
  

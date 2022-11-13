#    txt2segmentDIR
#    Copyright (C) 2022  Antoni Oliver
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#    Segmentation is performed using srx_segmenter: https://github.com/narusemotoki/srx_segmenter
#    The code is copied into this script.

import argparse
import sys
import re
import codecs
import nltk
import glob
import os

#SRX_SEGMENTER
import lxml.etree
import regex
from typing import (
    List,
    Set,
    Tuple,
    Dict,
    Optional
)

from tkinter import *
from tkinter.ttk import *

import tkinter 
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter.filedialog import askdirectory
from tkinter import messagebox

class SrxSegmenter:
    """Handle segmentation with SRX regex format.
    """
    def __init__(self, rule: Dict[str, List[Tuple[str, Optional[str]]]], source_text: str) -> None:
        self.source_text = source_text
        self.non_breaks = rule.get('non_breaks', [])
        self.breaks = rule.get('breaks', [])

    def _get_break_points(self, regexes: List[Tuple[str, str]]) -> Set[int]:
        return set([
            match.span(1)[1]
            for before, after in regexes
            for match in regex.finditer('({})({})'.format(before, after), self.source_text)
        ])

    def get_non_break_points(self) -> Set[int]:
        """Return segment non break points
        """
        return self._get_break_points(self.non_breaks)

    def get_break_points(self) -> Set[int]:
        """Return segment break points
        """
        return self._get_break_points(self.breaks)

    def extract(self) -> Tuple[List[str], List[str]]:
        """Return segments and whitespaces.
        """
        non_break_points = self.get_non_break_points()
        candidate_break_points = self.get_break_points()

        break_point = sorted(candidate_break_points - non_break_points)
        source_text = self.source_text

        segments = []  # type: List[str]
        whitespaces = []  # type: List[str]
        previous_foot = ""
        for start, end in zip([0] + break_point, break_point + [len(source_text)]):
            segment_with_space = source_text[start:end]
            candidate_segment = segment_with_space.strip()
            if not candidate_segment:
                previous_foot += segment_with_space
                continue

            head, segment, foot = segment_with_space.partition(candidate_segment)

            segments.append(segment)
            whitespaces.append('{}{}'.format(previous_foot, head))
            previous_foot = foot
        whitespaces.append(previous_foot)

        return segments, whitespaces


def parse(srx_filepath: str) -> Dict[str, Dict[str, List[Tuple[str, Optional[str]]]]]:
    """Parse SRX file and return it.
    :param srx_filepath: is soruce SRX file.
    :return: dict
    """
    tree = lxml.etree.parse(srx_filepath)
    namespaces = {
        'ns': 'http://www.lisa.org/srx20'
    }
    
    global rules
    rules = {}

    for languagerule in tree.xpath('//ns:languagerule', namespaces=namespaces):
        rule_name = languagerule.attrib.get('languagerulename')
        if rule_name is None:
            continue

        current_rule = {
            'breaks': [],
            'non_breaks': [],
        }

        for rule in languagerule.xpath('ns:rule', namespaces=namespaces):
            is_break = rule.attrib.get('break', 'yes') == 'yes'
            rule_holder = current_rule['breaks'] if is_break else current_rule['non_breaks']

            beforebreak = rule.find('ns:beforebreak', namespaces=namespaces)
            beforebreak_text = '' if beforebreak.text is None else beforebreak.text

            afterbreak = rule.find('ns:afterbreak', namespaces=namespaces)
            afterbreak_text = '' if afterbreak.text is None else afterbreak.text

            rule_holder.append((beforebreak_text, afterbreak_text))

        rules[rule_name] = current_rule

    return rules



#IMPORTS FOR YAML
import yaml
from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


def segmenta(cadena):
    global rules
    global srxlang
    segmenter = SrxSegmenter(rules[srxlang],cadena)
    segments=segmenter.extract()
    resposta=[]
    for segment in segments[0]:
        segment=segment.replace("’","'")
        resposta.append(segment)
    resposta="\n".join(resposta)
    return(resposta)

def select_directory():
    dir = askdirectory(initialdir = ".",mustexist=True, title = "Choose the output directory.")
    E1.delete(0,END)
    E1.insert(0,dir)
    E1.xview_moveto(1)
    
def select_output_file():
    outfile = asksaveasfilename(initialdir = ".",filetypes =(("text files", ["*.txt"]),("All Files","*.*")),
                           title = "Choose a file to save the segmented text.")
    E2.delete(0,END)
    E2.insert(0,outfile)
    E2.xview_moveto(1)
    
def select_srx_file():
    srxfile = askopenfilename(initialdir = ".",filetypes =(("SRX files", ["*.srx"]),("All Files","*.*")),
                           title = "Choose the SRX file to use.")
    E3.delete(0,END)
    E3.insert(0,srxfile)
    E3.xview_moveto(1)

def go():
    inDir=E1.get()
    outfile=E2.get()
    sortida=codecs.open(outfile,"w",encoding="utf-8")
    srxfile=E3.get()
    global srxlang
    srxlang=E4.get().strip()
    global rules
    rules = parse(srxfile)
    available_languages=rules.keys()
    if not srxlang in available_languages: 
        messagebox.showerror("SRX Language Error", "ERROR: language "+srxlang+" not available in "+srxfile+". Available languages: "+", ".join(available_languages))
    files = []
    for r, d, f in os.walk(inDir):
        for file in f:
            try:
                fullpath=os.path.join(r, file)  
                entrada=codecs.open(fullpath,"r",encoding="utf-8",errors="ignore")
                for linia in entrada:
                    segments=segmenta(linia)
                    if len(segments)>0:
                        if paragraph.get():
                            sortida.write("<p>\n")
                        sortida.write(segments+"\n")
            except:
                print("Error segmenting file "+fullpath+": ",sys.exc_info()[0])


top = Tk()
top.title("txt2segmentedtextDirFile_GUI")

B1=tkinter.Button(top, text = str("Input dir"), borderwidth = 1, command=select_directory,width=14).grid(row=0,column=0)
E1 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E1.xview_moveto(1)
E1.grid(row=0,column=1)

B2=tkinter.Button(top, text = str("Output file"), borderwidth = 1, command=select_output_file,width=14).grid(row=1,column=0)
E2 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E2.grid(row=1,column=1)

B3=tkinter.Button(top, text = str("SRX file"), borderwidth = 1, command=select_srx_file,width=14).grid(row=2,column=0)
E3 = tkinter.Entry(top, bd = 5, width=50, justify="right")
E3.grid(row=2,column=1)

L4 = Label(top,text="SRX Lang:").grid(sticky="E",row=3,column=0)
E4 = tkinter.Entry(top, bd = 5, width=15, justify="left")
E4.grid(sticky="W",row=3,column=1)

L5 = Label(top,text="Paragraph mark:").grid(sticky="E",row=4,column=0)
paragraph=tkinter.BooleanVar()
cbp = tkinter.Checkbutton(top,variable=paragraph, onvalue=True, offvalue=False)
cbp.grid(sticky="W",row=4,column=1)

B5=tkinter.Button(top, text = str("Segment!"), borderwidth = 1, command=go,width=14).grid(sticky="W",row=5,column=0)

E3.delete(0,END)
E3.insert(0,"segment.srx")

E4.delete(0,END)
E4.insert(0,"Generic")
   
top.mainloop()
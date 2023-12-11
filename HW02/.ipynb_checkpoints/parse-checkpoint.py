import os
import sys
from collections import defaultdict
from pathlib import Path
import string
import math
import sys
import random

#Function that converts file to utf8 format.
def convert_utf8(file_name,op_name):
    with open(file_name, 'r',encoding="utf-8",errors='ignore') as inp:
        with open(op_name, 'wb') as _file:
            for read in inp:
                _file.write(read.encode("utf-8"))
        _file.close()
    inp.close()

#Function for converting all the characters to lowercase.
def convert_lower_case(x):
    with open(x, "r+b",) as file:
        content = file.read()
        file.seek(0)
        file.write(content.lower())
        file.seek(0)
        file.close()

#Function for converting all the characters to lowercase.
def convert_lower_case(x):
    with open(x, "r+b",) as file:
        content = file.read()
        file.seek(0)
        file.write(content.lower())
        file.seek(0)
        file.close()

#Function that reads the file and removes the punct.
def read_and_remove_punct(x):

    file = open(x,  'r', encoding = 'utf_8')

    line = file.read().replace("\n", " ")
    file.close()

    removed = line.translate(str.maketrans('', '', string.punctuation))
    removed = removed.replace("w", "")
    removed = removed.replace("x", "")
    removed = removed.replace("q", "")
    removed = removed.replace("@", "")
    removed = removed.replace("¼", "")
    removed = removed.replace("Ã", "")
    removed = removed.replace("§", "")
    removed = removed.replace("¶", "")
    removed = removed.replace("Ÿ", "")
    removed = removed.replace("±", "")
    removed = removed.replace("Ä", "")
    return removed

sys.stdout = open('terminal_out_', 'w', encoding = 'utf_8') #stdout>file
convert_utf8("raw_file.txt", "utf.txt")

convert_lower_case("utf.txt") #Converting the file to lower case.
letter_list = read_and_remove_punct("utf.txt") #Reading file and keeping all of it in letter_list.
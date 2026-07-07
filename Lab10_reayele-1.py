"""
Program name: Word Analyzer 
Author: Rediet Ayele 
Purpose: 
Date: 07/07/26
"""

import pathlib
import string


class WordAnalyzer: 

    def __init__(self, filepath):
        self.__path = pathlib.Path(filepath)
        self.__word_counts = {}
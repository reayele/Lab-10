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
        self.__filepath = pathlib.Path(filepath)
        self.__word_counts = {}
    def main():
        files = {
            "1": pathlib.Path("moby_dick_ch.txt"),
            "2": pathlib.Path("frankenstein_ch1.txt"),
            "3": pathlib.Path("alice_ch1.txt"),
            "4": pathlib.Path("pride_prejudice_ch1.txt")
        }
        while True:
            print("\n --- Word Analyzer ---")
            print("Please select a file to analyze:")
            print("1. Moby Dick")
            print("2. Frankenstein")
            print("3. ALice in Wonderland")
            print("4. Pride and Prejudice")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ")
            if choice == "5":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid choice. Please select from 1-5.")
                input("\nPress Enter to return to the menu...")
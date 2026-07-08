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
            if choice in files: 
                print("\nPrcoessing", files[choice], "...")

            if choice == "5":
                print("\nGoodbye!")
                break

            else:
                print("\nInvalid choice. Please select from 1-5.")
                input("\nPress Enter to return to the menu...")
    if __name__ == "__main__":
                main()
        
    files = {
         "1": pathlib.Path("moby_dic_ch1.txt"),
         "2": pathlib.Path("moby_dic_ch1.txt"),
         "3": pathlib.Path("moby_dic_ch1.txt"),
         "4": pathlib.Path("moby_dic_ch1.txt")
    }
    
    def process_file(self):
        """Read the file and count each word."""
        try:
            if not self.__filepath.exists():
                raise FileNotFoundError
            remove_punctuation = str.maketrans("", "", string.punctuation)
            with self.__filepath.open("r", encoding="utf-8") as file:
                for line in file:
                    line = line.lower()
                    line = line.translate(remove_punctuation)
                    words = line.split()
                    
                    for word in words:
                        if word in self.__word_counts:
                            self.__word_counts[word] += 1
                        else: 
                            self.__word_counts[word] = 1
            return True
        except FileNotFoundError:
            print("Error: File not found.")
            return False


            
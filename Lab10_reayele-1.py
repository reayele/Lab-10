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
    
    def process_file(self):
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
              print("Error: File not found. ")
              return False
        
def print_report(self):
        words = list(self.__word_counts.keys())
        words.sort()

        for word in words:
            print(word, "::", self.__word_counts[word])

def main():
        files = {
             "1": pathlib.Path("princess_mars.txt"),
             "2": pathlib.Path("Tarzan.txt"),
             "3": pathlib.Path("treasure_islands.txt"),
             "4": pathlib.Path("monte_cristo.txt")
        }
        while True:
            print("\n --- Word Analyzer ---")
            print("Please select a file to analyze:")
            print("1. Princess of Mars")
            print("2. Tarzan")
            print("3. Treasure Island")
            print("4. Monte Cristo")
            print("5. Exit")

            choice = input("\nEnter your choice (1-5): ")
            if choice in files: 
                print("\nPrcoessing", files[choice], "...")
        
                analyzer = WordAnalyzer(files[choice])
                
                if analyzer.process_file():
                    analyzer.print_report()
                
                input("\nPress Enter to return to the menu...")

            elif choice == "5":
                print("\nGoodbye!")
                break
            else:
                print("\nInvalid choice. Please select from 1-5.")
                input("\nPress Enter to return to the menu...")
if __name__ == "__main__":
                main()
        

    
    
    
    
    
    
    
    
    
           
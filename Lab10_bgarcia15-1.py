"""
Lab 10: Word Analyzer
Author: Ben Garcia

Displays a menu of 4 predefined text files,
lets the user select one, reads and analyzes the file.
It will count the frequency of every word in the selected file and
print an alphabetical report.

The word analyzer class includes an optional list of "Stop words" during initialization
so that when processing the file it will ignore any words in that list so they dont appear in the final count/report

"""
from pathlib import Path
import string

class WordAnalyzer:
    """Class to analyze a text file and count the frequency of each word, with optional stop words to ignore.
    """
    def __init__(self, stop_words=None, filepath=None):
        """init method to initialize the WordAnalyzer class with an optional list of stop words.
        Will take the filepath to the text file as a string and store it as a private pathlibrary
        """
        self._path = Path(filepath) #private path object to store path string
        self._frequencies = {}  #private dictionary to store word frequencies

        if stop_words:
            self._stop_words = set(word.lower() for word in stop_words)  # Convert stop words to lowercase for case-insensitive comparison
        else:
            self._stop_words = set()  # Initialize an empty set if no stop words are provided

    def process_file(self, filepath):
        """Method to read the specified text file, 
        count the frequency of each word while ignoring stop words, 
        and store the counts in a dictionary.
            The method will return True if the file was processed successfully, or False if there was an error (e.g., file not found).
            It will also throw and exception and print an error message if the file is not found.
            
            Basic excecution steps:
            1. Attempt to open file from file path 
            2. create a translator to remove punctuation from the text using str.maketrans
            3. open the file using a with statement to ensure it is properly closed after processing
            4. iterate through each line in the file
            5.remove punctuation from the line using the translator
            6. split the cleaned line into words using the split method
            7. iterate through the split words and count the frequencies while checking each word against the stop words list.
        """
       
        
    def print_report(self):
        """Sort words alphabetically and print the frequency of each word
            by iterating through the sorted keys of the frecuencies dictionary, printing each key
            and its corresponding value 
        """
        for word in sorted(self._frequencies.keys()):
            print(f"{word}: {self._frequencies[word]}")


def main():
    """Main function to display a menu of predefined text files, 
    let the user select one, and analyze it using the WordAnalyzer class.
    Contains:
      a loop to allow the user to select files until user decides to exit 
      a dictionary to map user choices to file paths to txt files
      input validation to ensure the user selects a valid option from the menu
      calls to the WordAnalyzer class to process the selected file and print the report
    """

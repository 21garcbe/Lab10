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
        try:
            if not self._path.exists():
                print("Error: File not found.")
                return False
            
            translator = str.maketrans('', '', string.punctuation)
            
            with self._path.open('r') as file:
                for line in file:
                    clean_line = line.translate(translator)  # Remove punctuation from the line
                    words = clean_line.split()  # Split the line into words

                    #iterate through split words and count frequencies while ignoring stop words
                    for word in words:
                        if word in self._stop_words:
                            continue

                        #iterate count frequency if the word is already in the dictionary, otherwise add it with a count of 1
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1
            #return true if file was processed successfully
            return True
        #throw exception if file is not found and print error message, return false to indicate failure
        except FileNotFoundError as err:
            print(f"File not found: {err}")
            return False
       
        
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
    file_options = {
        '1': 'C:\\Users\\thebe\\PythonCSCC\\Lab10\\monte_cristo.txt',
        '2': 'C:\\Users\\thebe\\PythonCSCC\\Lab10\\princess_mars.txt',
        '3': 'C:\\Users\\thebe\\PythonCSCC\\Lab10\\Tarzan.txt',
        '4': 'C:\\Users\\thebe\\PythonCSCC\\Lab10\\treasure_island.txt'
    }
    print("--- Word Analyzer ---")
    while True:
        print("\nSelect a file to analyze:")
        for key, filename in file_options.items():
            print(f"{key}. {filename}")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Goodbye!")
            break
        elif choice in file_options:
            analyzer = WordAnalyzer(filepath=file_options[choice])
            if analyzer.process_file(file_options[choice]):
                print(f"\nWord frequency report for {file_options[choice]}:")
                analyzer.print_report()
            else:
                print("Failed to process the file.")
        else:
            print("Invalid choice. Please select a valid option.")









main()
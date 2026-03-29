"""
Lab 10: Word Analyzer
Author: Ben Garcia

Displays a menu of 4 predefined text files,
lets the user select one, reads and analyzes the file.
It will count the frequency of every word in the selected file and
print an alphabetical report.
"""
from pathlib import Path
import string

class WordAnalyzer:
    """Class to analyze a text file and count the frequency of each word.
    Attributes:
        _path (Path): A private attribute to store the file path as a Path object.
        _frequencies (dict): A private dictionary to store the frequency of each word.
    Methods:
        __init__(self, filepath=None): Initializes the WordAnalyzer class with a file path.
        process_file(self, filepath): Reads the specified text file, counts the frequency of each word while ignoring stop words, and stores the counts in a dictionary. Returns True if the file was processed successfully, or False if there was an error (e.g., file not found).
        print_report(self): Sorts words alphabetically and prints the frequency of each word.
    """
    def __init__(self, filepath=None):
        """init method to initialize the WordAnalyzer class
        Will take the filepath to the text file as a string and store it as a private pathlib
        """
        self._path = Path(filepath) 
        self._frequencies = {}  

       
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
            
            translator = str.maketrans('', '', string.punctuation + '“”‘’•')  # Create a translator to remove punctuation
            
            with self._path.open('r', encoding='utf-8-sig') as file:
                for line in file:
                    #Remove punctuation using translator, convert to lowercase, and replace hyphens/dashes with spaces
                    clean_line = line.translate(translator).lower()
                    clean_line = clean_line.replace('-', ' ')
                    clean_line = clean_line.replace('—', ' ')
                    clean_line = clean_line.replace('–', ' ')

                    words = clean_line.split()  

                    #iterate through split words and count frequencies, if first instance of word add, otherwise increment count
                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1
            return True
        #throw exception if file is not found and print error message, return false to indicate failure
        except FileNotFoundError as err:
            print(f"File not found: {err}")
            return False
       
        
    def print_report(self):
        """Sort words alphabetically with sorted() and print the frequency of each word
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

      Excecution steps:
        1. Display a menu of predefined text files and an option to exit
        2. Prompt the user to enter their choice
        3. Validate the user's choice and either exit, process the selected file, or display an error message for invalid input
        4. If a valid file is selected, create an instance of the WordAnalyzer class, call the process_file method, and print the report if processing was successful
        5. Repeat the menu until the user chooses to exit
    """
    file_options = {
        '1': 'monte_cristo.txt',
        '2': 'princess_mars.txt',
        '3': 'Tarzan.txt',
        '4': 'treasure_island.txt'
    }
    # Display the menu and prompt the user for input until they choose to exit
    print("--- Word Analyzer ---")
    while True:
        print("\nSelect a file to analyze:")
        print("1. monte_cristo.txt")
        print("2. princess_mars.txt")
        print("3. Tarzan.txt")
        print("4. treasure_island.txt")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        if choice == '5':
            print("Goodbye!")
            break
        # Validate the user's choice and process the selected file if valid, otherwise display an error message
        elif choice in file_options:
            analyzer = WordAnalyzer(filepath=file_options[choice])
            if analyzer.process_file(file_options[choice]):
                print(f"\nWord frequency report for {file_options[choice]}:")
                analyzer.print_report()
            else:
                print("Failed to process the file.")
        else:
            print("Invalid choice. Please select a valid option.")


#excecute the main function when the script is run
if __name__ == "__main__":
    main()



import os
import re
import sys
from nltk.corpus import stopwords
import nltk

# Get the parent directory of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from apps import CSR_REPORT_DIRECTORY

class Pre_Processing:
    def __init__(self):
        pass

    def clean_csr_text(self, text):
        """
            Cleans the CSR text by removing numbers, symbols, and converting it to lowercase.
        """
        # Remove punctuation and special characters except spaces
        text = re.sub(r'[^\w\s]', '', text)
        
        # Remove numbers
        text = re.sub(r'\d+', '', text)

        # Convert text to lowercase
        text = text.lower()

        return text

    def remove_symbols_from_file(self, filepath=CSR_REPORT_DIRECTORY):
        """
            Reads a file, cleans its text, and overwrites it.
        """
        status = False
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()

            cleaned_text = self.clean_csr_text(text)

            with open(filepath, 'w', encoding='utf-8') as f:  # Overwrite the file
                f.write(cleaned_text)
            print(f"Cleaned text from: {filepath}")
            status = True

        except UnicodeDecodeError:
            print(f"Unicode decode error for {filepath}. Consider investigating/fixing encoding.")
        except Exception as e:
            print(f"An error occurred with file {filepath}: {e}")
        finally:
            return status

    def process_directory(self, directory=CSR_REPORT_DIRECTORY):
        """
            Processes all .txt files in a directory to clean CSR reports.
        """
        status = False

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)
                status = self.remove_symbols_from_file(filepath)
        return status
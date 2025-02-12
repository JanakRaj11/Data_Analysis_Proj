import os
import re
import sys

# get the parent directory of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from apps import BASE_DIRECTORY

def remove_symbols_from_file(filepath):
    """Removes punctuation and symbols from a text file and overwrites the file.

    Args:
        filepath: The path to the text file.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()

        cleaned_text = re.sub(r'[^\w\s]', '', text)  # Remove all but alphanumeric and whitespace

        with open(filepath, 'w', encoding='utf-8') as f:  # Overwrite the file
            f.write(cleaned_text)
        print(f"Cleaned symbols from: {filepath}")

    except UnicodeDecodeError:
        print(f"Unicode decode error for {filepath}. Consider investigating/fixing encoding.")
    except Exception as e:
        print(f"An error occurred with file {filepath}: {e}")


def process_directory(directory):
    """Processes all .txt files in a directory to remove symbols.

    Args:
        directory: The path to the directory containing the .txt files.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)
            remove_symbols_from_file(filepath)


# Example usage:
directory_path = f"{BASE_DIRECTORY}"  # Replace with the actual path
process_directory(directory_path)

print("Finished processing files.")
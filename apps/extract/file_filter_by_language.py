import os
import sys

# get the parent directory of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from apps import CSR_REPORT_DIRECTORY

from langdetect import detect, LangDetectException

class Lanuage_Detector:
    def __init__(self):
        pass

    def detect_and_filter_english_txt(self, directory=CSR_REPORT_DIRECTORY):
        """
            Detects the language of .txt files in a directory and removes non-English files.
        """

        status = False

        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                print("*"*100)
                print(f"Language detection started for {filename}")
                filepath = os.path.join(directory, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:  # Handle potential encoding issues
                        text = f.read()
                        if text.strip():  # Check if the file is not empty or contains only whitespace
                            language = detect(text)
                            if language != 'en':
                                os.remove(filepath)
                                print(f"Removed non-English file: {filename}")
                        else:
                            print(f"File {filename} is empty or contains only whitespace.  Deleting...")
                            os.remove(filepath)

                except LangDetectException:
                    print(f"Language detection failed for {filename}.")
                    user_input = input("Do you want to delete it? (Y/n)")
                    if (user_input.lower() == "y") or (user_input.lower() ==  "yes"):
                        os.remove(filepath)
                        print(f"Deleted {filename}")

                except UnicodeDecodeError:
                    print(f"Unicode decode error for {filename}. Consider investigating/fixing encoding.")
                except Exception as e: # Catching other potential exceptions
                    status = False
                    print(f"An error occurred with file {filename}: {e}")
                finally:
                    print(f"Language detection completed for {filename}. Please manually check if there is any detection error in log.")
                    print("*"*100)
                    print("\n")
                    status = True
        return status
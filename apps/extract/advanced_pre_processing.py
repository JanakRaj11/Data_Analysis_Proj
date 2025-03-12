import os
import re
import sys
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# get the parent directory of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from apps import CSR_REPORT_DIRECTORY

class Advanced_Pre_Processing:
    def __init__(self):
        # Initialize stopwords and lemmatizer
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess_text(self, text):
        """
            Cleans and preprocesses CSR report text.
        """
        
        # Lowercasing
        text = text.lower()

        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # Tokenize text (split into words)
        words = text.split()

        # Remove stopwords
        words = [word for word in words if word not in self.stop_words]

        # Lemmatization (convert words to their base form)
        words = [self.lemmatizer.lemmatize(word) for word in words]
        
        # Join words back into a clean sentence
        return " ".join(words)

    def process_csr_reports(self, directory=CSR_REPORT_DIRECTORY):
        """
            Processes all CSR text files in a directory.
        """

        status = False

        # Download necessary NLTK resources (run once)
        nltk.download('stopwords')
        
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):  # Only process text files
                filepath = os.path.join(directory, filename)

                try:
                    with open(filepath, 'r', encoding='utf-8') as file:
                        text = file.read()

                    # Preprocess text
                    cleaned_text = self.preprocess_text(text)

                    # Save the cleaned text (overwrite original file or save separately)
                    with open(filepath, 'w', encoding='utf-8') as outfile:
                        outfile.write(cleaned_text)

                    print(f"Processed: {filename}")
                    status = True

                except Exception as e:
                    status = False
                    print(f"Error processing {filename}: {e}")
            return status
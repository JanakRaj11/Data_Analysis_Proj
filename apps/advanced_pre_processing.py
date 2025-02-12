import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK resources (run once)
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize stopwords and lemmatizer
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    """Cleans and preprocesses CSR report text."""
    
    # Lowercasing
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Tokenize text (split into words)
    words = text.split()

    # Remove stopwords
    words = [word for word in words if word not in stop_words]

    # Lemmatization (convert words to their base form)
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join words back into a clean sentence
    return " ".join(words)

def process_csr_reports(directory):
    """Processes all CSR text files in a directory."""
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):  # Only process text files
            filepath = os.path.join(directory, filename)

            try:
                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()

                # Preprocess text
                cleaned_text = preprocess_text(text)

                # Save the cleaned text (overwrite original file or save separately)
                with open(filepath, 'w', encoding='utf-8') as outfile:
                    outfile.write(cleaned_text)

                print(f"Processed: {filename}")

            except Exception as e:
                print(f"Error processing {filename}: {e}")

# Example: Process all reports in the "CSR_Reports" folder
process_csr_reports("/path/to/CSR_Reports")
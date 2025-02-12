
# ==============================================================
# Check carbon emmision is mentioned in the report or not
# ==============================================================

import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

def find_carbon_commitments(directory):
    """Search for carbon emission commitments in CSR reports."""
    
    keywords = ["carbon emission", "net zero", "carbon neutrality", "scope 1", "scope 2", "scope 3", "2030 target"]
    
    results = {}

    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()

            # Check if any keyword is in the text
            found_keywords = [kw for kw in keywords if kw in text]
            
            if found_keywords:
                results[filename] = found_keywords

    return results

# Example Usage
carbon_reports = find_carbon_commitments("/path/to/CSR_Reports")
for report, keywords in carbon_reports.items():
    print(f"{report}: Found Keywords -> {keywords}")
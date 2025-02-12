import os
import sys
import pandas as pd

# get the parent directory of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from apps import BASE_DIRECTORY

# List to store report details
report_data = []

def extract_report_info(directory):
    """Extract key information from CSR reports."""
    keywords = ["carbon emission", "carbon dioxide emissions", "net zero", "carbon neutrality", "scope 1", "scope 2", "scope 3", "2030 target"]
    
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory, filename)

            with open(filepath, 'r', encoding='utf-8') as file:
                text = file.read()

            # Extract relevant information
            relevant_info = {
                "company_name": filename.replace(".txt", ""),  # Extract company name
                "carbon_commitments": [kw for kw in keywords if kw in text],
                "report_year": "2025",  # This should be extracted based on the report or filename
                "industry": "Oil & Gas"  # Extract or manually categorize by industry
            }

            report_data.append(relevant_info)

    # Convert to DataFrame for easy analysis
    df = pd.DataFrame(report_data)
    return df

# Example Usage
df_reports = extract_report_info("/path/to/CSR_Reports")
print(df_reports.head())

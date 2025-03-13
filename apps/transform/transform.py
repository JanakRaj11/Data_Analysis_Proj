import datetime
import os
import sys
import pandas as pd

# get the parent directory of the project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from apps import CSR_REPORT_DIRECTORY, REPORT_OUTPUT_DIRECTORY

class Transform:
    def __init__(self):
        pass

    def extract_report_info(self, directory=CSR_REPORT_DIRECTORY):
        """
            Extract key information from CSR reports.
        """
        # List to store report details
        report_data = []
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                filepath = os.path.join(directory, filename)

                with open(filepath, 'r', encoding='utf-8') as file:
                    text = file.read()
                # get the report year
                splitted_filename = filename.split("_")[-1]
                year = splitted_filename.split(".")[0]
                # Extract relevant information
                relevant_info = {
                                    "CompanyName": filename.replace(".txt", ""),
                                    "ReportYear": str(year),  # Ensure year is a string for consistency
                                    "ReportText": text
                                }
                report_data.append(relevant_info)
            else:
                print("File format issue: file is not in .txt format.")

        # Convert to DataFrame for easy analysis
        df = pd.DataFrame(report_data)
        return df
    
    def tranform_csr_data(self):
        """""
            Tranform CSR report and create pre-processed CSV file for analysis.
        """
        status = False
        
        print("Starting transformation process...")

        df_reports = self.extract_report_info()

        if not df_reports.empty:
            report_file_name = f"Report_Outcome.csv"
            report_file_path = f"{REPORT_OUTPUT_DIRECTORY}/{report_file_name}"
            df_reports.to_csv(path_or_buf=report_file_path, mode="w+")
            print(df_reports.count())
            status = True
            print("Tranformation completed.")
        else:
            print("Error occured while transforming CSR data.")
        return status
    
# Transform().tranform_csr_data()
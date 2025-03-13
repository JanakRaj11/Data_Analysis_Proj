import sys
import time
from apps.transform.transform import Transform as transform
from apps.extract.pre_processing import Pre_Processing as pre_processor
from apps.extract.file_filter_by_language import Lanuage_Detector as lng_detector
from apps.extract.advanced_pre_processing import Advanced_Pre_Processing as advance_processor

def extract_service():
    """""
        Extract the CSR reports from the source location
        Filter the files with English language only
    """
    status = False

    lng_detect_status = lng_detector().detect_and_filter_english_txt()
    if lng_detect_status:
        status = lng_detect_status

        pre_process_status = pre_processor().process_directory()
        status = pre_process_status
        if pre_process_status:
            advanced_pre_process_status = advance_processor().process_csr_reports()
            status = advanced_pre_process_status
    return status

def transform_service():
    """""
        Perform Stop words removal & Lemmatization to clean and transform the CSR reports
         so that we get the pre-processed CSV file for analysis
    """
    status = False

    transform_status = transform().tranform_csr_data()
    if transform_status:
        status = True
    return status

def main():
    """
        Main function to perform CSR report analysis.
        
        The process consists of:
        1. Extracting CSR reports.
        2. Filtering non-English files.
        3. Pre-processing and transforming the extracted data.

        If extraction fails, the script terminates without proceeding to transformation.
        If transformation fails, the script logs an error and exits.
    """
    print("*" * 200)
    print("CSR Report Analysis Started...")

    print("Extraction of the CSR reports started...")
    
    if not extract_service():
        print("Error: Extraction failed. Please check the logs for details.")
        sys.exit(1)

    print("Extraction completed.")
    time.sleep(1)
    
    print("Filtering English-language files completed.")
    time.sleep(1)

    print("Pre-processing and transformation started...")
    
    if not transform_service():
        print("Error: Transformation failed. Please check the logs for details.")
        sys.exit(1)

    print("Pre-processing and transformation completed.")
    print("Analysis of the CSR reports completed.")
    print("*" * 200)

if __name__ == "__main__":
    main()
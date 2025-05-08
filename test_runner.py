#testing

from geomodule.io_utils import load_csv, load_json, save_json
from geomodule.matcher import match_closest_points

import os
from datetime import datetime


# Utility Function to Run One Test
def run_test(file1: str, file2: str, filetype: str = "csv"):
   
    """
    Run a match test between two files and save output with timestamp.
    
    Args:
        file1: Path to first file (dataset A)
        file2: Path to second file (dataset B)
        filetype: 'csv' or 'json'
    """
    
    print(f"\n▶️ Running test for: {file1} vs {file2} [{filetype.upper()}]")

    # Load data from CSV or JSON
    if filetype == "csv":
        arr1 = load_csv(file1)
        arr2 = load_csv(file2)
    elif filetype == "json":
        arr1 = load_json(file1)
        arr2 = load_json(file2)
    else:
        print("❌ Unsupported file type. Use 'csv' or 'json'.")
        return

    # Run matching
    results = match_closest_points(arr1, arr2)

    # Generate unique output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"test_cases/output_{timestamp}.json"

    # Save output
    save_json(results, os.path.basename(file1), os.path.basename(file2), output_file)


# Main Runner
if __name__ == "__main__":
    print("\n📦 Batch Testing GeoModule with Sample Files")

    # Example test files — you can change or expand this list
    test_configs = [
    ("test_cases/world_cities.csv", "test_cases/iata_airports.csv", "csv")
    ]


    # Run each configured test
    for fileA, fileB, ftype in test_configs:
        if os.path.exists(fileA) and os.path.exists(fileB):
            run_test(fileA, fileB, ftype)
        else:
            print(f"⚠️ Skipping: One of the files does not exist → {fileA}, {fileB}")

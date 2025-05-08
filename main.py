from geomodule.io_utils import load_csv, load_json, manual_input, save_json
from geomodule.matcher import match_closest_points

import os


def main():
    
    """
    Command-line interface for running the GeoModule matcher.
    Allows selection of input methods and saves result as JSON.
    """
    #welcome message
    print("\n🌍 GeoModule: Match Closest GPS Points")
    print("======================================")

    # Step 1: Let user choose input method
    print("\nChoose how to load your two input datasets:")
    print("1️⃣  Load from CSV files")
    print("2️⃣  Load from JSON files")
    print("3️⃣  Enter coordinates manually")

    choice = input("Enter your choice (1/2/3): ").strip()

    #prepare variables for data and lables
    arr1 = []
    arr2 = []
    label1 = ""
    label2 = ""

    #load from csv files
    if choice == "1":
        file1 = input("Path to first CSV file: ").strip()
        file2 = input("Path to second CSV file: ").strip()

        # Check if files exist before loading
        if not os.path.exists(file1) or not os.path.exists(file2):
            print("❌ One or both CSV files not found.")
            return

        arr1 = load_csv(file1)
        arr2 = load_csv(file2)
        label1 = os.path.basename(file1)
        label2 = os.path.basename(file2)

    #load from json files
    elif choice == "2":
        file1 = input("Path to first JSON file: ").strip()
        file2 = input("Path to second JSON file: ").strip()

        if not os.path.exists(file1) or not os.path.exists(file2):
            print("❌ One or both JSON files not found.")
            return

        arr1 = load_json(file1)
        arr2 = load_json(file2)
        label1 = os.path.basename(file1)
        label2 = os.path.basename(file2)

    #load from manual entry
    elif choice == "3":
        print("\n➡️ Enter coordinates for the FIRST dataset:")
        arr1 = manual_input()

        print("\n➡️ Enter coordinates for the SECOND dataset:")
        arr2 = manual_input()

        label1 = "Manual_Input_A"
        label2 = "Manual_Input_B"

    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
        return

    # Step 2: Perform matching
    print("\n🔍 Matching points...")
    results = match_closest_points(arr1, arr2)

    # Step 3: Save output
    save_json(results, source_a=label1, source_b=label2)


if __name__ == "__main__":
    main()

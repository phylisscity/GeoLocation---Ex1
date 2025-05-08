import csv
import json
from typing import List, Tuple
from datetime import datetime

#type alias to represent coordinates as lat,lon
Coordinate = Tuple[float, float]


#load data from csv
def load_csv(filepath: str) -> List[Coordinate]:
    
    """
    Load coordinates from a CSV file. 
    Automatically detects latitude/longitude columns.
    returns list of lat,lon tuples.
    """
    
    coords = []
    
    #open csv
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  #read rows as dictionaries
        
        for row in reader:
            
            try:
                #automatically detect which columns are lat and lon
                lat_key = next((k for k in row if "lat" in k.lower()), None)
                lon_key = next((k for k in row if "lon" in k.lower() or "lng" in k.lower()), None)

                #skip rows that dont have both
                if not lat_key or not lon_key:
                    continue
                
                #convert vals to float and add to list
                lat = float(row[lat_key])
                lon = float(row[lon_key])
                coords.append((lat, lon))
            except (ValueError, KeyError):
                #skip rows with invalid data
                continue
            
    return coords

#load data from json
def load_json(filepath: str) -> List[Coordinate]:
    
    """
    Load coordinates from a JSON file. 
    Looks for 'lat'/'lon' or similar keys in each object.
    accepts keys like lat, lon, latitude, longitude, etc
    
    returns list of lat,lon tuples
    """
    
    coords = []
    
    #open and parse json
    with open(filepath, mode='r', encoding='utf-8') as file:
        data = json.load(file)
        
        for item in data:
            #try common variations of lat and lon key names
            try:
                lat = item.get("lat") or item.get("latitude")
                lon = item.get("lon") or item.get("lng") or item.get("longitude")
                
                #add to list if both vals present
                if lat is not None and lon is not None:
                    coords.append((float(lat), float(lon)))
            except (ValueError, KeyError, TypeError):
                continue #skip rows with invalid data
            
    return coords


#manual entry
def manual_input() -> List[Coordinate]:
    
    """
    Allows a user to enter coordinates manually from CLI.
    returns list of lat,lon tuples.
    """
    
    coords = []
    
    print("\n🔹 Enter coordinates manually (type 'done' to finish):")
    
    while True:
        
        try:
            #prompt for lat or exit
            lat = input("Latitude (or 'done'): ").strip()
            if lat.lower() == 'done':
                break
            
            #prompt for lon
            lon = input("Longitude: ").strip()
            #convert to float and store
            coords.append((float(lat), float(lon)))
        except ValueError:
            print("❌ Invalid input. Try again.")
            
    return coords

#save results to json file
def save_json(
    matches: List[Tuple[Coordinate, Coordinate, float]],
    source_a: str,
    source_b: str,
    output_file: str = "output.json"
):
    """
    Saves the matched coordinate results as a JSON file, including metadata like:
    - Timestamp
    - Data source descriptions
    - Matched points and distances

    Arguments:
        matches: List of tuples in the form (pointA, pointB, distance)
        source_a: Description or label for dataset A
        source_b: Description or label for dataset B
        output_file: Filename to save output to (default: 'output.json')
    """
    structured = {
        "timestamp": datetime.utcnow().isoformat() + "Z",  # UTC timestamp for reference
        "source_A": source_a,
        "source_B": source_b,
        "results": []
    }

    # Format each match into a clean dictionary
    for pointA, pointB, dist in matches:
        structured["results"].append({
            "from": {"lat": pointA[0], "lon": pointA[1]},
            "to": {"lat": pointB[0], "lon": pointB[1]},
            "distance_km": dist
        })

    # Save to file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=4)

    print(f"✅ Results saved to {output_file}")
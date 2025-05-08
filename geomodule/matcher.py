import math
from typing import List, Tuple


# Type alias for clarity
Coordinate = Tuple[float, float]


#haversine distance
def haversine(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
   
    """
    Calculate the great-circle distance between two geographic coordinates using the Haversine formula.

    Returns distance in kilometers.
    """
    
    R = 6371  # Earth's radius in km

    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

    # Haversine computation
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    #formula
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c


#find closest point
def find_closest_point(point: Coordinate, reference_points: List[Coordinate]) -> Tuple[Coordinate, float]:
  
    """
    Find the closest point in reference_points to the given point.
    Returns the closest coordinate and the distance in kilometers.
    """
    
    lat1, lon1 = point
    
    # Find the reference point that gives the minimum Haversine distance
    closest = min(reference_points, key=lambda ref: haversine(lat1, lon1, ref[0], ref[1]))
    
    # Compute the actual distance to that closest point
    distance = round(haversine(lat1, lon1, closest[0], closest[1]), 2)
    return closest, distance


#match all points from array a to closest in array b
def match_closest_points(array1: List[Coordinate], array2: List[Coordinate]) -> List[Tuple[Coordinate, Coordinate, float]]:
    
    """
    For each point in array1, find the closest point in array2.
    Returns a list of tuples: (point_from_array1, closest_point_from_array2, distance).
    """
    
    matches = []
    
    #process each point in array1
    for point in array1:
        
        closest, distance = find_closest_point(point, array2)
        matches.append((point, closest, distance))
        
    return matches

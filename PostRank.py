import pandas as pd
import numpy as np
import requests

def get_lat_lng(address, api_key):
    url = 'https://api.opencagedata.com/geocode/v1/json'
    params = {
        'q': address,
        'key': api_key
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            lat_lng = data['results'][0]['geometry']
            return lat_lng['lat'], lat_lng['lng']
        else:
            return None, None
    else:
        print(f"Error: {response.status_code}")
        return None, None

api_key = ''  

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    lat1, lon1, lat2, lon2 = map(np.radians, [lat1, lon1, lat2, lon2])
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  
    return c * r

def find_nearby_locations(df, target_lat, target_lon, threshold_km):
    """
    Returns nearby locations within a certain threshold (in km) from the target latitude and longitude.

    Parameters:
    df (DataFrame): DataFrame containing 'Latitude' and 'Longitude' columns.
    target_lat (float): Target latitude.
    target_lon (float): Target longitude.
    threshold_km (float): Distance threshold in kilometers.

    Returns:
    DataFrame: A DataFrame with rows within the specified distance from the target location.
    """
    distances = df.apply(lambda row: haversine(target_lat, target_lon, row['Latitude'], row['Longitude']), axis=1)
    nearby_df = df[distances <= threshold_km].copy()
    nearby_df['Distance_km'] = distances[distances <= threshold_km]
    
    return nearby_df



ALL_2024 = pd.read_csv("2024_Aug.csv", encoding='unicode_escape')
ALL_2024['Latitude'] = pd.to_numeric(ALL_2024['Latitude'], errors='coerce')
ALL_2024['Longitude'] = pd.to_numeric(ALL_2024['Longitude'], errors='coerce')
VALID_2024 = ALL_2024[((ALL_2024['Latitude'].between(-90, 90)) & (ALL_2024['Longitude'].between(-180, 180)))] 

# STEP 1 : Read the address and clean it as required
cus_end_point = "Amarajyothi Hospital, Kamalapur Road, Dharwad, Karnataka" 


# Step 2 : Get Latitude and Logitude
lat, lng = get_lat_lng(cus_end_point, api_key)

if lat and lng:
    print(f"Latitude: {lat}, Longitude: {lng}")
    print(f"https://www.google.com/maps?q={lat},{lng}")
else:
    print("Address not found.")

# Step 3 : Find Nearby Postoffice Delivery Hubs

tol = 10 # Kilometer Radius
Query = find_nearby_locations(VALID_2024, lat, lng, 10).sort_values(by="Distance_km").head(10)

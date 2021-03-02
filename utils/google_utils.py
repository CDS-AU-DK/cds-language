#!/usr/bin/bash

# Functions to work with Google maps client data
def get_placeid(string, api_client):
    '''Takes a string and an established googlemaps places API client.
       Returns first place_id associated with that string.
       If no place_id found, returns None.'''
    try:
        place = api_client.places(string)
        status = place['status']
        if status == 'OK':
            place_id = place['results'][0]['place_id']
        elif status == 'ZERO_RESULTS':
            place_id = None
        else:
            place_id = None
    except:
        place_id = None
    return place_id

def process_id(placeid, api_client):
    '''Takes a Google place_id and an established googlemaps geocoding API client.
        Looks up and parses geo data for placeid.
        Returns int code on error, else dictionary of geo data.
    '''
    # Define all variables, initial to None
    result = {
    'formatted_address' : None,
    'location_type' : None,
    'country' : None,
    'admin_1' : None,
    'admin_2' : None,
    'locality' : None,
    'lat' : None,
    'lon' : None,
    'partial' : None,
    }
    # Perform reverse geocode.
    try:
        data = gc_client.reverse_geocode(placeid)
    except:
        return 1 # Problem with geocoding API call
    
    # Use the first result. Should only be one when reverse geocoding with place_id.
    try:
        data = data[0]
        result['formatted_address'] = data['formatted_address']
        result['location_type'] = data['types'][0]
        result['lat'] = data['geometry']['location']['lat']
        result['lon'] = data['geometry']['location']['lng']
        try:
            result['partial'] = result['partial_match']
        except:
            result['partial'] = False
    except:
        print("   Bad geocode for place_id %s" % (placeid))
        return 2 # Problem with basic geocode result
    
    try:
        for addr_comp in data['address_components']:
            comp_type = addr_comp['types'][0]
            if comp_type == 'locality':
                result['locality'] = addr_comp['long_name']
            elif comp_type == 'country':
                result['country'] = addr_comp['long_name']
            elif comp_type == 'administrative_area_level_1':
                result['admin_1'] = addr_comp['long_name']
            elif comp_type == 'administrative_area_level_2':
                result['admin_2'] = addr_comp['long_name']
    except:
        return 3 # Problem with address components
    
    return result

if __name__=="__main__":
    pass
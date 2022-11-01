import os
import requests
import json

from dotenv import load_dotenv
import pandas as pd


def return_money(value):
    """ input: a string containing the money rised by a company
        output: a float with the money properly formated turning M to milions and B to billions
    """
    if value.startswith("$") or value.startswith("€"):
        if value.endswith("k"):
            return round(float(value[1:-1])*100)
        elif value.endswith("M"):
            return round(float(value[1:-1])*100000)
        elif value.endswith("B"):
            return round(float(value[1:-1])*100000000)
        else:
            return 0


def get_distance (latitude, longitude, query="", category="", limit=1):
    """ 
        inputs: latitude to search around.
                longitude to search around.
                *optional* query: a kind of place to search for.
                *optional* category: a foursquare category to search for.
                *optional* limit: limit of results to return, 1 by default.
                
        output: An integer, the distance to the closest location of the kind searched for.
                Note: If no location is found it returns 10000.
    """
    
    if query != "":
        query = f"query={query}&"
    
    if category != "":
        category = f"&categories={category}"
        
    # Doing the call for foursquare     
    ll = f"{latitude}%2C{longitude}"
    url = f"https://api.foursquare.com/v3/places/search?{query}ll={ll}{category}&sort=DISTANCE&limit={str(limit)}"

    headers = {
        "accept": "application/json",
        "Authorization": token_fsq,
    }
    
    response = requests.get(url, headers=headers).json()
    
    if response["results"] == []:
        return 10000
    else:
        return int(response["results"][0]["distance"])


def add_distance_column(dataframe, new_column, query="", category=""):
    """
        inputs: A DataFrame to append the new column with distance.
                The name of the new column.
                *optional* query: a kind of place to search for.
                *optional* category: a foursquare category to search for.
                
        output: The DataFrame with a new column including the distance to the nearest place found.
        returns None
    """
    distances_list = []
    
    for index, row in dataframe.iterrows():
        distances_list.append(get_distance(row["latitude"], row["longitude"], query=query, category=category))
        
    dataframe[f"{new_column}"] = distances_list
    
    return None


def add_normalized_column(dataframe, column_name):
    """
        inputs: a DataFrame
                a column with distances to be normalized
                
        output: the DataFrame with the distances normalized.
        
        *returns None
    """
    
    normalized_distances_list = []
    
    max_in_column =  dataframe[f"{column_name}"].max()
    
    for index, row in dataframe.iterrows():
        normalized_distances_list.append(row[f"{column_name}"]/max_in_column)
        
    dataframe[f"{column_name}_normalized"] = normalized_distances_list
    
    return None


def calculate_proximity_index(dataframe):
    """
        input: a DataFrame with distances to different locations.
        output: the DataFrame including the proximity index as a new column
    """
    proximity_index = (
        0.25 * dataframe.school_distance_normalized +
        0.10 * dataframe.airport_distance_normalized +
        0.25 * dataframe.train_distance_normalized +
        0.20 * dataframe.club_distance_normalized +
        0.1 * dataframe.vegan_distance_normalized +
        0.05 * dataframe.stadium_distance_normalized +
        0.05 * dataframe.pet_groomer_distance_normalized
    )
    
    return round(100 - proximity_index*100, 2)
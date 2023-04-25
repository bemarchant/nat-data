import json
import requests
from constants import *

def get_observations_by_project_id(project_id):
    query = {'project_id' : project_id, "per_page" : 'all'}
    data = requests.get(api_url + "observations", params = query)
    return data.json()

def get_observations_by_user_id(user_id):
    query = {'user_id' : user_id}
    data = requests.get(api_url + "observations", params = query)
    return data.json()

def get_observations(query):
    data = requests.get(api_url + "observations", params = query)
    return data.json()

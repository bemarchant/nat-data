import requests
import json
import plots as plt
from datetime import datetime

from constants import *

def is_in_project(obs, month_number):
    months_2022 = [10,11,12]
    months_2023 = [1,2,3,4]

    date_str = obs['observed_on_details']['date']
    date_format = '%Y-%m-%d'

    date_obj = datetime.strptime(date_str, date_format)

    if date_obj is not None and date_obj.month == month_number and date_obj.month in months_2022 and date_obj.year == 2022:
        return True
    if date_obj is not None and date_obj.month == month_number and date_obj.month in months_2023 and date_obj.year == 2023:
        return True
    return False

def is_in_month(obs, month_number):
    date_str = obs['observed_on_details']['date']
    date_format = '%Y-%m-%d'

    date_obj = datetime.strptime(date_str, date_format)
    if date_obj.month == month_number:
        return True
    return False

def is_geoprivacy_obscure(obs):
    if obs['taxon_geoprivacy'] == 'obscure':
        return True
    return False
def is_geoprivacy_open(obs):
    if obs['taxon_geoprivacyc'] == 'open':
        return True
    return False
def is_geoprivacy_private(obs):
    if obs['taxon_geoprivacy'] == 'private':
        return True
    return False

def is_in_taxa(obs, taxon_id):
    if obs['taxon'] is None: 
        return False
    return taxon_id in obs['taxon']['ancestor_ids']

def is_research_quality(obs):
    if obs['quality_grade'] == 'research': 
        return True
    return False
def is_needs_id_quality(obs):
    if obs['quality_grade'] == 'needs_id': 
        return True
    return False
def is_casual_quality(obs):
    if obs['quality_grade'] == 'casual': 
        return True
    return False

def get_observations(query):
    data = requests.get(api_url + "observations", params = query)
    return data.json()

# data = get_observations(query)

# for page in range(2,7):
#     query['page'] = page
#     data_page = get_observations(query)
#     data['results'] += data_page['results']

# with open("data", "w") as fp:
#     json.dump(data,fp)

with open("data","r+") as data_json:
    data=json.load(data_json)

#Plot a histogram
#print(data['total_results'])
# for t in taxa:
#     t['needs_id'] = len([obs for obs in data['results'] if is_needs_id_quality(obs) and is_in_taxa(obs, t['taxon_id'])])
#     t['research_grade'] = len([obs for obs in data['results'] if is_research_quality(obs) and is_in_taxa(obs, t['taxon_id'])])
#     t['casual'] = len([obs for obs in data['results'] if is_casual_quality(obs) and is_in_taxa(obs, t['taxon_id'])])
#     t['observations'] = t['needs_id'] + t['research_grade'] + t['casual'] 
#     print("###########")
#     print(f"needs_id :  {t['needs_id']}")
#     print(f"research_grade :  {t['research_grade']}")
#     print(f"casual :  {t['casual']}")
#     print(f"observations :  {t['observations']}")

# plt.plot_histogram()
#end plot

taxa = 47170
obs = [obs for obs in data['results'] if is_in_taxa(obs, taxa)] 
print(f"all : {len(obs)}")

obs = [obs for obs in data['results'] if is_research_quality(obs) and is_in_taxa(obs, taxa)] 
print(f"is_research_quality : {len(obs)}")

obs = [obs for obs in data['results'] if is_needs_id_quality(obs) and is_in_taxa(obs, taxa)] 
print(f"is_needs_id_quality : {len(obs)}")

obs = [obs for obs in data['results'] if is_casual_quality(obs) and is_in_taxa(obs, taxa)] 
print(f"is_casual_quality : {len(obs)}")

#get number of species inside taxonomy
obs = [obs for obs in data['results'] if is_in_taxa(obs, taxa) and is_research_quality(obs)] 
species_list = [o['taxon']['name'] for o in obs if is_research_quality(o)]
species_set = set(species_list)
species_count = [species_list.count(s) for s in species_set]
print(species_set)
print(species_count)
print(len(species_set))

# print(f"species : {len(species)}")

#Get all observations
# obs = [obs for obs in data['results']]

# for ob in obs:
#     geoprivacy = ob['taxon_geoprivacy']
    
#     try:
#         name =  ob['taxon']['name']
#     except:
#         name = "???"

#     try:
#         date = ob['observed_on_details']['date']
#     except:
#         date = "???"

#     loc = ob['location']
#     id = ob['id']
#     qualitygrade = ob['quality_grade']

#     print(f"{name}, {loc}, {date}, {id}, {geoprivacy}, {qualitygrade}")

# get all observations by month
# for month in range(1,13):
#     print (f"month: {month} -- {len([ob for ob in obs if is_in_month(ob,month)])}")


# get all observations tagged in the project El Manzano
# obs = [obs for obs in data['results'] if is_needs_id_quality(obs) or is_research_quality] 
# print(f"all : {len(obs)}")

# for month in range(1,13):
#      print (f"month: {month} -- {len([ob for ob in obs if is_in_month(ob, month)])}")
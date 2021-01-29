#%%
import json
import requests
import pandas as pd
import numpy as np
from pprint import pprint
# %%
spacex = requests.get('https://api.spacexdata.com/v3/capsules')
spacex_df = pd.DataFrame(spacex.json())


# %%
connURL = "https://api.spacexdata.com/v3/capsules"
response = requests.get(connURL).json()
for launch in np.arange(0, len(response)):
    capsule = response[launch]["capsule_id"]
    details = response[launch]["details"]
    date = response[launch]["original_launch"]
    print(f"{capsule} - {details} launched on {date}.")
# %%
base = "https://api.spacexdata.com/v3/launchpads"
siteID = '/vafb_slc_3w'
# %%
queryUrl = f'{base}{siteID}'
response = requests.get(queryUrl)
response = response.json()
pprint(response)
# %%

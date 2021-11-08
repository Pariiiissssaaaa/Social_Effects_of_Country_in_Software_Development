from library import *
import json
import urllib.request as urllib2
import pandas as pd
from geopy.geocoders import Nominatim





user_pd=pd.read_pickle('user_pandas.pickle')
unique_loc=user_pd.user_location.value_counts()
user_w_loc=pd.read_pickle('user_w_loc.pickle')
new_loc=set(unique_loc.index).difference(set(user_w_loc['location'].drop_duplicates()))




geolocator = Nominatim()
country=defaultdict()

for i, loc in tqdm(enumerate(new_loc)):
    try:
        
        response = urllib2.urlopen('https://nominatim.openstreetmap.org/search?q='+ str(loc)+'&format=geojson')
        html = response.read()
        loc_coordinates=json.loads(html)['features'][0]['geometry']['coordinates']
        location = geolocator.reverse(str(loc_coordinates[1])+','+str(loc_coordinates[0]))
        country[loc]=location.raw['address']['country']

    except:
        country[loc]=None
    if (i>0 and i%1000==0):
        time.sleep(60)
        

f = open("loc2country_new.json","w")
f.write(json.dumps(country))
f.close()
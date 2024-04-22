#%%
import requests
r = requests.get('http://api.tvmaze.com/singlesearch/shows?q=big+bang+theory&embed=episodes')

#%%
contentsJSon = r.json()
len(contentsJSon["_embedded"]["episodes"])
#%%
contentsJSon = r.json()
contentsJSon["_embedded"]["episodes"][0]
# %%

import re
ldocs = []

for jo in contentsJSon["_embedded"]["episodes"][0:200]:
    d = {}
    d['id'] = jo['id']
    d['season'] = jo['season']
    d['episode'] = jo['number']
    d['name'] = jo['name']
    d["summary"] = re.sub('<[^<]+?>', '', jo['summary'])
    ldocs.append(d)
    
#%%
import json
import redis
from redis.commands.search.field import TextField, NumericField
from redis_services import connect_redis, create_index, index_documents

#Define variables
index_name = 'idx:bibbang' #the name of the index, which you will use when doing queries
doc_prefix = 'bibbang_episode:' #prefix for the document keys

# Define RediSearch fields
season = NumericField(name="season")
episode = NumericField(name="episode")
name = TextField(name="name")
summary = TextField(name="summary")

fields = [season, episode, name, summary]

r = connect_redis()
create_index(r, index_name, doc_prefix, fields)
index_documents(r, doc_prefix, ldocs)

# %%

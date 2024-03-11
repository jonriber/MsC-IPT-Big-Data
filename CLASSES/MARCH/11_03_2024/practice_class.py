#%% GOOGLE TOOLKIT

## installing dependencies

from googlesearch import search
import justext
import requests


#%% defining a function to get the text from a given url
def get_text(url):
    text=""
    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist("Portuguese"))
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            text+=paragraph.text
    return text

#%% searching for a query and getting the text from the first 10 results
query = "Jonatas Magno Tavares Ribeiro"
my_results_list = []

for url in search(query, tld="com", num=10, stop=10, pause=2):
    full_content = get_text(query)
    my_results_list.append({"fullCOntent": full_content, "url": url})
    print(f"URL: {url}")
    
print(my_results_list)

#%% API practice coding section

import requests
from requests.exceptions import Timeout

url_api = "https://arquivo.pt/textsearch"
query = "Antonio Costa"
payload = {"q": query}

try:
    response = requests.get(url_api, params=payload, timeout=50)
    response.raise_for_status()
except Timeout:
    print("The request timed out")
    
response["respose_items"][0]["title"]


#%% New York times API

## First thing to do is to create an account in the New York Times API website
## Then, we will get an API key to use in our requests


#%% NIF PORTUGUES API

import json
import requests
from requests.exceptions import Timeout

with open("local_envs.json", "r") as file:
    envs = json.load(file)

key = envs["nif_personal_key"]

print(key)

nif_target = "504665901"

api_url = f"http://www.nif.pt/?json=1"
payload = {"q": nif_target, "key": key}

try:
    response = requests.get(api_url, params=payload, timeout=50)
    response.raise_for_status()
except Timeout:
    print("The request timed out")

print(response.json())

# %% READING RESPONSES

content = response.json()
print(content)

# print(content["result"]["title"])

result = {
    "title": content["records"]["504665901"]["title"],
    "nif": content["records"]["504665901"]["nif"],
    "address": content["records"]["504665901"]["address"],
    "pc4": content["records"]["504665901"]["pc4"],
    "pc3": content["records"]["504665901"]["pc3"],
    "city": content["records"]["504665901"]["city"],
    "activity": content["records"]["504665901"]["activity"],
    "cae": content["records"]["504665901"]["cae"],
    "email": content["records"]["504665901"]["contacts"]["email"],
    "phone": content["records"]["504665901"]["contacts"]["phone"],
    "website": content["records"]["504665901"]["contacts"]["website"],
    "fax": content["records"]["504665901"]["contacts"]["fax"],
}

print("result: ", result)

#%% GETTING two NIFs from the API
list_of_nifs = ["504665901", "504665902"]
list_of_results = []

for nif in list_of_nifs:
    payload = {"q": nif, "key": key}
    try:
        response = requests.get(api_url, params=payload)
        content = response.json()
        result = {
            "title": content["records"][nif]["title"],
            "nif": content["records"][nif]["nif"],
            "address": content["records"][nif]["address"],
            "pc4": content["records"][nif]["pc4"],
            "pc3": content["records"][nif]["pc3"],
            "city": content["records"][nif]["city"],
            "activity": content["records"][nif]["activity"],
            "cae": content["records"][nif]["cae"],
            "email": content["records"][nif]["contacts"]["email"],
            "phone": content["records"][nif]["contacts"]["phone"],
            "website": content["records"][nif]["contacts"]["website"],
            "fax": content["records"][nif]["contacts"]["fax"],
        }
        list_of_results.append(result)
    except Timeout:
        print("The request timed out")

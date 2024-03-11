#%% GOOGLE TOOLKIT

## installing dependencies

from googlesearch import search
import justext
import requests


#%%
def get_text(url):
    text=""
    response = requests.get(url)
    paragraphs = justext.justext(response.content, justext.get_stoplist("Portuguese"))
    for paragraph in paragraphs:
        if not paragraph.is_boilerplate:
            text+=paragraph.text
    return text

query = "Jonatas Magno Tavares Ribeiro"
my_results_list = []

for url in search(query, tld="com", num=10, stop=10, pause=2):
    full_content = get_text(query)
    my_results_list.append({"fullCOntent": full_content, "url": url})
    print(f"URL: {url}")
    
print(my_results_list)
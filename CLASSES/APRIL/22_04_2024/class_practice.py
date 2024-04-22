#Insert here all theimport redis
#%%
import redis
from redis.commands.search.field import TextField, NumericField, VectorField
from redis_service import connect_redis, create_index
import json
import numpy as np 

#%% 
def get_embeddings_bert(text, tokenizer, model):
    # Tokenize and encode the text
    inputs = tokenizer(text, return_tensors="pt", max_length=512, truncation=True)

    # Get the embeddings
    output = model(**inputs)

    document_embedding = output.last_hidden_state.mean(dim=1).squeeze().detach().numpy()
    return document_embedding

#%%
from transformers import AutoTokenizer, AutoModel

model_name = "neuralmind/bert-base-portuguese-cased" #PORTULAN/albertina-ptpt
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)


#%% 
import json
with open("data/publico_km.json", "r",encoding="utf8") as readfile:
    KeyMoments = json.load(readfile)
    
ListOfContents = KeyMoments[:20]

for i in range(len(ListOfContents)):
    ListOfContents[i]['title_emb'] = get_embeddings_bert(ListOfContents[i]['title'], tokenizer, model)
    ListOfContents[i]['news_emb'] = get_embeddings_bert(ListOfContents[i]['news'], tokenizer, model)
    
    if i % 10 == 0:
            print(f"\r{100*i/len(ListOfContents):.2f}%", end='')
    elif i == len(ListOfContents) - 1:
        print(f"\r100.00%", end='')

#%%
def index_documents(r, doc_prefix, documents, *vector_fields):
    for i, doc in enumerate(documents):
        key = f"{doc_prefix}{str(i)}"
        
        for field in vector_field:
            # create byte vectors for item
            text_embedding = np.array(doc[field], dtype=np.float32).tobytes()

             # replace list of floats with byte vectors
            doc[field] = text_embedding
        
        r.hset(key, mapping=doc)
    
    print("Documents indexed")
#%%

index_name = 'idx:publico_hugging' #the name of the index, which you will use when doing queries
doc_prefix = 'publico_hugging:' #prefix for the document keys

# Constants
vector_field = 'title_emb'
vector_field1 = "news_emb"
VECTOR_DIM = len(ListOfContents[0][vector_field]) # length of the vectors
VECTOR_NUMBER = len(ListOfContents)              # initial number of vectors
DISTANCE_METRIC = "COSINE"                # distance metric for the vectors (ex. COSINE, IP, L2)

# Define RediSearch fields
source = TextField(name="source")
lan = TextField(name="lan")
topic = TextField(name="topic")
date = TextField(name="date")
title = TextField(name="title")
news = TextField(name="news")
title_emb = VectorField(vector_field,
    "FLAT", {
        "TYPE": "FLOAT32",
        "DIM": VECTOR_DIM,
        "DISTANCE_METRIC": DISTANCE_METRIC,
        "INITIAL_CAP": VECTOR_NUMBER,
    }
)
news_emb = VectorField(vector_field1,
    "FLAT", {
        "TYPE": "FLOAT32",
        "DIM": VECTOR_DIM,
        "DISTANCE_METRIC": DISTANCE_METRIC,
        "INITIAL_CAP": VECTOR_NUMBER,
    }
)

fields = [source, lan, topic, date, title, news, title_emb, news_emb]

r = connect_redis()
create_index(r, index_name, doc_prefix, fields)
index_documents(r, doc_prefix, ListOfContents, vector_field, vector_field1)
# %%

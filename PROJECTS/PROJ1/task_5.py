import json
import redis

# Connect to Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# Read JSON file
with open('data.json') as f:
    data = json.load(f)

# Index data into Redis
for item in data:
    # Assuming 'item_id' is unique identifier
    redis_client.set(f"item:{item['item_id']}", json.dumps(item))

print("Indexing completed successfully.")

import json
import os
from seed import data

FILE_PATH = os.path.join(os.path.dirname(__file__), 'data.json')

def read_data():
    with open(FILE_PATH, 'r') as f:
        return json.load(f)
    
def write_data(data):
    with open(FILE_PATH, 'w') as f:
        return json.dump(data, f, indent=2)
    
def seed_data():
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        write_data(data)
        print("Seeded data.json")
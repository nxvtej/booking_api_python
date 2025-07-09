import json

FILE_PATH = 'data.json'

def read_data():
    with open(FILE_PATH, 'r') as f:
        return json.load(f)
    
def write_data(data):
    with open(FILE_PATH, 'w') as f:
        return json.dump(data, f, indent=2)
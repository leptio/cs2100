"""Works with json files"""
#JSON: JavaScript Object Notation
#JSON data can be read into Python as a dictionary
import json
import pprint
import os

file_path = os.path.join(os.path.dirname(__file__), 'example_json_data.json')
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)
    pprint.pp(data)

import os
import re
import json

def get_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def get_file_list(path):
    file_list = os.listdir(path)
    return file_list

def file_name_to_movie_year(file_name):
    #regex search for something in file name
    result = re.search(r'(^(\w+[ |\.])+)\(*(19\d{2}|20\d{2})\)*', file_name)
    if result is not None:
        print(result.group(1), result.group(3))

if __name__ == '__main__':
    config = get_config()
    print("Config loaded")
    file_list = []
    for path in config['movies']['storage']['paths']:
        file_list.extend(get_file_list(path))
    print("file list retrieved")
    for file_name in file_list:
        file_name_to_movie_year(file_name)
import json

with open('discord_data.json', 'r') as f:
    file = json.load(f)
    data = file['data']
    meta = file['meta']

def meta_processing(meta):
    users = {}
    for user in meta['users'].keys():
        users[user] = meta['users'][user]['name']
    
    return users

users = meta_processing(meta)


with open('processed_discord_data.txt', 'w') as f:
    
    for item in data.values():
        try:
            f.write(f"{item['m']}\n")
        except:
            continue
import json

# read the json files into python dictionaries

with open("food-enforcement-0001-of-0001.json") as file:
    food_recall = json.load(file)
    
with open("food-event-0001-of-0001.json") as file:
    food_event = json.load(file)
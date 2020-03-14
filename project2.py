import json


# read the json files into python dictionaries

with open("food-enforcement-0001-of-0001.json") as file:
    food_recall = json.load(file)
    
with open("food-event-0001-of-0001.json") as file:
    food_event = json.load(file)

# iterate through event file
# check against recalls for similar product description to name_brand
# add similar recall and  products to owl, delete recalls from original json files
# add product to product list to check against (repeated name_brand)

name_brand_names = []
i = 0
for event in food_event["results"]:
    for product in event["products"]:
        for recall in food_recall["results"]:
            print(str(product["name_brand"]) + " ")
            print(recall["product_description"])
            break
        break
    if i < 2:
        i += 1
    else:
        break

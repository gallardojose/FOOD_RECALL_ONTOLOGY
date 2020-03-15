import json


def compare_strings(str1, str2):
    str1_list = [word for word in str1.split()]
    str2_list = [word for word in str2.split()]
    in_string = 0
    # word match
    for word in str1_list:
        if word in str2_list:
            in_string += 1
    # return word match percentage and length of name_brand
    return in_string/len(str1_list), len(str1_list)


# read the json files into python dictionaries
with open("food-enforcement-0001-of-0001.json") as file:
    food_recall = json.load(file)

with open("food-event-0001-of-0001.json") as file:
    food_event = json.load(file)

# iterate through event file
# check against recalls for similar product description to name_brand
# add similar recall and products to owl, delete recalls from dictionary
# add product to product list to check against (repeated name_brand)
# add any remaining recalls to owl file

name_brand_names = []
i = 0
for event in food_event["results"]:
    for product in event["products"]:
        if product["name_brand"] not in name_brand_names:
            for recall in food_recall["results"]:
                if compare_strings(product["name_brand"], recall["product_description"])[0] == 1 and \
                        compare_strings(product["name_brand"], recall["product_description"])[1] > 1:
                            # add food event & recall to owl

                            name_brand_names.append(product["name_brand"])
                            i += 1
        # else:
            # add food mishap



print(i)
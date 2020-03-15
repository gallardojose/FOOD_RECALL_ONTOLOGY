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
    if len(str1_list) > 0:
        return in_string/len(str1_list), len(str1_list)
    else:
        return 0, 0

# def add_food_mishap(mishap, added):
#     # open owl file and add individual mishap
#     # start mishap
#     rdf_mishap_opentag(mishap["report_number"])
#     # add list of reactions, report_number, list of outcomes, list of products
#     for reaction in mishap["reactions"]:
#         added.write(rdf_reaction(reaction)) # ask for insertion of newline
#     added.write(rdf_report_number(mishap["report_number"]))
#     for outcome in mishap["outcomes"]:
#         added.write(rdf_outcome(outcome))  # ask for insertion of newline
#     for product in mishap["products"]:
#         added.write(rdf_product_name_brand[product]["name_brand"])
#         added.write(rdf_product_industry_code[product]["industry_code"])
#         added.write(rdf_product_role[product]["role"])
#         added.write(rdf_product_industry_name[product]["industry_name"])
#     added.write(rdf_date_created(mishap["date_created"]))
#
#
#     rdf_mishap_closetag()



# def add_food_recall():


# read the json files into python dictionaries
with open("food-enforcement-0001-of-0001.json") as file:
    food_recall = json.load(file)

with open("food-event-0001-of-0001.json") as file:
    food_event = json.load(file)

# added mishaps and recalls
added = open("added.txt", "w")

# iterate through event file
# check against recalls for similar product description to name_brand
# add similar recall and products to owl, delete recalls from dictionary
# add product to product list to check against (repeated name_brand)
# add any remaining recalls to owl file

name_brand_names = []
i = 0
for event in food_event["results"]:
    print(event["date_started"])
    name_brand_names.append(event["date_started"])
    if not name_brand_names[0]:
        print("true")
    print(name_brand_names[0])
    break
    for product in event["products"]:
        if product["name_brand"] not in name_brand_names:
            for recall in food_recall["results"]:
                if compare_strings(product["name_brand"], recall["product_description"])[0] == 1 and \
                        compare_strings(product["name_brand"], recall["product_description"])[1] > 1:
                            # add recall to owl

                            name_brand_names.append(product["name_brand"])
                            i += 1
    # add food mishap
    # add_food_mishap(event, added)


print(i)
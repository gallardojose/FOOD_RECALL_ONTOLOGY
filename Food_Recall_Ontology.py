import json
import io

def start_file():
    string = "";
    string += "<?xml version=\"1.0\"?>\n";
    string += "<rdf:RDF xmlns=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#\"\n";
    string += "\txml:base=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall\"\n";
    string += "\txmlns:owl=\"http://www.w3.org/2002/07/owl#\"\n";
    string += "\txmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n";
    string += "\txmlns:xml=\"http://www.w3.org/XML/1998/namespace\"\n";
    string += "\txmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n";
    string += "\txmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n";
    string += "\txmlns:Food_Recall=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#\">\n";
    string += "\t<owl:Ontology rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall\"/>\n";
    f.write(string);

def end_file():
    f.write("</rdf:RDF>");
    
'''
def add_topObjectPropertyDescription():
    string = "\n\t";
    string += "<rdf:Description rdf:about=\"http://www.w3.org/2002/07/owl#topObjectProperty\">\n";
    string += "\t\t<rdfs:range>\n";
    string += "\t\t\t<owl:Restriction>\n";
    string += "\t\t\t\t<owl:onProperty rdf:resource=\"http://www.w3.org/2002/07/owl#topDataProperty\"/>\n";
    string += "\t\t\t\t<owl:someValuesFrom rdf:resource=\"http://www.w3.org/2001/XMLSchema#string\"/>\n";
    string += "\t\t\t</owl:Restriction>\n"
    string += "\t\t</rdfs:range>\n"
    string += "\t</rdf:Description>\n";
    f.write(string);
'''

#--------------------Class--------------------

def writeClass(name, subClassOf):
    string = "\n\t"
    
    if subClassOf == None:
        string += "<owl:Class rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
        string += name
        string += "\"/>"
    else:
        string += "<owl:Class rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
        string += name
        string += "\">"
        string += "\n    "
        string += "\t<rdfs:subClassOf rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
        string += subClassOf
        string += "\"/>"
        string += "\n\t</owl:Class>"
    
    string+="\n";
    f.write(string)
    

def addClasses():
    writeClass("address", "location");
    writeClass("city", "location");
    writeClass("class_i", "classification");
    writeClass("class_ii", "classification");
    writeClass("class_iii", "classification");
    writeClass("classification", None);
    writeClass("completed", "status");
    writeClass("consumer", None);
    writeClass("country", "location");
    writeClass("firm", None);
    writeClass("food_event", None);
    writeClass("food_mishap", "food_event");
    writeClass("food_recall", "food_event");
    writeClass("location", None);
    writeClass("ongoing", "status");
    writeClass("outcomes", None);
    writeClass("postal_code", "location");
    writeClass("product", None);
    writeClass("reactions", None);
    writeClass("state", "location");
    writeClass("status", None);
    writeClass("terminated", "status");



#--------------------Object Property--------------------


def writeObjectProperty(name, domain, rang):
    string = "\n\t"
    string += "<owl:ObjectProperty rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
    string += name
    string += "\">"
    string += "\n\t\t"
    
    string += "<rdfs:subPropertyOf rdf:resource=\"http://www.w3.org/2002/07/owl#"
    string += "topObjectProperty"
    string += "\"/>"
    
    string += "\n\t\t"
    string += "<rdfs:domain rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
    string += domain
    string += "\"/>"
        
    string += "\n\t\t"
    string += "<rdfs:range rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
    string += rang
    string += "\"/>"

    string += "\n\t</owl:ObjectProperty>"
    string+="\n";

    f.write(string)


def addObjectProperties():
    writeObjectProperty("corresponding_consumer", "food_mishap", "consumer");
    writeObjectProperty("current_status", "product", "status");
    writeObjectProperty("has_outcome", "food_mishap", "outcomes");
    writeObjectProperty("has_product", "food_event", "product");
    writeObjectProperty("has_reaction", "food_mishap", "reactions");
    writeObjectProperty("classify_as", "food_recall", "classification");
    writeObjectProperty("recalling_firm", "food_recall", "firm");


#--------------------NamedIndividual--------------------


def writeDataProperty(name, domain, rang):
    string = "\n\t"
    string += "<owl:DatatypeProperty rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"+ name +"\">\n";
    string += "\t\t<rdfs:subPropertyOf rdf:resource=\"http://www.w3.org/2002/07/owl#topDataProperty\"/>\n";
    string += "\t\t<rdfs:domain rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"+ domain +"\"/>\n";
    string += "\t\t<rdfs:range rdf:resource=\"http://www.w3.org/2001/XMLSchema#"+ rang +"\"/>\n";
    string += "\t</owl:DatatypeProperty>"
    string += "\n"
    f.write(string);

def addDataProperties():
    writeDataProperty("address", "food_recall", "string");
    writeDataProperty("city", "food_recall", "string");
    writeDataProperty("country", "food_recall", "string");
    writeDataProperty("postal_code", "food_recall", "string");
    writeDataProperty("state", "food_recall", "string");
    writeDataProperty("initial_firm_notification", "food_recall", "string");
    writeDataProperty("age", "consumer", "positiveInteger");
    writeDataProperty("age_unit", "consumer", "string");
    writeDataProperty("center_classification_date", "classification", "positiveInteger");
    writeDataProperty("code_info", "food_recall",  "string");
    writeDataProperty("date_created", "food_mishap", "positiveInteger");
    writeDataProperty("date_started", "food_mishap", "positiveInteger");
    writeDataProperty("distribution_pattern", "product", "string");
    writeDataProperty("event_id", "food_recall", "positiveInteger");
    writeDataProperty("gender", "consumer", "string");
    writeDataProperty("industry_code", "product", "positiveInteger");
    writeDataProperty("industry_name", "product", "string");
    writeDataProperty("more_code_info", "food_recall", "string");
    writeDataProperty("product_description", "product", "string");
    writeDataProperty("product_name", "product", "string");
    writeDataProperty("product_quantity", "product",  "string");
    writeDataProperty("product_type", "product",  "string");
    writeDataProperty("reason", "food_recall",  "string");
    writeDataProperty("recall_initialization_date",  "food_recall",  "positiveInteger");
    writeDataProperty("recall_number", "food_recall", "string");
    writeDataProperty("report_date", "food_recall", "positiveInteger");
    writeDataProperty("report_number", "food_mishap", "positiveInteger");
    writeDataProperty("role", "product", "string");
    writeDataProperty("termination_date", "product", "positiveInteger");
    writeDataProperty("voluntary_mandated", "food_recall", "string");


def writeNamedIndividual(individual, classType, objectAssertions, dataAssertions):
    string = "\n\t";
    string += "<owl:NamedIndividual rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"+individual+"\">\n";
    string += "\t\t<rdf:type rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"+classType+"\"/>\n";
    
    if(objectAssertions != None):
        for item in objectAssertions:
            string += "\t\t<"+item[0]+" rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"+item[1]+"\"/>\n";
    if(dataAssertions != None):
        for item in dataAssertions:
            string += "\t\t<"+item[0]+ " rdf:datatype=\"http://www.w3.org/2001/XMLSchema#"+ item[2] +"\">"+str(item[1])+"</"+item[0]+">\n"
            
   
    string += "\t</owl:NamedIndividual>";
    string += "\n";
    f.write(string);


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

def remove_special_chars(s):
    s2 = ""
    for char in s:
        if not char.isalpha() and not char.isdigit():
            s2 = s2 + " "
        else:
            s2 += char

    return s2


def addNamedIndividuals():
    '''
    #JOSE NEEDS TO FILL THIS IN (POPULATE DATA)
    
    The objectAssertions variable is a list of tuples. A tuple consists (objectProperty, Individual")
    The dataAssertions variable is a list of tuples. A tuple consists (DataProperty_name, value, type")
    
    Example of creating an Individual:
    #writeNamedIndividual("Alice", "consumer", [("has_reactions","FOOD_ALLERGY") , ....]  , [("age", 43, "positiveInteger"), ("gender", "male", "string"), .....]);
    
    '''
    
    #writeNamedIndividual("Alice", "consumer", [("has_reactions","FOOD_ALLERGY") ]  , [("age", 43, "positiveInteger"), ("gender", "male", "string")]);

    ''' 
    iterate through event file
    check against recalls for similar product description to name_brand
    add similar recall and products to owl, delete recalls from dictionary
    add product to product list to check against (repeated name_brand)
    '''
    i = 0
    consumer_id = 1
    name_brand_names = {}
    classifications = {}
    firms = {}
    recall_list = food_recall["results"]
    for event in food_event["results"]:
        if i < 50:
            event_products = []
            for product in event["products"]:
                product_name_brand = remove_special_chars(str(product["name_brand"]))
                event_products.append(product_name_brand)
                if product_name_brand not in name_brand_names:
                    # add product to ontology first so it can be referenced by recall and mishap
                    try:
                        writeNamedIndividual(product_name_brand, "product", [], [("product_name", product_name_brand, "string"), ("industry_code", product["industry_code"], "positiveInteger"), ("industry_name", product["industry_name"], "string"), ("role", product["role"], "string")])
                    except:
                        print("")
                    name_brand_names[product_name_brand] = 1
                    recall_index = 0
                    for recall in recall_list:
                        compared_strings = compare_strings(product_name_brand, recall["product_description"])
                        if compared_strings[0] == 1 and compared_strings[1] > 1:
                            # add recall and corresponding properties to owl / delete from dictionary
                            if recall["classification"] not in classifications:
                                writeNamedIndividual(recall["classification"], "classification", [], [])
                                classifications[recall["classification"]] = 1
                            recall_firm = remove_special_chars(recall["recalling_firm"])
                            if recall_firm not in firms:
                                writeNamedIndividual(recall_firm, "firm", [], [])
                                firms[recall_firm] = 1

                            # add recall to ontology
                            try:
                                writeNamedIndividual(recall["recall_number"], "food_recall", [("classify_as", recall["classification"]) if recall["classification"] else "", ("has_product", product_name_brand), ("recalling_firm", recall_firm)], [("address", recall["address_1"], "string"), ("city", recall["city"], "string"), ("code_info", recall["code_info"], "string"), ("country", recall["country"], "string"), ("event_id", recall["event_id"], "positiveInteger"), ("initial_firm_notifaction", recall["initial_firm_notification"], "string"), ("postal_code", recall["postal_code"], "string"), ("reason", recall["reason_for_recall"], "string"), ("recall_initialization_date", recall["recall_initiation_date"], "positiveInteger"), ("recall_number", recall["recall_number"], "string"), ("report_date", recall["report_date"], "positiveInteger"), ("state", recall["state"], "string"), ("voluntary_mandated", recall["voluntary_mandated"], "string")])
                            except:
                                print("")
                            recall_list.pop(recall_index)
                        recall_index += 1

            # add consumer
            mishap_object_array = []
            consumer_array = []
            if not event["consumer"] == {}:
                if "age" in event["consumer"].keys():
                    consumer_array.append(("age", event["consumer"]["age"], "positiveInteger"))
                if "age_unit" in event["consumer"].keys():
                    consumer_array.append(("age_unit", event["consumer"]["age_unit"], "string"))
                if "gender" in event["consumer"].keys():
                    consumer_array.append(("gender", event["consumer"]["gender"], "string"))
                writeNamedIndividual(str(consumer_id), "consumer", [], consumer_array)
                mishap_object_array.append(("corresponding_consumer", str(consumer_id)))
                consumer_id += 1
            # add products
            for product in event_products:
                mishap_object_array.append(("has_product", product))
            # add outcomes
            for outcome in event["outcomes"]:
                writeNamedIndividual(outcome, "outcomes", [], [])
                mishap_object_array.append(("has_outcome", outcome))
            # add reactions
            for reaction in event["reactions"]:
                writeNamedIndividual(reaction, "reaction", [], [])
                mishap_object_array.append(("has_reaction", reaction))
            # add food mishap
            try:
                writeNamedIndividual(event["report_number"], "food_mishap",
                                     mishap_object_array,
                                     [("date_created", event["date_created"] , "positiveInteger") if event["date_created"] else "",
                                      ("date_started", event["date_started"], "positiveInteger"),
                                      ("report_number", event["report_number"], "positiveInteger")])
            except:
                print("")
        
        i += 1


    
    return





# ------------ Create and Write in file ----------------





# read the json files into python dictionaries

with open("food-enforcement-0001-of-0001.json") as file:
    food_recall = json.load(file)
    
with open("food-event-0001-of-0001.json") as file:
    food_event = json.load(file)


f = io.open("./Food_Recall.owl", "w", encoding="utf-8");
start_file();
addClasses();
addObjectProperties();
addDataProperties();
addNamedIndividuals();
end_file();
f.close();

print("Done");


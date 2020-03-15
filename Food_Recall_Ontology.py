import json

def start_file(uri):
    string = "";
    string += "<?xml version=\"1.0\"?>\n";
    string += "<rdf:RDF xmlns=\""
    string += uri
    string += "#\"\n";
    string += "\txml:base=\""
    string += uri
    string += "\"\n";
    string += "\txmlns:owl=\"http://www.w3.org/2002/07/owl#\"\n";
    string += "\txmlns:rdf=\"http://www.w3.org/1999/02/22-rdf-syntax-ns#\"\n";
    string += "\txmlns:xml=\"http://www.w3.org/XML/1998/namespace\"\n";
    string += "\txmlns:xsd=\"http://www.w3.org/2001/XMLSchema#\"\n";
    string += "\txmlns:rdfs=\"http://www.w3.org/2000/01/rdf-schema#\"\n";
    string += "\txmlns:Food_Recall=\""
    string += uri
    string += "#\">\n";
    string += "\t<owl:Ontology rdf:about=\""
    string += uri
    string += "\"/>\n";
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

def writeClass(name, subClassOf, uri):
    string = "\n\t"
    
    if subClassOf == None:
        string += "<owl:Class rdf:about=\""
        string += uri
        string += "#"
        string += name
        string += "\"/>"
    else:
        string += "<owl:Class rdf:about=\""
        string += uri
        string += "#"
        string += name
        string += "\">"
        string += "\n    "
        string += "\t<rdfs:subClassOf rdf:resource=\""
        string += uri
        string += "#"
        string += subClassOf
        string += "\"/>"
        string += "\n\t</owl:Class>"
    
    string+="\n";
    f.write(string)
    

def addClasses(uri):
    writeClass("address", "location", uri);
    writeClass("city", "location", uri);
    writeClass("class_i", "classification", uri);
    writeClass("class_ii", "classification", uri);
    writeClass("class_iii", "classification", uri);
    writeClass("classification", None, uri);
    writeClass("completed", "status", uri);
    writeClass("consumer", None, uri);
    writeClass("country", "location", uri);
    writeClass("firm", None, uri);
    writeClass("food_event", None, uri);
    writeClass("food_mishap", "food_event", uri);
    writeClass("food_recall", "food_event", uri);
    writeClass("location", None, uri);
    writeClass("ongoing", "status", uri);
    writeClass("outcomes", None, uri);
    writeClass("postal_code", "location", uri);
    writeClass("product", None, uri);
    writeClass("reactions", None, uri);
    writeClass("state", "location", uri);
    writeClass("status", None, uri);
    writeClass("terminated", "status", uri);



#--------------------Object Property--------------------


def writeObjectProperty(name, domain, rang, uri):
    string = "\n\t"
    string += "<owl:ObjectProperty rdf:about=\""
    string += uri
    string += "#"
    string += name
    string += "\">"
    string += "\n\t\t"
    
    string += "<rdfs:subPropertyOf rdf:resource=\"http://www.w3.org/2002/07/owl#"
    string += "topObjectProperty"
    string += "\"/>"
    
    string += "\n\t\t"
    string += "<rdfs:domain rdf:resource=\""
    string += uri
    string += "#"
    string += domain
    string += "\"/>"
        
    string += "\n\t\t"
    string += "<rdfs:range rdf:resource=\""
    string += uri
    string += "#"
    string += rang
    string += "\"/>"

    string += "\n\t</owl:ObjectProperty>"
    string+="\n";

    f.write(string)


def addObjectProperties(uri):
    writeObjectProperty("corresponding_consumer", "food_mishap", "consumer", uri);
    writeObjectProperty("current_status", "product", "status", uri);
    writeObjectProperty("has_outcome", "food_mishap", "outcomes", uri);
    writeObjectProperty("has_product", "food_event", "product", uri);
    writeObjectProperty("has_reaction", "food_mishap", "reactions", uri);
    writeObjectProperty("classify_as", "food_recall", "classification", uri);
    writeObjectProperty("recalling_firm", "food_recall", "firm", uri);


#--------------------NamedIndividual--------------------


def writeDataProperty(name, domain, rang, uri):
    string = "\n\t"
    string += "<owl:DatatypeProperty rdf:about=\""
    string += uri
    string += "#"+ name +"\">\n";
    string += "\t\t<rdfs:subPropertyOf rdf:resource=\"http://www.w3.org/2002/07/owl#topDataProperty\"/>\n";
    string += "\t\t<rdfs:domain rdf:resource=\""
    string += uri
    string += "#"+ domain +"\"/>\n";
    string += "\t\t<rdfs:range rdf:resource=\"http://www.w3.org/2001/XMLSchema#"+ rang +"\"/>\n";
    string += "\t</owl:DatatypeProperty>"
    string += "\n"
    f.write(string);

def addDataProperties(uri):
    writeDataProperty("address", "food_recall", "string", uri);
    writeDataProperty("city", "food_recall", "string", uri);
    writeDataProperty("country", "food_recall", "string", uri);
    writeDataProperty("postal_code", "food_recall", "string", uri);
    writeDataProperty("state", "food_recall", "string", uri);
    writeDataProperty("initial_firm_notification", "food_recall", "string", uri);
    writeDataProperty("age", "consumer", "positiveInteger", uri);
    writeDataProperty("age_unit", "consumer", "string", uri);
    writeDataProperty("center_classification_date", "classification", "positiveInteger", uri);
    writeDataProperty("code_info", "food_recall",  "string", uri);
    writeDataProperty("date_created", "food_mishap", "positiveInteger", uri);
    writeDataProperty("date_started", "food_mishap", "positiveInteger", uri);
    writeDataProperty("distribution_pattern", "product", "string", uri);
    writeDataProperty("event_id", "food_recall", "positiveInteger", uri);
    writeDataProperty("gender", "consumer", "string", uri);
    writeDataProperty("industry_code", "product", "positiveInteger", uri);
    writeDataProperty("industry_name", "product", "string", uri);
    writeDataProperty("more_code_info", "food_recall", "string", uri);
    writeDataProperty("product_description", "product", "string", uri);
    writeDataProperty("product_name", "product", "string", uri);
    writeDataProperty("product_quantity", "product",  "string", uri);
    writeDataProperty("product_type", "product",  "string", uri);
    writeDataProperty("reason", "food_recall",  "string", uri);
    writeDataProperty("recall_initialization_date",  "food_recall",  "positiveInteger", uri);
    writeDataProperty("recall_number", "food_recall", "string", uri);
    writeDataProperty("report_date", "food_recall", "positiveInteger", uri);
    writeDataProperty("report_number", "food_mishap", "positiveInteger", uri);
    writeDataProperty("role", "product", "string", uri);
    writeDataProperty("termination_date", "product", "positiveInteger", uri);
    writeDataProperty("voluntary_mandated", "food_recall", "string", uri);

    







def writeNamedIndividual(individual, classType, objectAssertions, dataAssertions, uri):
    string = "\n\t";
    string += "<owl:NamedIndividual rdf:about=\""
    string += uri
    string += "#"+individual+"\">\n";
    string += "\t\t<rdf:type rdf:resource=\""
    string += uri
    string += "#"+classType+"\"/>\n";
    
    if(objectAssertions != None):
        for item in objectAssertions:
            string += "\t\t<"+item[0]+" rdf:resource=\""
            string += uri
            string += "#"+item[1]+"\"/>\n";
    if(dataAssertions != None):
        for item in dataAssertions:
            string += "\t\t<"+item[0]+ " rdf:datatype=\"http://www.w3.org/2001/XMLSchema#"+ item[2] +"\">"+str(item[1])+"</"+item[0]+">\n"
            
   
    string += "\t</owl:NamedIndividual>";
    string += "\n";
    f.write(string);










def addNamedIndividuals(uri):
    '''
    #JOSE NEEDS TO FILL THIS IN (POPULATE DATA)
    
    The objectAssertions variable is a list of tuples. A tuple consists (objectProperty, Individual")
    The dataAssertions variable is a list of tuples. A tuple consists (DataProperty_name, value, type")
    
    Example of creating an Individual:
    #writeNamedIndividual("Alice", "consumer", [("has_reactions","FOOD_ALLERGY") , ....]  , [("age", 43, "positiveInteger"), ("gender", "male", "string"), .....]);
    
    '''
    
    #writeNamedIndividual("Alice", "consumer", [("has_reactions","FOOD_ALLERGY") ]  , [("age", 43, "positiveInteger"), ("gender", "male", "string")]);

    
    return





# ------------ Create and Write in file ----------------





# read the json files into python dictionaries

with open("food-enforcement-0001-of-0001.json") as file:
    food_recall = json.load(file)
    
with open("food-event-0001-of-0001.json") as file:
    food_event = json.load(file)





f = open("./Food_Recall.owl", "w");
start_file("Food_Recall");
addClasses("Food_Recall");
addObjectProperties("Food_Recall");
addDataProperties("Food_Recall");
addNamedIndividuals("Food_Recall");
end_file();
f.close();

print("Done");
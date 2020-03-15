# sample of calls 
# writeObjectProperty("has_product","topObjectProperty","address","true","true","positiveInteger")
# -- when "range" and "restriction" are true, you have the structure below:
'''
    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#recall_number">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#food_recall"/>
        <rdfs:range>
            <owl:Restriction>
                <owl:onProperty rdf:resource="http://www.w3.org/2002/07/owl#topDataProperty"/>
                <owl:someValuesFrom rdf:resource="http://www.w3.org/2001/XMLSchema#positiveInteger"/>
            </owl:Restriction>
        </rdfs:range>
    </owl:ObjectProperty> 
'''

#writeObjectProperty("has_product","topObjectProperty","address","firm",None,"positiveInteger")
# -- when "range" has a value and "restriction" is None, you have the following structure:
'''
    <owl:ObjectProperty rdf:about="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#recalling_firm">
        <rdfs:subPropertyOf rdf:resource="http://www.w3.org/2002/07/owl#topObjectProperty"/>
        <rdfs:domain rdf:resource="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#food_recall"/>
        <rdfs:range rdf:resource="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#firm"/>
    </owl:ObjectProperty>
'''


def writeObjectProperty(name, subPropertyOf, domain, range, restriction, someValuesFrom):
    string = ""
    string += "<owl:ObjectProperty rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#"
    string += name
    string += "\">"
    string += "\n    "
    
    if len(subPropertyOf) != 0:
        string += "<rdfs:subPropertyOf rdf:resource=\"http://www.w3.org/2002/07/owl#"
        string += subPropertyOf
        string += "\"/>"
    
    if len(domain) != 0:
        string += "\n    "
        string += "<rdfs:domain rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#"
        string += domain
        string += "\"/>"
        
    if restriction != None:
        string += "\n    "
        string += "<rdfs:range>"
        string += "\n        "
        string += "<owl:Restriction>"
        string += "\n            "
        string += "<owl:onProperty rdf:resource=\"http://www.w3.org/2002/07/owl#topDataProperty\"/>"
        string += "\n            "
        string += "<owl:someValuesFrom rdf:resource=\"http://www.w3.org/2001/XMLSchema#"
        string += someValuesFrom
        string += "\"/>"
        string += "\n        "
        string += "</owl:Restriction>"
        string += "\n    "
        string += "</rdfs:range>"
    else:
        string += "\n    "
        string += "<rdfs:range rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#"
        string += range
        string += "\"/>"

    string += "\n</owl:ObjectProperty>"
    file.write(string)


# sample of calls
# writeClass("food_mishap", "food_event") -- the result is:
'''
<owl:Class rdf:about="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#food_mishap">
    <rdfs:subClassOf rdf:resource="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#food_event"/>
</owl:Class>

'''

# writeClass("product", None) -- the result is:
'''
<owl:Class rdf:about="http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#product"/>

'''
 
def writeClass(name, subClassOf):
    string = ""
    
    if subClassOf == None:
        string += "<owl:Class rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#"
        string += name
        string += "\"/>"
    else:
        string += "<owl:Class rdf:about=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recalltt#"
        string += name
        string += "\">"
        string += "\n    "
        string += "<rdfs:subClassOf rdf:resource=\"http://www.semanticweb.org/owner/ontologies/2020/2/Food_Recall#"
        string += subClassOf
        string += "\"/>"
        string += "\n</owl:Class>"
    
    file.write(string)
    



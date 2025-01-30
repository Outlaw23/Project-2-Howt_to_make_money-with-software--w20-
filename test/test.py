#imports
import json
import os

# variabelen
totaalKosten = ""

# json data
data = {
        "company": {
        "name": "Paper Code",
        "address": "Puzzelpap, 2367YU Antwerpen",
        "phone": "+32 069876543",
        "email": "PaperCode@outlook.com"
        },
        "kosten": {
        "totaalKosten": totaalKosten

        }


}

with open(f"") as json_file:
        dataLoad = json.load(json_file)

#json generator
with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

# functions
def totaalKostenFun():


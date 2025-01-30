# imports
import json
import os



# variabelen



# functions
with open(f"test_set_softwareleverancier/2000-018.json") as f:
    dataLoad = json.load(f)

kostenPerStuk = (dataLoad["order"]["producten"][0]["prijs_per_stuk_excl_btw"])
aantal = (dataLoad["order"]["producten"][0]["aantal"])

totaalKosten = kostenPerStuk * aantal



# json data
data = {
    "company": {
        "name": "Paper Code",
        "address": "Puzzelpap, 2367YU Antwerpen",
        "phone": "+32 069876543",
        "email": "PaperCode@outlook.com"
    },
    "kosten": {
        "totaalKosten":totaalKosten,
        "kostenPerStuk": kostenPerStuk,
        },
    "order": {
        "ordernummer": dataLoad["order"]["ordernummer"],
        "orderdatum":   dataLoad["order"]["orderdatum"],
        "betaaltermijn": dataLoad["order"]["betaaltermijn"],
        },
    "klant": dataLoad["order"]["klant"]
    }




# json generator
with open("factuur.json", "w") as json_file:
    json.dump(data, json_file, indent=4)





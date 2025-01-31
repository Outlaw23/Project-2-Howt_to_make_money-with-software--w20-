# imports
import json
import os

# variabelen


# functions
with open(f"../../../test_set_softwareleverancier/2000-018.json") as f:
    dataLoad = json.load(f)

kostenPerStuk = (dataLoad["order"]["producten"][0]["prijs_per_stuk_excl_btw"])
aantal = (dataLoad["order"]["producten"][0]["aantal"])

totaalKosten = kostenPerStuk * aantal

# json data
data = {
    "company": {
        "name": "Paper Code",
        "address": "Puzzelpap 29",
        "postcode" : "2367YU Sliedrecht",
        "phone": "+32 069876543",
        "email": "PaperCode@outlook.com"
    },
    "kosten": {
        "totaalKosten": totaalKosten,
        "kostenPerStuk": kostenPerStuk,
    },
    "order": {
        "ordernummer": dataLoad["order"]["ordernummer"],
        "orderdatum": dataLoad["order"]["orderdatum"],
        "betaaltermijn": dataLoad["order"]["betaaltermijn"],
    },
    "klant": dataLoad["order"]["klant"],
    "producten": {
        "productnaam": dataLoad["order"]["producten"][0]["productnaam"],
        "aantal" : dataLoad["order"]["producten"][0]["aantal"],
        "prijs_per_stuk_excl_btw" : dataLoad["order"]["producten"][0]["prijs_per_stuk_excl_btw"],
        "btw_percentage": dataLoad["order"]["producten"][0]["btw_percentage"],
        "totaalKosten": totaalKosten,
    }

}

# json generator
with open("../../deel 3/P2,D3,O1/factuur.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

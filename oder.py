import json
import os





for x in os.listdir("test_set_softwareleverancier"):
    print(x)


with open(f"test_set_softwareleverancier/2000-018.json") as json_file:
    data = json.load(json_file)

    # Print the data
    hoi = (data["order"]["producten"][0]["prijs_per_stuk_excl_btw"])
    print(hoi)
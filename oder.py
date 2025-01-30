import json
import os

with open("factuur.json") as f:
    data = json.load(f)

    # Print the data
    hoi = data["klant"]["naam"]
    print(hoi)

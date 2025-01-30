import json

data = {
    "naam": "Jan",
    "leeftijd": 30,
    "hobby's": ["lezen", "voetbal", "muziek"]
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

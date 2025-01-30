import json

data = {
        "company": {
        "name": "Paper Code",
        "address": "Puzzelpap, 2367YU Antwerpen",
        "phone": "+32 069876543",
        "email": "PaperCode@outlook.com"
        }
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file, indent=4)

    #     "company": {
    #     "name": "Paper Code",
    #     "address": "Puzzelpap, 2367YU Antwerpen",
    #     "phone": "+32 069876543",
    #     "email": "PaperCode@outlook.com"
    #     }
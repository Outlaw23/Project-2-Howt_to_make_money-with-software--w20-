import json
import os





for x in os.listdir("test_set_softwareleverancier"):
    print(x)


    with open(f"test_set_softwareleverancier/{x}") as json_file:
        data = json.load(json_file)

    # Print the data
    print(data)
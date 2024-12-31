import json

with open("test.json", "r") as file:
    myfile = json.load(file)


print(myfile)

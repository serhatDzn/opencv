import json
with open("team.json","r") as file:
    data = json.load(file)


print(data["starPlayer"])


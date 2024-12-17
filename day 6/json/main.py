import json

# json to Dictionry
with open("json/example_1.json","r") as json_file:
    data = json.load(json_file)
    print(data , type(data))

data = {
    "name":"Dilan",
    "age":20
}

with open("json/write.json","w") as test_file:
    test_file.write(json.dumps(data,indent=4))
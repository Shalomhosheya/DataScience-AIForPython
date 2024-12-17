import csv

csv_file_path = "csv/test.csv"

data = [
    {"Name":"Jhon Doe","Age":30,"city":"New York"},
    {"Name":"Jane Smith","Age":28,"city":"LA"},
    {"Name":"Bob Johanason","Age":35,"city":"Chicago"}
]

field_names = ["Name","Age","city"]

with open(csv_file_path,"w",newline="") as file:
    csv_writer = csv.DictWriter(file,fieldnames=field_names)

    csv_writer.writeheader()

    for row in data:
        csv_writer.writerow(row)

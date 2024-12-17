import csv

with open("csv/customers-100.csv","r",newline="")as customers:
        # print(csv.reader(customers),type(csv.reader(customers)))
        # csv_reder = csv.reader(customers)

        # for row in csv_reder:
        #     print(row,type(row))

        dict_reder = csv.DictReader(customers)

        for row in dict_reder:
              print(row,type(row))
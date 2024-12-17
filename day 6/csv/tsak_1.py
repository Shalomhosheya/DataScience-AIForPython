import csv
 
high_salay = []
with open("csv/customer.csv") as customers:
    files = csv.reader(customers)
    # print(files)

    for row in files:
        print(row)
        if row[3] == "Salary":
                continue
        elif int(row[3]) > 57000:
            high_salay.append(dict({
                 "EmployeeId":row[0] ,"Name":row[1] ,"Department" = row[2] ,"Salary" : row[3]
                 
            }))
            high_salay["EmployeeId"] = row[0]
            high_salay["Name"] = row[1]
            high_salay["Department"]= row[2]
            high_salay["Salary"] = row[3]
print(high_salay)

field_names=["EmployeeId","Name","Department","Salary"]

with open("csv/high_salary_employee.csv","w",newline="") as salary:
    csv_writer = csv.DictWriter(salary,fieldnames=field_names)

    csv_writer.writeheader()

    for row in high_salay:
         print(row)
        # csv_writer.writerow(row)

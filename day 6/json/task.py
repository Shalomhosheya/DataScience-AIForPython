import json

def view_all():
    with open("json/student.json","r") as json_file:
        data = json.load(json_file)
        for student in data:
            if(student["grade"]>75):
                print(student)

def add_student():

    datas ={}

    datas["name"] = input("input name : ")
    datas["grade"] = int(input("input grade : "))
    print(datas)


    with open("json/student.json","r") as json_file:
        data = json.load(json_file)
        data.append(datas)
        with open("json/student.json","w") as json_file:
            json_file.write(json.dumps(data))
                
add_student()
view_all()
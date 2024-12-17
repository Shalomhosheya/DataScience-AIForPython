def add_new_contact():
    contcat_list = []
    massage = ["name : ","mobile : ","email :"]
    
    for i in range(0,len(massage)):
        contcat_list.append(input(massage[i]))
        
    
    with open("task1/contact.txt","a") as contact:
        for i in range(0,len(contcat_list)):
            contact.write(contcat_list[i]+"\n")
        

def view_all_contact():
    with open("task1/contact.txt","r") as contact:
        lists = contact.readlines()
        for i in lists:
            print(i)
        

while(True):

    option = int(input("input an option : "))

    match option :
        case 1: add_new_contact()
        case 2: view_all_contact()
        case 3: break
    


with open("my_file.txt") as file:
    content = file.read()
    print(content,type(content))

with open("my_file1.txt","w") as file1:
    # file1.write("I love Programing.\n")
    # file1.write("I want to do some specal things using programing")

    file1.writelines(["I love Programing\n","I want to do some specal things using programing"])

with open("my_file1.txt","a") as file1: #append mode
    file1.write("\nHi Kids")
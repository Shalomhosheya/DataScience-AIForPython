file1  = open("my_file.txt") # by default read mode
file2  = open("my_file1.txt","w")
print(file1.readlines(),type(file1.readlines()))

file1.close()

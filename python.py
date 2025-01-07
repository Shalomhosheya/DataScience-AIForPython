# import requests
# response = requests.get('https://api.github.com/events')

# print(response)
# print("\n",response.status_code,"\n")
# if response.status_code == 200:
#     print("success","\n")
#     print(response.headers,"\n")
#     print(response.headers['content-type'])
#     print("\n",response.text)




# print("hello world!")

# my_tuple_1=(20,"cat",10) #have comma 
# my_list_4=list(my_tuple_1)
# my_list_4[1]="rat"
# my_tuple_1=tuple(my_list_4)
# print(my_tuple_1)
# print(type(my_tuple_1))

# my_list = [10,20,'dog',True,45]
# my_list_2 = my_list.copy()
# my_list.append("dead")
# print(my_list_2)

# my_list = [10,20,'dog',True,45]
# my_list_2 = list(my_list)
# my_list.append("dead")
# print(my_list_2)

# my_list_3=[10,20,50,"fan","man"]
# my_list_3=my_list_2+my_list
# print(my_list_3)   

# my_tuple_1=(10,"cat",50,80)#tuple is round brackets
# print(len(my_tuple_1))
# print(type(my_tuple_1))

# my_tuple_1=(10,"cat",50,80)#tuple is round brackets
# my_tuple_1[1]="dog"
# print(len(my_tuple_1))
# print(type(my_tuple_1))

# my_tuple_1=(20,"cat",10) #have comma 
# my_list_4=list(my_tuple_1)
# my_list_4[1]="rat"
# my_tuple_1=tuple(my_list_4)
# print(my_tuple_1)
# print(type(my_tuple_1))

# my_tuple_1=(10,8,20,5)
# my_tuple_2=(5,9,-1)
# my_tuple_3 = list(my_tuple_1+my_tuple_2)
# my_tuple_3.pop(2)
# my_tuple_3.sort()
# print(my_tuple_3)

# my_tuple_1=((1,10,8),("dog","cat","rat"),(True,False)) 
# print(my_tuple_1[0][1], my_tuple_1[1][2], my_tuple_1[2][1])
# s_1=range(5,20,3)
# print(s_1,type(s_1))
# for i in s_1:
#     print(i) 

# dict_1 ={
# "name":"sugar",
# "weight":"1kg",
# "price":100,
# "price":150 #replace /it does not duplicate
# }
# print(dict_1,type(dict_1))
# print(dict_1["weight"])
# print(len(dict_1))

# dict_1 ={
# "name":"sugar",
# "weight":"1kg",
# "price":100
# }

# print(dict_1,type(dict_1))
# print(dict_1["weight"])
# print(len(dict_1))

# dict_1.update({"weight":"2kg","price":270.50})
# print(dict_1,type(dict_1))

# dict_1["color"]="white"
# print(dict_1,"lenght:",len(dict_1))

# dict_1.pop("weight")#remove the 
# print(dict_1)

# dict_1.popitem()#final class will be 
# print(dict_1)

# dict_2 =dict_1.copy()#copy is used to copy the dict
# dict_1["name"]="pol"
# print(dict_1)
# print(dict_2)
# print()
# print(dict_2.keys())

# x=50
# y=7

# print(x//y)#ignores the decimal
# print(x%y)#ignores the decimal

# x=5
# print(x==5)

# x=input("enter value:")
# print(x)



# # del dict_1["price"]#another method to delete the code
# # print(dict_1)


# x=1000
# y=1000

# print(x is y)

import pdb

def multiplication(a,b):
 answer = a*b
 return answer

pdb.set_trace()
a = input("enter the number")
b = input("enter the number")
result = multiplication(a,b)
print(result)
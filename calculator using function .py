#
# replace1=""
# print("***************     welcome to zodiac calculator")
# print("enter a number1 :")
# num1=int(input())
# print("enter a number2 :")
# num2=int(input())
# print("these are the operators you can use :")
# print("1.addition")
# print("2.subtraction")
# print("3.multiplication")
# print("4.division")
# print("5.modulus")
# operator=input("please choose an option from these (1,2,3,4,5):")
# print(operator)
# replace1=""
# result=0
# def add(num1,num2):
#     return num1+num2
# if operator == "1":
#     result=add(num1,num2)
#     print(result)
# def subtract(num1,num2):
#     return num1-num2
# if operator == "2":
#     result=subtract(num1,num2)
#     print(result)
# def multiply(num1,num2):
#     return num1* num2
# if operator == "3":
#     result = multiply(num1, num2)
#     print(result)
# def division(num1, num2):
#     return num1/num2
# if operator == "4":
#     result = division(num1, num2)
#     print(result)
# def modulus(num1, num2):
#     return num1%num2
# if operator == "5":
#     result = modulus(num1, num2)
#     print(result)
#
#
#




num1=int(input())
print("enter a number2 :")
num2=int(input())
print("these are the operators you can use :")
print("1.addition")
print("2.subtraction")
print("3.multiplication")
print("4.division")
print("5.modulus")
operator=input("please choose an option from these (1,2,3,4,5):")
replace1=""
result=0
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2
def modulus(num1,num2):
    return num1%num2
if operator == "1":
   result = add(num1, num2)
   print(result)
if operator == "2":
   result = subtract(num1, num2)
   print(result)
if operator == "3":
   result = multiply(num1, num2)
   print(result)
if operator == "4":
   result = division(num1, num2)
   print(result)
if operator == "5":
   result = modulus(num1, num2)
   print(result)
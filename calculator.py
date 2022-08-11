 print("***************************** welcome to mini calculator")
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
# if operator=="1":
#     print("this an addition operation")
#     print("sum of the two number is:",num1+num2)
# if operator=="2":
#     print("this is an subtraction operator")
#     print("the difference of the two number is :",num1-num2)
# if operator=="3":
#     print("this is an multiplication operator")
#     print("the multiplication of the two number is :",num1*num2)
# if operator=="4":
#     print("this is an division operator")
#     print("the division of the two number is :",num1/num2)
# if operator=="4":
#     print("this is an modulus operation")
#     print("the modulus of the two number is :",num1%num2)
#








                       #optimising


#
# replace1=""
# print("***************************** welcome to mini calculator")
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

# result=0
# operator=input("please choose an option from these (1,2,3,4,5):")
# print(operator)
# if operator=="1":
#     replace1="addition"
#     result=num1+num2
# if operator=="2":
#     replace1="subtraction"
#     result=num1-num2
# if operator=="3":
#     replace1="multiplication"
#     result=num1*num2
# if operator=="4":
#     replace1="division"
#     result=num1/num2
# if operator=="4":
#     replace1="modulus"
#     result=num1%num2
# print("the result of",replace1,"of",num1,"and",num2,"is",result)
#
#






print("***************************** welcome to mini calculator")
print("enter a number1 :")
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
print(operator)
flag="print"
replace1=""
result=0
if operator=="1":
    replace1 = "addition"
    result=num1+num2
if operator=="2":
    if num1<num2:
        flag="do not print"
        print("cannot subtract the first number is less than the second number")
    else:
        flag="print"
        replace1="subtraction"
        result=num1-num2
if operator=="3":
    replace1 = "multiplication"
    result=num1*num2
if operator=="4":
    replace1="division"
    result=num1/num2
if operator=="4":
    replace1="modulus"
    result=num1%num2
if flag=="print":
    print("the result of",replace1,"of",num1,"and",num2,"is",result)





vowels_and_constants=['a','e','i','o','u','r','t','w','x','P','A','E','I','O','U']
vowels=['A','E','I','O','U']
vowels_list=[]
constants_list=[]
for i in vowels_and_constants:
    i=i.upper()
    if i in vowels:
        vowels_list.append(i)
    else:
        constants_list.append(i)
print(vowels_list)
print(constants_list)

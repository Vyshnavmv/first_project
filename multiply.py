# mul=1
# for i in range(1,11):
#     mul*=i
# print(mul)





num=12345
sum=0
for i in range(len(str(num))):  # convert to string annd calculate the length
    temp=num%10   # get last value
    num=num//10   #avoid last value
    print(num)
    sum+=temp
print(sum)

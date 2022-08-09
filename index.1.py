#x1=int(input("enter x1 "))
#x2=int(input("enter x2 "))
#y1=int(input("enter y1 "))
#y2=int(input("enter y2 "))
#distance=(((x1-x2)**2)+((y2-y1)**2))**.5
#print(distance)


#num=int(input("enter number"))
#bina=(bin(num))
#print(bina)


#oct=(oct(num))
#print(oct)


#num=5
#spaces=5
#row
#for row in range(1,num+1):
 #   #space
  #  for space in range(1,spaces):
   #     print("",end="")
    #spaces-=1
    #col
    #for col in range(1,row+1):
     #   print("*",end=" ")
    #print()





num=5
spaces=5
#row
for row in range(num,0,-1):
    #space
    for space in range(1,spaces):
        print("",end="")
    spaces+=1
    #col
    for col in range(1,row+1):
        print("*",end=" ")
    print()


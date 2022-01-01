a=int(input("Enter Number: "))
print("Is the number Prime?")
def prime(num):
    if(num==1):
        return False
    elif(num==2):
        return True
    else:
        for x in range(2,num):
             if(num%x==0):
                 return False
             return True
print(prime(a))     

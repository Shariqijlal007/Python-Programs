a=int(input("Enter a : "))
b=int(input("Enter b : "))
def swap(x,y):
    temp=x
    x=y
    y=temp
    print("A = ",x,"B = ",y)
swap(a,b)

list_1=[]
n=int(input("Enter size of list:"))
for x in range(0,n):
    print("Enter value at a[",x,"]=",end='')
    a=int(input())
    list_1.append(a)
print("Main list=",list_1)
list_2=[]
list_3=[]
for f in range(1,n+1):
    if(f<=(n/2)):
        list_2.append(list_1[f-1])
    else:
        list_3.append(list_1[f-1])
print("Sub list 2 =",list_2)
print("Sub list 3 =",list_3)

list_1=[90,87,23,3,8,34,67,75,1,2,3,4,34,34,2]
n=15
b=int(input("Enter number to check:"))
for f in range(0,n):
    if(list_1[f]==b):
        print("Found at index:",f)
        continue
    else:
        pass
print("The Integer List is=",list_1)

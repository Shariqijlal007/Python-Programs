a=[1,2,3,4,5]
print("list is : ",a)
def product(a):
    q=1
    x=0
    while(x<len(a)):
     p=a[x]*q
     q=p
     x=x+1
    print("product of list is : ",q)
product(a)

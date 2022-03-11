# Implement a bonary search:
def bsearch(l,key):
    i=0
    j=len(l)-1
    flag=0
    while i<=j and flag==0:
        mid=i+j//2
        if l[mid]==key:
            flag=flag+1
            pos=mid+1
        elif l[mid]>key:
            j=mid-1
        elif l[mid]<key:
            i=mid+1
    if flag==1:
        print("key found at %d position."%(pos))
    else:
        print("not found")
    


n=int(input("enter size of the list:"))
l=[]
for i in range(n):
    val=int(input("enter value in a sorted form:"))
    l.append(val)
print(l)
key=int(input("enter number to be search:"))
bsearch(l,key)

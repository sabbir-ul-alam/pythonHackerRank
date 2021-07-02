superSet=set(map(int,input().split()))
n= int(input())
flag=1
for i in range(n):
    subSet=set(map(int,input().split()))
    res=subSet.intersection(superSet)
    if len(res)!=len(subSet):
        flag=0
    elif len(res)==len(superSet):
        flag=0
if flag==1:
    print("True")
else:
    print("False")
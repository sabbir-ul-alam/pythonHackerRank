import itertools
k,m=input().split()
k=int(k)
m=int(m)
mega_list=[]
for i in range(k):
    ls=list(map(int,input().split()))
    mega_list.append(ls[1:])
product_list=list(itertools.product(*mega_list))
max=0
for i in product_list:
    sum=0
    for j in i:
        #print(j,end="")
        sum=sum+pow(j,2)
    if sum%m>max:
        max=sum%m
    #print("####",sum,"####",max)

print(max)

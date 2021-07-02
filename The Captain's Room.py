n=int(input())
room=list(map(int,input().split()))
min=10000
count=dict()
for i in room:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1

for k,v in count.items():
    if v==1:
        print(k)
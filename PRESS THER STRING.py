strr=input()
length=len(strr)
i=0
res=[]
while(i<length):
    count=0
    val=strr[i]
    for j in range(i,length):
        if strr[i]==strr[j]:
            count=count+1
            #print("match",strr[i],i)
            if j==length-1:
                i=length+1
        else:
            i=j
            #print("no match", strr[i], i)
            break
    res.append('('+str(count)+', {}'.format(val)+')')
print(*res)
import itertools
n=int(input())
ls=list(input().split(" "))
#print(ls)
k=int(input())
index_for_a=[x for x in range(len(ls)) if ls[x]=='a']
#print(index_for_a)
permutations=list(itertools.combinations([x for x in range(len(ls))],k))
#print(permutations)
count=set()
for n in index_for_a:
    for k in permutations:
        try:
            ind=k.index(n)
            #print(k,"n={}".format(n), "ind={}".format(ind))
            count.add(k)
        except:
            pass
#print(len(count))
print(len(count)/len(permutations))

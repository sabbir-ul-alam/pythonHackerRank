import collections
line=list(input())
line_dic=dict(collections.Counter(sorted(line)))
#print(line_dic)
line_dcc=collections.OrderedDict(sorted(line_dic.items(),reverse=1,key=lambda kv:kv[1]))
#print(line_dcc)
for  i,j in enumerate(line_dcc.items(),start=1):
    print(j[0],j[1])
    if i==3:
        break


#for i in range(len(key_list)):



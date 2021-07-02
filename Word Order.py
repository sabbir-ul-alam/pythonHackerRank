import collections
n=int(input())
list_of_words=[]
for i in range(n):
    line=input()
    list_of_words.append(line)
list_of_keys=collections.Counter(list_of_words).keys()
list_of_val=collections.Counter(list_of_words).values()

print(len(list_of_keys))
print(*list_of_val)
#print(collections.Counter(list_of_words))

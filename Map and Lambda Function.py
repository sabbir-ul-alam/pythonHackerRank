def fib(n):
    a=0
    b=1
    res=[0]
    for i in range(n-1):
        res.append(b)
        tmp=a
        a=b
        b=tmp+b
    return res


n=int(input())
#print(fib(n))
# res=lambda x:x for x in range(1,n) x=x
if n==0:
    print([])
else:
    print(list(map(lambda x:pow(x,3),fib(n))))

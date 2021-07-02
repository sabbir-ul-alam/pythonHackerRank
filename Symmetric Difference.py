if __name__ == '__main__':
    m=int(input())
    mSet=set(map(int,input().split()))
    n = int(input())
    nSet = set(map(int, input().split()))
    lm=mSet.difference(nSet)
    ln =nSet.difference(mSet)
    res=lm.union(ln)
    res=sorted(list(res))

    print(*res,sep="\n")


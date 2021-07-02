if __name__ == '__main__':
    n,m=map(int,input().split())
    ls=list(map(int,input().split()))
    nset=set(map(int,input().split()))
    mset = set(map(int, input().split()))
    h=0
    nsetLen=m
    msetLen=m
    for i in ls:
        nset.add(i)
        mset.add(i)
        if len(nset)==nsetLen:
            h=h+1
        if len(mset)==msetLen:
            h=h-1
        if len(mset)!=msetLen and len(nset)!=nsetLen:
            # msetLen=len(mset)
            # nsetLen=len(nset)
            nset.remove(i)
            mset.remove(i)
        elif len(nset)!=nsetLen:
            nset.remove(i)
        #     nsetLen=len(nset)
        elif len(mset)!=msetLen:
            mset.remove(i)
        #     msetLen=len(mset)
    print(h)
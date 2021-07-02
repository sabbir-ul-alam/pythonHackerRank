if __name__ == '__main__':
    n=int(input())
    ls=map(int,input().split())
    tp=tuple(ls)
    print(tp.__hash__())

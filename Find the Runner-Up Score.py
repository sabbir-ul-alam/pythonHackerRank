if __name__=="__main__":
    n=int(input())
    arr=map(int,input().split())
    ####enumerate always comes first
    arrList={x for c,x in enumerate(arr) if c <n}
    sorted_list=sorted(arrList)
    print(sorted_list[len(sorted_list)-2])


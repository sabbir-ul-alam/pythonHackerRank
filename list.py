def insert(ls,val):
    value=val[1]
    ind=val[0]
    ls.insert(ind,value)

def print_list(ls):
    print(ls)

def remove(ls,val):
    value=val[0]
    ls.remove(value)

def append(ls,val):
    value=val[0]
    ls.append(value)

def sort(ls):
    ls.sort()

def pop(ls):
    ls.pop()

def reverse(ls):
    ls.reverse()

if __name__ == '__main__':
    main_list=[]
    N = int(input())
    for _ in range(N):
        cmd,*line=input().split()
        val=list(map(int,line))
        if cmd=="insert":
            insert(main_list,val)
        elif cmd=="print":
            print_list(main_list)
        elif cmd=="remove":
            remove(main_list,val)
        elif cmd=="append":
            append(main_list,val)
        elif cmd=="sort":
            sort(main_list)
        elif cmd=="pop":
            pop(main_list)
        elif cmd=="reverse":
            reverse(main_list)




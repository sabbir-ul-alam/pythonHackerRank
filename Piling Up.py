from  collections import deque
t=int(input())
for i in range(t):
    n=int(input())
    line_input=deque(map(int,input().split()))

    flag=0
    max=0
    if n==1:
        print("Yes")
        continue
    left=line_input.popleft()
    right=line_input.pop()
    if left>=right:
        max=left
        line_input.append(right)
    else:
        max=right
        line_input.appendleft(left)


    while(True):
        max_min = 0
        if len(line_input)==1:
            max_min=line_input.pop()
            if max_min > max:
                flag = 1
            else:
                max = max_min
            break





        left = line_input.popleft()
        right = line_input.pop()
        if left >= right:
            max_min = left
            line_input.append(right)
        else:
            max_min = right
            line_input.appendleft(left)
        if max_min>max:
            flag=1
        else:
            max=max_min



    if flag==1:
        print("No")
    else:
        print("Yes")


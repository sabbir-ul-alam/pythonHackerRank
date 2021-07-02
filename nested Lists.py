if __name__ == '__main__':
    student_list=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student=[name,score]
        student_list.append(student)

    for x in range(len(student_list)):
        for y in range(len(student_list)):
            if student_list[x][1]>=student_list[y][1]:
                #print(student_list[x][1],student_list[y][1])
                tmp=student_list[y]
                student_list[y]=student_list[x]
                student_list[x]=tmp
    #print(student_list)
    min=student_list[len(student_list)-1]
    min2=-1
    lowest=[]
    for x in range(len(student_list)-1,-1,-1):
        #print(student_list[x][1],min[1])
        if student_list[x][1]>min[1]:
            min2=student_list[x][1]
            break
    #print(min2)
    if min2==-1:
        for x in sorted(student_list):
            print(x[0])
    else:
        lowest=[x for x in student_list if x[1]==min2]
        #print(lowest)
        res=sorted(lowest)
        for x in res:
            print(x[0])
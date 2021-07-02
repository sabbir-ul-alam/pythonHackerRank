def solve(s):
    line=list(s)
    res=[]
    for i in range(len(line)):
        if line[i]>='a' and  line[i]<='z':
            if i-1<0 or line[i-1]==" ":
                line[i]=line[i].upper()
    return  "".join(line)



if __name__ == '__main__':
    s = input()
    result = solve(s)

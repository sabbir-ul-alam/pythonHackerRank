def swap_case(s):
    tmp=""
    for i in s:
        if i >="A" and i <="Z":
            tmp=tmp+i.lower()
        elif i>='a' and i<='z':
            tmp=tmp+i.upper()
        else:
            tmp=tmp+i
    return tmp

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
def minion_game(string):
    # your code goes here
    length=len(string)
    kev=0
    st=0
    for i in range(length):
        if string[i]=='A' or string[i]=='E' or string[i]=='I' or string[i]=='O' or string[i]=='U':

                tmp=length-i                #print(tmp)
                kev=kev+tmp


        else:
                ctmp=length-i
                st=st+ctmp
    if st>kev:
        print("Stuart {}".format(st))
    elif kev >st:
        print("Kevin {}".format(kev))
    else:
        print("Draw")




if __name__ == '__main__':
    s = input()
    minion_game(s)
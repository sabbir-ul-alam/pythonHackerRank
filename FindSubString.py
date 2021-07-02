def count_substring(main,sub):
    count=0
    while True:
        #print(main)
        ind=main.find(sub)
        #print(ind)
        main=main[ind+len(sub):]

        if ind<0:
            return count
        count = count + 1


if __name__=="__main__":
    mainString=input()
    subString=input()
    print(count_substring(mainString,subString))
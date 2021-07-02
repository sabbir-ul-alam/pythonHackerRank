def merge_the_tools(string, k):
    # your code goes her

    startIndex=0
    endIndex=k
    while True:
        res = {}
        for x in range(startIndex,endIndex):
            res[string[x]]=string[x]
        for x in res:
            print(x,end="")

        startIndex=startIndex+k
        endIndex=endIndex+k
        #print(startIndex, endIndex)
        if endIndex > len(string):
            break
        else:
            print("")




if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
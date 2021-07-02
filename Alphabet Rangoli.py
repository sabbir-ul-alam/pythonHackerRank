def print_rangoli(size):
    # your code goes here

    col=2*size-2+1+2*size-2
    row=2*size-1
    ##top
    dash=2*size-2
    val=chr(ord("a")+size-1)
    step=0

    for i in range((row//2)):
        falg = 1
        val = chr(ord("a") + size - 1)
        lowerVal=chr(ord(val)-i)
        #print(lowerVal)
        print("".ljust(dash,"-"),end="")
        for x in range(i+step+1):
            if x%2!=0:
                print("-",end="")
            else:
                if val>lowerVal and falg==1:
                    print(val,end="")
                    val=chr(ord(val)-1)
                else:
                    falg = 0
                    print(val, end="")
                    val = chr(ord(val) + 1)


        print("".ljust(dash, "-"))
        dash=dash-2
        step = step + 3
    #middle
    val = chr(ord("a") + size - 1)
    falg=1
    for i in range(col):
        if i%2!=0:
            print("-",end="")
        else:
            if val>'a' and falg==1:
                print(val,end="")
                val=chr(ord(val)-1)
            else:
                falg=0
                print(val,end="")
                val=chr(ord(val)+1)
    #bottom
    print("")
    dash = 2
    step = 4*size-7
    for i in range((row // 2), 0, -1):
        falg = 1
        val = chr(ord("a") + size - 1)
        lowerVal = chr(ord(val) - i+1)
        #print(i,lowerVal)
        print("".ljust(dash, "-"), end="")
        for x in range(step):
            if x % 2 != 0:
                print("-", end="")
            else:
                if val > lowerVal and falg == 1:
                    print(val, end="")
                    val = chr(ord(val) - 1)
                else:
                    falg = 0
                    print(val, end="")
                    val = chr(ord(val) + 1)

        print("".ljust(dash, "-"))
        dash = dash + 2
        step = step - 4



if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
if __name__ == '__main__':
    row,col=input().split(" ")
    row=int(row)
    col=int(col)
    #print(row, col)

    #upper  side
    wD = (col - 3) // 2
    wL = 1
    for i in range(1,row//2+1):
        print("-"*wD+".|."*wL+"-"*wD)
        wL=wL+2
        wD=wD-3
    print("WELCOME".center(col,"-"))
    #lowwer side
    wD = 3
    wL = (col-2*wD)//3
    for i in range(1, row // 2 + 1):
        print("-" * wD + ".|." * wL + "-" * wD)
        wL = wL - 2
        wD = wD + 3


import  re
if __name__ == '__main__':
    t=int(input())
    for i in range(t):
        line=input()
        try:
         re.compile(line)
         print("True")
        except :
            print('False')

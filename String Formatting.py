def print_formatted(number):
    # your code goes here
    ln=len(bin(number))-2

    for i in range(1,number+1):
        print("{0:{wd}d} {0:{wd}o} {0:{wd}X} {0:{wd}b}".format(i,wd=ln))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
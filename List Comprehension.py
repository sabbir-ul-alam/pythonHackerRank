if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    #[ expression-involving-loop-variable for loop-variable in sequence ]
    #[ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ]
    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ])




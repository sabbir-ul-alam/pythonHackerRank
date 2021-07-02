def wrapper(f):
    def fun(l):
        # complete the function
        res=[]
        #str='abc'
        #str.startswith('a')
        for i in l:
            if len(i)>10:
             if i.startswith('+91'):
                 tmp=list(i)
                 tmp.insert(3,' ')
                 tmp.insert(9,' ')
                 res.append("".join(tmp))
             elif i.startswith('91'):
                 tmp=list(i)
                 tmp.insert(0,'+')
                 tmp.insert(3, ' ')
                 tmp.insert(9, ' ')
                 res.append("".join(tmp))
             elif i.startswith('0'):
                 tmp = list(i)
                 tmp.pop(0)
                 tmp.insert(0, '+')
                 tmp.insert(1, '9')
                 tmp.insert(2, '1')
                 tmp.insert(3, ' ')
                 tmp.insert(9, ' ')
                 res.append("".join(tmp))
            else:
                tmp=list(i)
                tmp.insert(0, '+')
                tmp.insert(1, '9')
                tmp.insert(2, '1')
                tmp.insert(3, ' ')
                tmp.insert(9, ' ')
                res.append("".join(tmp))

        #print(*res)
        return f(res)



    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)



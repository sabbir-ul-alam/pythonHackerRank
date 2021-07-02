import cmath
line=complex(input())
x=line.real
y=line.imag

# op=""
# for x in line:
#     if x=='+' or x=='-':
#         op=x
# x,y=line.split(op)
# x=int(x)
# y=int(str(y).split('j')[0])
print(abs(complex(x,y)))
print(cmath.phase(complex(x,y)))



y=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x)
print(y('s'))
print(y('1'))
print(y('2'))
print(y('3'))
print(y('4'))

####
#print(*(sorted(input(), key=lambda x: (x.isdigit(), x.isdigit() and int(x)%2==0, x.isupper(), x.islower(), x))), sep='')
####
#Key paremeter is sued to determin te priority. Here isupper has more
#priority than islower. So when comparing lower and upper value. Upper will be at the end
#for ascending order. But here 'x' is used to compare values who have same priority.
#and after chosing priority sorts the poiter based on pririty.
#And later returns the value from the pointer.
# this mechanism is called TimSiort
tuple=(1,2,3,4)
print(tuple[0:2])
print(tuple[2:4])

tuple=(2,3,4,5,6,7,8,9,9)
t,*k=tuple
print(k)
print(t)
print(len(tuple))
print(tuple[2])
print(tuple.count(9))

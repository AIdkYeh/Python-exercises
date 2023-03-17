L=list(range(10))
even=[]

for i in L:
    if i%2 ==0:
        even.append(i)
        L.pop(L.index(i))
L.extend(even)
print(L)

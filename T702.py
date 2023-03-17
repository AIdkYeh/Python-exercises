def fact(x):
    ttl=1
    for i in range(1,int(x)+1):
        ttl*=i
    return ttl

x = input() # 4
if x.isdigit() == True:
    print(fact(x))
else:
    print(x+'是一個不合法的輸入，無法運算')

def f(*arg):
    ttl=0
    for i in arg:
        ttl+=i
    return ttl
print(f(1, 2, 3)) # 6
print(f(1, 2, 3, 4, 5)) # 15

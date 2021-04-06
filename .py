def func(n):
    if n == 0:
        return ()
    else:
        return func(n-1)

print(func(5))
print(func(20))
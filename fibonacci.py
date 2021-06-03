def fibonacci(n):
    if(n <= 1):
        return n
    return fibonacci(n-1) + fibonacci(n-2)


i = 0

while True:
    n = fibonacci(i)
    if n > 100:
        break
    else:
        print(n)
        
        i = i + 1
        continue

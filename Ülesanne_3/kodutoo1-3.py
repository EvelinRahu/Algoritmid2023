def fibonacci(n):
    if n <= 1:
        return n 
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Sisesta number: "))

if n < 0:
    print("Sisestatud arv peab olema positiivne täisarv!")
else:
    print(n, ".Fibonacci arv on:", fibonacci(n))

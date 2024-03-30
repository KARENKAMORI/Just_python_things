# KARENKAMORI 
# 30/03/2021

# python implementation of the fibonacci series
def main():
    n = int(input("Fibonacci size: "))
    print(fibonacci(n))

# fibonacci function implementation
def fibonacci(n):
    fibonacci_list = []
    a = 0
    b = 1
    i = 0 # for while loop iteration

    fibonacci_list.append(a)
    fibonacci_list.append(b)

    while i < n:
        x = b # temporarily holds current value of b before the arithmetic operation modification.
        b= a + b
        a = x
        fibonacci_list.append(b)
        i += 1

    return fibonacci_list

if __name__ == "__main__":
    main()

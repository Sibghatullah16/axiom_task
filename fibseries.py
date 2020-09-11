def fib(n):
    number1 = 0
    number2 = 1

    if n < 1:
        return -1

    if n == 1:
        return number1

    if n == 2:
        return number2

    count = 3
    while count <= n:
        fib_n = number1 + number2
        number1 = number2
        number2 = fib_n
        count += 1
    return fib_n
        

  # Replace with your code
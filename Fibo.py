num = int(input("Digite um número: "))
fib1 = 0
fib2 = 1
fib = 0
while fib < num:
    fib = fib1 + fib2
    fib1 = fib2
    fib2 = fib
    print(fib)
if fib == num:
    print(num, "pertence à sequência de Fibonacci.")
else:
    print(num, "não pertence à sequência de Fibonacci.")

commit();

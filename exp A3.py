num = int(input("Enter a number: "))
fac = 1
i = 1

while i <= num:
    fac *= i
    i += 1

print(f"Factorial of {num} is {fac}")

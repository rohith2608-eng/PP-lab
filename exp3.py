# Number is even or not

print("Number is even or not")

n = int(input("Enter the number: "))

if n % 2 == 0:
    print("\nIt's even")
else:
    print("\nIt's odd")


# Finding the factorial of a number

print("\n\n\n# Finding the factorial of a number")

f = int(input("Enter the number: "))

if f < 0:
    print("Factorial not defined for negative numbers")
else:
    fact = 1
    for i in range(1, f + 1):
        fact *= i
    print("Factorial =", fact)


print("print all prime number between interval")

# Prime number check function

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Prime numbers in range

def primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes


start = int(input("\nEnter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers:", primes_in_range(start, end))

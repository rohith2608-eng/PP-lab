num = int(input("Enter a number: "))
original = num
reverse = 0

while num > 0:
    reminder = num % 10
    reverse = (reverse * 10) + reminder
    num = num // 10

if original == reverse:
    print(f"{original} is a Palindrome")
else:
    print(f"{original} is not a Palindrome")

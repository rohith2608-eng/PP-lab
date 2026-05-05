num = int(input("Enter any number: "))
reverse = 0

while num > 0:
    reminder = num % 10
    reverse  = (reverse * 10) + reminder
    num      = num // 10

print(f"Reverse of entered number is: {reverse}")

print("\nValueError Handling")
while True:
    try:
        num = int(input("Input an integer: "))
        print("Input value:", num)
        break
    except ValueError:
        print("Error: Invalid input, input a valid integer.")

print("\nFileNotFoundError Handling")
while True:
    try:
        filename = input("Input a file name: ")
        file = open(filename, 'r')
        print("File contents:")
        print(file.read())
        file.close()
        break
    except FileNotFoundError:
        print("Error: File not found.")

print("\nTypeError Handling")
while True:
    try:
        num1 = float(input("Input the first number: "))
        break
    except ValueError:
        print("Error: Invalid input. Please input a valid number.")

try:
    numbers = input("Enter two numbers separated by comma: ")
    a, b = numbers.split(",")
    a = int(a)
    b = int(b)
    result = a / b
    print("Result is", result)

except Exception:
    print("Error occurred")

else:
    print("No exceptions")

finally:
    print("This will execute no matter what")

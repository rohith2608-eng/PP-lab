try:
    f = open("file1.txt", "x")
    f.close()
except FileExistsError:
    pass

f = open("file1.txt", "w")
f.write("Panimalar Engineering College\n")
f.write("Panimalar")
f.close()

f = open("file1.txt", "r")
print(f.readline(), end="")
print("Readline:")
print(f.readline())
f.close()

f = open("file1.txt", "a")
f.write("\nSuccessfully Inserted")
f.close()

print("Successfully Inserted")

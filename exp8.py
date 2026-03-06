dict_a = {1:'India', 2:'USA', 3:'UK', 4:'Canada'}

print("Dictionary 'dict_a' is...")
print(dict_a)

print("Dictionary 'dict_a' keys...")
for k in dict_a.keys():
    print(k)

print("Dictionary 'dict_a' values...")
for v in dict_a.values():
    print(v)

print("Dictionary 'dict_a' keys&values...")
for k,v in dict_a.items():
    print(k,":",v, sep="")

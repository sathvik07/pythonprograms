s = "bvubuhoioijoih"
unique = []

for x in s:
    if x not in unique:
        unique.append(x)

print (len(unique))
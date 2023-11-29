bilangan_ganjil = []
count = 1

while len(bilangan_ganjil) < 8:
    if count % 2 != 0:
        bilangan_ganjil.append(count)
    count += 1

output = ', '.join(map(str, bilangan_ganjil))
print(output)
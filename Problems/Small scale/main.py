m = []

while True:
    f = input()
    if f == '.':
        break
    m.append(float(f))

print(min(m))
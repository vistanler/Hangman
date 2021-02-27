s = input()

i = 0
c = ""

pun = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for char in s:
    if char not in pun:
        c = c + char

c = c.lower()
print(c)

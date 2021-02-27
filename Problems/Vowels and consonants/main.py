st = input()

t = 0
vow = "aeiou"

while t < len(st):
    if not st[t].isalpha():
        break
    elif st[t] in vow:
        print('vowel')
    else:
        print('consonant')
    t += 1

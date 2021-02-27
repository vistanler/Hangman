# Write your code here
import random

li = ['python', 'java', 'kotlin', 'javascript']
rand = li[random.randint(0, len(li) - 1)]
letters = set(rand)
guessed_letters = set()
st = ""
st1 = ""
i = 0
q = 8
w = 0
g_lost = True
print('H A N G M A N')
print("")


for i in range(len(rand)):
    st = st + '-'
    i = i + 1


while True:
    gs = input('Type "play" to play the game, "exit" to quit: ')
    if gs == 'exit':
        break
    elif gs == 'play':
        while q != 0:
            print(st)
            a = input('Input a letter: ')
            a.replace(' ', '')
            if len(a) > 1:
                print("You should input a single letter")
                print()
                continue
            if (not a[0].isalpha()) or (not a[0].islower()):
                print("Please enter a lowercase English letter")
                print()
                continue

            if (a in st) or (a in guessed_letters):
                print("You've already guessed this letter")
                print()
                # q = q - 1
                # if q == 0:
                #     print('You lost!')
                # print("")
                continue
            guessed_letters = guessed_letters.union([a])
            if a in letters:
                for w in range(len(rand)):
                    if rand[w] == a:
                        st1 = st1 + a
                    else:
                        st1 = st1 + st[w]
                st = st1
                st1 = ""
            else:
                q = q - 1
                if q == 0:
                    print("That letter doesn't appear in the word")
                    print('You lost!\n')
                else:
                    print("That letter doesn't appear in the word")
            print("")
            if st == rand:
                print(st)
                print("You guessed the word!")
                print("You survived!\n")
                g_lost = False
                break

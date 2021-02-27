row = int(input())
col = int(input())

if (row == 1 and col == 1) or (row == 8 and col == 8) or (row == 1 and col == 8) or (row == 8 and col == 1):
    print(3)
elif ((row == 1 or col == 1) or (row == 8 or col == 8)) and ((row or col < 8) or (row or col >1)):
    print(5)
else:
    print(8)
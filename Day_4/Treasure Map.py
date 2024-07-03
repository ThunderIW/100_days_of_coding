line1 = ["⬜️", "️⬜️", "️⬜️"]
line2 = ["⬜️", "⬜️", "️⬜️"]
line3 = ["⬜️️", "⬜️️", "⬜️️"]
map = [line1, line2, line3]

position = input()
column = 0
row = int(position[1]) - 1

if position[0] == 'A':
    column = 0

elif position[0] == 'B':
    column = 1

elif position[0] == 'C':
    column = 2

map[row][column] = 'X'
print(map)

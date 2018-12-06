# advent of Code Day 1 Puzzle 1

with open('Day1Input.txt', 'r') as f:
    content = f.readlines()


seen_numbers = []
new_num = 0
for i in content:
    new_num = new_num + int(i.lstrip('+'))
    seen_numbers.append(new_num)


# Advent of code Day 1 Puzzle 2
'''
seen_numbers = []
new_num = 0
for i in content:
    new_num = new_num + int(i.lstrip('+'))
    if new_num in seen_numbers:
        print(new_num)
    else:
        seen_numbers.append(new_num)
'''

# Part 2


def func():
    sett = set()
    new_num = 0
    while True:
        for i in content:
            new_num += int((i.lstrip()))
            if new_num in sett:
                print('repeat!!: ', new_num)
                return
            sett.add(new_num)


func()

# Part 1
with open('Day2Input.txt') as f:
    content = f.readlines()


def get_occurrences(line):
    count_dict = {}
    for letter in line:
        if letter in count_dict:
            count_dict[letter] += 1
        else:
            count_dict[letter] = 1
    print({k: v for k, v in count_dict.items() if v > 1})
    return {k: v for k, v in count_dict.items() if v > 1}


def count_occurrences(occurrences_dict):
    count_two = 0
    count_three = 0
    for _, v in occurrences_dict.items():
        if v == 2:
            count_two = 1
        if v == 3:
            count_three = 1
    return count_two, count_three

'''
if __name__ == '__main__':
    count_of_two = 0
    count_of_three = 0
    for line in content:
        occurrences = get_occurrences(line)
        two_count, three_count = count_occurrences(occurrences)
        count_of_two += two_count
        count_of_three += three_count
    checksum = count_of_two * count_of_three
    print(checksum)
'''

# ===========================================================================
# Part two

for line in content:
    for selection in content:
        count = 0
        for i in zip(line, selection):
            if i[0] != i[1]:
                count += 1
        if count == 1:
            print(selection)
            print(line)

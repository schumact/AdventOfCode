# definitely not the prettiest.
# part one

with open('Day3input.txt', 'r') as f:
    content = f.readlines()

counter = 0

multi_array = [[0 for i in range(6)] for x in range(6)]


def index_checker(index, end_result, multi_list):
    while not index >= end_result[0]:
        multi_list[index + 1] += 1
        index += 1


for i in content:
    coordinates = (i.rsplit()[2].strip(':').split(','))
    area = i.rsplit()[3].split('x')
    new_tuple = [int(area[0]) + int(coordinates[0]) - 1, int(area[1]) + int(coordinates[1]) - 1]
    coordinates[0] = int(coordinates[0])
    coordinates[1] = int(coordinates[1])
    area[0] = int(area[0])
    area[1] = int(area[1])
    desired_row = multi_array[coordinates[1]]
    while not coordinates[1] > new_tuple[1]:
        desired_row[coordinates[0]] += 1
        index_checker(coordinates[0], new_tuple, desired_row)
        desired_row = multi_array[coordinates[1] + 1]
        coordinates[1] += 1

for row in multi_array:
    for col in row:
        if col >= 2:
            counter += 1

print(counter)

# =======================================================
# Part two:

counter = 0

fabric_area_list = [(0, 0), ]


def cross_check_id_area():
    for idd, _ in fabric_area_list:
        count = 0
        for row in multi_array:
            for col in row:
                if col == idd:
                    count += 1
        if count == _:
            print(f'we found a winner {idd}')


def index_checker2(index, end_result, multi_list, fabric_id):
    '''
    coordinates[0], new_tuple, desired_row
    '''
    while not index >= end_result[0]:
        if multi_list[index + 1] == 0:
            multi_list[index + 1] = fabric_id
        else:
            multi_list[index + 1] = 999
        index += 1


for i in content:
    fabric_id = int(i.strip('#').split(' ')[0])
    coordinates = (i.rsplit()[2].strip(':').split(','))
    area = i.rsplit()[3].split('x')
    fabric_area_list.append((fabric_id, int(area[0]) * int(area[1])))
    new_tuple = [int(area[0]) + int(coordinates[0]) - 1, int(area[1]) + int(coordinates[1]) - 1]
    coordinates[0] = int(coordinates[0])
    coordinates[1] = int(coordinates[1])
    area[0] = int(area[0])
    area[1] = int(area[1])
    desired_row = multi_array[coordinates[1]]  # depth of array
    while not coordinates[1] > new_tuple[1]:  # while current depth isn't equal to final depth
        if desired_row[coordinates[0]] == 0:
            desired_row[coordinates[0]] = fabric_id
        else:
            desired_row[coordinates[0]] = 999
        index_checker2(coordinates[0], new_tuple, desired_row, fabric_id)
        desired_row = multi_array[coordinates[1] + 1]
        coordinates[1] += 1

cross_check_id_area()

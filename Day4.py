from datetime import datetime, timedelta

with open('Day4Input.txt', 'r') as f:
    content = f.readlines()


new_log_list = []
for line in content:
    date_obj = datetime.strptime(line.lstrip('[')
                                 .split(']')[0].rstrip(),
                                 '%Y-%m-%d %H:%M')
    line = line.split('[')[1].split(']')
    line[0] = date_obj
    line[1] = line[1].strip()
    new_log_list.append(line)

new_list = []
for i in sorted(new_log_list):
    if "Guard" in i[1]:
        new_list.append(i[1].split("#")[1].split(" ")[0])
    else:
        if 'falls' in i[1]:
            new_list.append(i[0])
        else:
            new_list[-1] = i[0] - new_list[-1]

dicty = {}
last_guard = ''
for i in new_list:
    if isinstance(i, str):
        last_guard = i
        if i not in dicty:
            dicty[i] = timedelta(0, 0)
    else:
        dicty[last_guard] += i

print(dicty)

largest_v = timedelta(0, 0)
for k, v in dicty.items():
    if v > largest_v:
        largest_v = v
        print(k)

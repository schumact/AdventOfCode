from datetime import datetime

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

print(new_log_list)

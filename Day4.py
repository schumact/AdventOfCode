from datetime import datetime, timedelta
from collections import Counter


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


largest_v = timedelta(0, 0)
most_min_guard = 0
for k, v in dicty.items():
    if v > largest_v:
        largest_v = v
        most_min_guard = int(k)


def get_guard_intervals(guard):
    guard_intervals = []
    last_guardd = ''
    for x in sorted(new_log_list):
        if "Guard" in x[1]:
            last_guardd = x[1].split("#")[1].split(" ")[0]
        else:
            if last_guardd == str(guard):
                guard_intervals.append(x)

    return guard_intervals


intervals = get_guard_intervals(most_min_guard)
intervals_datetimes = []
for t in intervals:
    intervals_datetimes.append(t[0])


def perdelta(start, end, duration):
    current = start
    while current <= end:
        yield current
        current += duration


stack = []
for i, k in zip(intervals_datetimes[0::2], intervals_datetimes[1::2]):
    for y in perdelta(i, k, timedelta(minutes=1)):
        stack.append(y)


minutes_list = [z.minute for z in stack]

most_frequent_min = Counter(minutes_list).most_common(1)
print(most_frequent_min[0][0] * most_min_guard)

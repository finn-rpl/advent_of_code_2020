import json
import time

with open('scores_day5.json', 'r') as jf:
    dd = json.load(jf)

template = []
for i in range(1, 26):
    template.append(str(i)+'.1')
    template.append(str(i)+'.2')

pzls = {}
for m in dd['members']:
    mm = dd['members'][m]
    for j in range(1,26):
        j = str(j)
        for k in range(1,3):
            k = str(k)
            try:
                ts = int(mm["completion_day_level"][j][k]['get_star_ts'])
                if j + '.' + k not in pzls:
                    pzls[j + '.' + k] = {}
                pzls[j + '.' + k][mm['name']] = ts
            except KeyError:
                pass

for p in pzls:
    lb = {k: v for k, v in sorted(pzls[p].items(), key=lambda item: item[1])}
    print(p)
    for m in lb:
        mj = m + '                '
        print(mj[:15], end = ': ')
        print(time.ctime(lb[m]))


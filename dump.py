

def read_list(input_file, data_type=str):
    with open(input_file, 'r') as listf:
        lines = listf.read().strip('\n').split('\n')
        out = []
        for line in lines:
            out.append(data_type(line))
        return out


def find_two_sums(input_list, desired_total):
    for i in input_list:
        for k in input_list:
            if i+k == desired_total:
                return i*k


def find_three_sums(input_list, desired_total):
    for i in input_list:
        for j in input_list:
            for k in input_list:
                if i+j+k == desired_total:
                    return i*j*k


# print(find_two_sums(read_list('day1.csv', int),2020))
# print(find_three_sums(read_list('day1.csv',int),2020))

def read_xsv(input_file, rowdelim='\n', coldelim=' '):
    with open(input_file, 'r') as xsvf:
        lines = xsvf.read().strip('\n').split(rowdelim)
        return [line.split(coldelim) for line in lines]


def password_validation(input_data):
    valid_passwords = 0
    for line in input_data:
        bounds = line[0].split('-')
        char = line[1][0]
        pw = line[2]
        if int(bounds[0]) <= pw.count(char) <= int(bounds[1]):
            valid_passwords += 1
    return valid_passwords


def password_validation2(input_data):
    valid_passwords = 0
    for line in input_data:
        bounds = line[0].split('-')
        char = line[1][0]
        pw = line[2]
        if (pw[int(bounds[0])-1] == char) != (pw[int(bounds[1])-1] == char):
            valid_passwords += 1
    return valid_passwords

# print(password_validation1(read_xsv('day2.csv')))
# print(password_validation2(read_xsv('day2.csv')))


def tree_hit(input_data, xs, ys):
    x = xs
    y = ys
    out = 0
    while y <= len(input_data)-1:
        if x >= len(input_data[0]):
            x = x - len(input_data[0])
        if input_data[y][x] == '#':
            out += 1
        x += xs
        y += ys
    return out

# d3 = read_list('day3.csv')
# print(tree_hit(d3, 3, 1))
# print(tree_hit(d3, 1, 1) * tree_hit(d3, 3, 1) * tree_hit(d3, 5, 1) * tree_hit(d3, 7, 1) * tree_hit(d3, 1, 2))


def read_batch(input_file):
    with open(input_file, 'r') as file:
        out = []
        f = file.read()
        f = f.split('\n\n')
        for line in f:
            line = line.replace('\n', ' ').strip(' ')
            lines = [line.split(':') for line in line.split(' ')]
            out.append({k: v for k, v in lines})
    return out


d4 = read_batch('day4/day4.csv')
required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eyecols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']


def day4(input_dict):
    n = 0
    for p in input_dict:
        brk = False
        for r in required:
            if r not in p.keys():
                brk = True
        if brk:
            continue
        if len(p['hcl']) != 7 or p['hcl'][0] != '#':
            continue
        if 1920 > int(p['byr']) \
                or int(p['byr']) > 2020 \
                or 2010 > int(p['iyr']) \
                or int(p['iyr']) > 2020 \
                or 2020 > int(p['eyr']) \
                or int(p['eyr']) > 2030:
            continue
        if p['hgt'][-2:] == 'in':
            if 59 > int(p['hgt'][:-2]) or int(p['hgt'][:-2]) > 76:
                continue
        elif p['hgt'][-2:] == 'cm':
            if 150 > int(p['hgt'][:-2]) or int(p['hgt'][:-2]) > 193:
                continue
        else:
            continue
        if p['ecl'] not in eyecols or len(p['pid']) != 9:
            continue
        n += 1
    return n


# print(day4(d4))


# d5 = read_list('day5/day5.csv')
ind = {0: 64, 1: 32, 2: 16, 3: 8, 4: 4, 5: 2, 6: 1, 7: 4, 8: 2, 9: 1}
# NOTE: [[0]*8]*128 != [[0 for i in range(8)] for i in range(128)]
seats = [[0 for i in range(8)] for j in range(128)]  # pt2 addition


def day5(input_list):
    ids = []  # pt2 addition
    highest = 0
    for bp in input_list:
        row = 0
        col = 0
        for i in range(len(bp)):
            if bp[i] == 'B':
                row += ind[i]
            elif bp[i] == 'R':
                col += ind[i]
        pid = (row*8)+col  # pt2 addition
        if pid > highest:
            highest = pid
        ids.append(pid)  # pt2 addition
        seats[row][col] = 1  # pt2 addition
    print(highest)
    for i in range(len(seats)):  # pt2 addition
        for j in range(len(seats[i])):  # pt2 addition
            if seats[i][j] == 0 and (i*8)+j-1 in ids and (i*8)+j+1 in ids:  # pt2 addition
                print((i*8)+j)  # pt2 addition


# day5(d5)

def read_day6(input_file):
    with open(input_file, 'r') as file:
        out = []
        f = file.read()
        f = f.split('\n\n')
        for line in f:
            group = line.strip(' ').strip('\n')
            people = [i for i in group.split('\n')]
            out.append(people)
    return out


# d6 = read_day6('day6/day6.csv')


def day6(input_list):
    count1 = 0
    count2 = 0
    for g in input_list:
        dd = {}
        for p in g:
            for q in p:
                if q in dd:
                    dd[q] += 1
                else:
                    dd[q] = 1
        count1 += len(dd)
        for i in dd:
            if dd[i] == len(g):
                count2 += 1
    print(count1)
    print(count2)
    pass

# day6(d6)


# od6 = read_list('2019day6/2019day6.csv')


def oldday6(input_list):
    dd = {}
    links = []
    count = 0
    for i in input_list:
        k, v = i.split(')')
        links.append((k, v))
        if k in dd:
            dd[k].append(v)
        else:
            dd[k] = [v]

    tree = [['COM']]
    added = []
    while len(added) != len(dd):
        for i in list(tree):
            branch = i[-1]
            if branch in dd and branch not in added:
                for j in dd[branch]:
                    newentry = i.copy()
                    newentry.append(j)
                    tree.append(newentry)
                added.append(branch)

    path = {}
    for i in tree:
        count += len(i) - 1
        if i[-1] in ['YOU', 'SAN']:
            for j in i[:-1]:
                if j not in path:
                    path[j] = 0
                else:
                    path[j] = 1

    print(count)
    print(len([i for i in path if path[i] == 0]))


# oldday6(od6)

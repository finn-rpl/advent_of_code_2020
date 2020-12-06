import utils

def day4(input_dict):
    required = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eyecols = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    n = 0
    n2 = 0
    for p in input_dict:
        brk = False
        for r in required:
            if r not in p.keys():
                brk = True
        if brk:
            continue
        n += 1

        ## PART 2

        if len(p['hcl']) != 7 or p['hcl'][0] != '#':
            continue
        if 1920 > int(p['byr']) or int(p['byr']) > 2020 or 2010 > int(p['iyr']) or int(p['iyr']) > 2020 or 2020 > int(p['eyr']) or int(p['eyr']) > 2030:
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
        n2 += 1
    return n, n2


if __name__ == '__main__':
    d4 = utils.read_batch('day4.csv')
    print(day4(d4))
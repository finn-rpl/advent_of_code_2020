import utils

def day7tree(input_list):
    dd = {}

    for line in input_list:
        kv = line.split(' contain ')
        vlist = kv[1].strip('.').split(',')
        vdict = {}
        if not vlist == ['no other bags']:
            for i in vlist:
                i = i.strip(' ').split(' ')
                key = ' '.join(i[1:-1])
                vdict[key] = int(i[0])
        dd[kv[0][:-5]] = vdict

    return dd


def day7(input_list):

    dd = day7tree(input_list)

    paths = ['shiny gold']
    past = -1
    while len(paths) != past:
        past = len(paths)
        for k in dd:
            for v in dd[k]:
                if v in paths and k not in paths:
                    paths.append(k)

    return len(paths)-1

def day7pt2(input_list):

    dd = day7tree(input_list)

    paths = ['shiny gold']
    parents = []
    past = -1
    while len(paths) != past:
        past = len(paths)
        added = []
        for k in paths:
            if k in paths and k not in parents:
                added.append(k)
                for v in dd[k]:
                    for i in range(dd[k][v]):
                        paths.append(v)
            for v in dd[k]:
                if v in paths and k not in paths:
                    paths.append(k)
        parents.extend(added)

    return len(paths)-1


if __name__ == '__main__':

    d7 = utils.read_list('day7.csv')

    print(day7(d7))
    print(day7pt2(d7))
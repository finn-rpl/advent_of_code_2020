import utils

def day7pairs(input_list):
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

    dd = day7pairs(input_list)

    tree = ['shiny gold']
    past = -1
    while len(tree) != past:
        past = len(tree)
        for k in dd:
            for v in dd[k]:
                if v in tree and k not in tree:
                    tree.append(k)

    return len(tree)-1

def day7pt2(input_list):

    dd = day7pairs(input_list)

    tree = ['shiny gold']
    parents = []
    past = -1
    while len(tree) != past:
        past = len(tree)
        new_parents = []
        for k in tree:
            if k in tree and k not in parents:
                new_parents.append(k)
                for v in dd[k]:
                    for i in range(dd[k][v]):
                        tree.append(v)
            for v in dd[k]:
                if v in tree and k not in tree:
                    tree.append(k)
        parents.extend(new_parents)

    return len(tree)-1


if __name__ == '__main__':

    d7 = utils.read_list('day7.csv')

    print(day7(d7))
    print(day7pt2(d7))
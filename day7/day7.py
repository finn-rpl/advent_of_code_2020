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


def build_tree(dict_pairs):
    tree = ['shiny gold']
    past = -1

    while len(tree) != past:
        past = len(tree)
        for k in dict_pairs:
            for v in dict_pairs[k]:
                if v in tree and k not in tree:
                    tree.append(k)

    return tree


def build_tree_reverse_recursive(dict_pairs):
    tree = ['shiny gold']
    parents = []
    past = -1

    while len(tree) != past:
        past = len(tree)
        new_parents = []
        for k in tree:
            if k in tree and k not in parents:
                new_parents.append(k)
                for v in dict_pairs[k]:
                    for i in range(dict_pairs[k][v]):
                        tree.append(v)
            for v in dict_pairs[k]:
                if v in tree and k not in tree:
                    tree.append(k)
        parents.extend(new_parents)

    return tree


def main():

    d7 = utils.read_list('day7.csv')
    pairs_dictionary = day7pairs(d7)

    print(len(build_tree(pairs_dictionary))-1)

    print(len(build_tree_reverse_recursive(pairs_dictionary)) - 1)


if __name__ == '__main__':
    main()

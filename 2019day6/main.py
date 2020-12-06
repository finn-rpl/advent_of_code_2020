import utils

def dict_branches(links):
    out = {}
    for k, v in links:
        if k in out:
            out[k].append(v)
        else:
            out[k] = [v]
    return out

def list_branches(link_dict, root):
    tree = [[root]]
    added = []
    while len(added) != len(link_dict):
        for i in list(tree):
            branch = i[-1]
            if branch in link_dict and branch not in added:
                for j in link_dict[branch]:
                    newentry = i.copy()
                    newentry.append(j)
                    tree.append(newentry)
                added.append(branch)
    return tree

def oldDay6(links):
    count = 0

    tree = dict_branches(links)

    tree = list_branches(tree, 'COM')

    path = {}
    for i in tree:
        # PART 1
        count += len(i) - 1

        # PART 2
        if i[-1] in ['YOU', 'SAN']:
            for j in i[:-1]:
                if j not in path:
                    path[j] = 0
                else:
                    path[j] = 1

    return count, len([i for i in path if path[i] == 0])

if __name__ == '__main__':
    od6 = utils.read_xsv('2019day6.csv', coldelim=')')

    print(oldDay6(od6))

def read_list(input_file, data_type=str):
    with open(input_file, 'r') as listf:
        lines = listf.read().strip('\n').split('\n')
        out = []
        for line in lines:
            out.append(data_type(line))
        return out

def read_xsv(input_file, rowdelim='\n', coldelim=' '):
    with open(input_file, 'r') as xsvf:
        lines = xsvf.read().strip('\n').split(rowdelim)
        return [line.split(coldelim) for line in lines]

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

def get_advent_input(day):
    day = str(day)
    try:
        open('d'+day+'.csv')
    except FileNotFoundError:
        import requests
        with open('login.txt') as lf:
            login = lf.read().strip('\n')
        r = requests.get('https://adventofcode.com/2020/day/'+day+'/input',cookies={'session':login})
        with open('d'+day+'.csv', 'w+') as f:
            f.write(r.text)
            print(r.elapsed)

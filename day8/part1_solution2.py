import utils


class GameIterator:
    def __init__(self, input_list):
        self.instructions = input_list

    def __iter__(self):
        self.line = -1
        return self

    def __next__(self):
        instruction = self.instructions[self.line]
        if instruction[0] == 'jmp':
            self.line += int(instruction[1])
        else:
            self.line += 1
        try:
            self.instructions[self.line]
        except IndexError:
            raise StopIteration
        return self.line


def run(input_list, raise_errors=True):
    acc = 0
    history = []
    for line in iter(GameIterator(input_list)):
        if line in history:
            if not raise_errors:
                return acc
            else:
                raise StopIteration
        history.append(line)
        if input_list[line][0] == 'acc':
            acc += int(input_list[line][1])
    return acc


def main():
    d8 = utils.read_xsv('day8.csv')
    print(run(d8, raise_errors=False))


if __name__ == '__main__':
    main()

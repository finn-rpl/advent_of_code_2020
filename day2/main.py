import utils


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


if __name__ == '__main__':
    print(password_validation(utils.read_xsv('day2.csv')))
    print(password_validation2(utils.read_xsv('day2.csv')))
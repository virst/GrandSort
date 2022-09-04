import random
import string


def get_random_string(length):
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(length))
    return result_str


def get_random_string_list(length):
    rez_list = []
    for i in range(length):
        rez_list.append(get_random_string(random.randint(20, 200)))
    return rez_list


def make_file(length):
    #str_list = get_random_string_list(int(length / 10))
    str_list = get_random_string_list(1000)
    fn = "L" + str(length) + ".txt"
    f = open(fn, 'w')
    for i in range(length):
        f.write(str(random.randint(0, 10000)) + ". " + random.choice(str_list) + '\n')
    f.close()
    return fn

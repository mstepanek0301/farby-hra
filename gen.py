from random import randrange

def gen(total):
    split_1, split_2 = sorted((
        randrange(total), randrange(total)
    ))

    r = split_1
    g = split_2 - split_1
    b = total - split_2

    return r, g, b

print('[' + ','.join([
    '[' + ','.join(map(str, gen(10))) + ']'
    for _ in range(10)
]) + ']')

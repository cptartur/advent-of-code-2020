import itertools

def apply_mask(mask, value):
    value = list(f'{int(value):036b}')
    for i, c in enumerate(mask):
        if c == '1':
            value[i] = '1'
        elif c == 'X':
            value[i] = 'X'
    return ''.join(value)

def write_to_memory(d, addr, value):
    xs = addr.count('X')
    for x in itertools.product('01', repeat=xs):
        a = addr
        for i in x:
            a = a.replace('X', i, 1)
        d[int(a, 2)] = value

with open(r'days\14\input.txt', 'r') as f:
    t = [i for i in f if i != '']
    d = {}
    mask = ''
    for i in t:
        inst, _, value = i.split()
        if inst == 'mask': 
            mask = value
        else:
            inst, addr = inst.rstrip(']').split('[')
            value = int(value)
            addr = apply_mask(mask, addr)
            write_to_memory(d, addr, value)
    print(sum(d.values()))

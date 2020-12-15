def apply_mask(mask, value):
    digits_to_change = mask.replace('1', '0').replace('X', '1')
    mask = mask.replace('X', '0')
    digits_to_change = int(digits_to_change, 2)
    mask = int(mask, 2)
    return (value & digits_to_change) | mask

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
            addr = int(addr)
            value = int(value)
            value = apply_mask(mask, value)
            d[addr] = value
    print(sum(d.values()))

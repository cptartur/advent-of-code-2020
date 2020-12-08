with open(r'days\8\input.txt', 'r') as f:
    t = f.read().split('\n')
    acc = 0
    inst = 0
    while True:
        if t[inst] == 0:
            break
        code, value = t[inst].split()
        value = int(value)
        t[inst] = 0
        inst += 1
        if code == 'jmp':
            inst += value - 1
        elif code == 'acc':
            acc += value
    print(acc)
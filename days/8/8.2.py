with open(r'days\8\input.txt', 'r') as f:
    t1 = f.read().split('\n')
    for i in range(len(t1)):
        t = t1.copy()
        code, value = t[i].split()
        if code == 'acc':
            continue
        if code == 'nop':
            t[i] = f'jmp {value}'
        elif code == 'jmp':
            t[i] = f'nop {value}' 
        acc = 0
        inst = 0
        while inst < len(t) - 1:
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
        else:
            break
    print(acc)
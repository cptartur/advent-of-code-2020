with open(r'days\6\input.txt', 'r') as f:
    t = f.read().split('\n\n')
    t = [len(set(i.replace('\n', ''))) for i in t]
    print(sum(t))
with open(r'days\5\input.txt', 'r') as f:
    t = f.read().split()
    ids = []
    for seat in t:
        ids.append(int(''.join(['1' if l in ['B', 'R'] else '0' for l in seat]), 2))
    x = sum(range(min(ids), max(ids) + 1)) - sum(ids)
    print(x)
        
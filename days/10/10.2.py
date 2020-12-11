import functools

@functools.lru_cache(None)
def find_permutation(t, start, end):
    if end - start <= 3:
        return 1
    total = 0
    for i, v in enumerate(t):
        if v - start <= 3:
            total += find_permutation(t[i + 1:], v, end)
    return total
    

with open(r'days\10\input.txt', 'r') as f:
    t = [int(i.strip()) for i in f]
    t = sorted(t)
    print(find_permutation(tuple(t), 0, t[-1] + 3))
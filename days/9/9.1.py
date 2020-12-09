def check_if_valid(t, index, rng):
    for i in range(index - rng, index):
        for j in range(i + 1, index):
            if t[i] + t[j] == t[index]:
                return True
    return False

with open(r'days\9\input.txt', 'r') as f:
    t = f.read().split()
    t = list(map(int, t))
    rng = 25
    for index, value in enumerate(t[rng:], rng):
        if not check_if_valid(t, index, rng):
            print(value)
            break

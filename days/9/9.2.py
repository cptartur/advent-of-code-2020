def check_if_valid(t, index, rng):
    for i in range(index - rng, index):
        for j in range(i + 1, index):
            if t[i] + t[j] == t[index]:
                return True
    return False

def find_range(t, value):
    for i in range(len(t)):
        s = set()
        sum_of_range = 0
        for j in range(i, len(t)):
            sum_of_range += t[j]
            s.add(t[j])
            if sum_of_range > value:
                break
            if sum_of_range == value:
                return (min(s), max(s))
    return (-1, -1)

with open(r'days\9\input.txt', 'r') as f:
    t = f.read().split()
    t = list(map(int, t))
    rng = 25
    for index, value in enumerate(t[rng:], rng):
        if not check_if_valid(t, index, rng):
            r = find_range(t, value)
            if r != (-1, -1):
                print(sum(r))
                break

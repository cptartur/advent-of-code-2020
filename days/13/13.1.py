def divisor(n, k):
    r = (n + k) % k
    return n if r == 0 else n + k - r

with open(r'days\13\input.txt', 'r') as f:
    start, line = f.read().split()
    start = int(start)
    t = [int(i) for i in line.split(',') if str.isdigit(i)]
    div_t = [(divisor(start, i), i) for i in t]
    x, y = min(div_t)
    print((x - start) * y)
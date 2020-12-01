with open('1.txt', 'r') as f:
    t = f.read().split()
    t = list(map(int, t))
    for i in range(len(t)):
        for j in range(1, len(t[i:])):
            if t[i] + t[j] == 2020:
                print(t[i] * t[j])
                break 
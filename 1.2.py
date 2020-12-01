with open('1.txt', 'r') as f:
    t = f.read().split()
    t = list(map(int, t))
    for i in range(len(t)):
        for j in range(len(t)):
            for k in range(len(t)):
                if t[i] + t[j] + t[k] == 2020:
                    print(t[i] * t[j] * t[k])
                    break
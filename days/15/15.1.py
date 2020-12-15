t = (2,15,0,9,1,20)
d = {v: [i, -1] for i, v in enumerate(t, start=1)}
last = t[-1]
for i in range(len(t) + 1, 2021):
    if (last in d and d[last][1] == -1) or last not in d:
        d[0][1], d[0][0] = d[0][0], i
        last = 0
    else:
        last = d[last][0] - d[last][1]
        if last not in d:
            d[last] = [-1, -1]
        d[last][1], d[last][0] = d[last][0], i
print(last)
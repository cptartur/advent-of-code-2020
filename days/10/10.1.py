with open(r'days\10\input.txt', 'r') as f:
    t = [int(i.strip()) for i in f]
    t = sorted(t)
    t = [v - t[i - 1] for i, v in enumerate(t)]   
    diff_1 = t.count(1) + 1
    diff_3 = t.count(3) + 1
    print(diff_1 * diff_3)
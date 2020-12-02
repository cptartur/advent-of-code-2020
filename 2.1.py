with open('2.txt', 'r') as f:
    t = [line.strip('\n') for line in f]
    valid_count = 0
    for s in t:
        s = s.split()
        min_occurences, max_occurences = map(int, s[0].split('-'))
        letter = s[1].strip(':')
        if min_occurences <= s[2].count(letter) <= max_occurences:
            valid_count += 1
    print(valid_count)

with open('2.txt', 'r') as f:
    t = [line.strip('\n') for line in f]
    valid_count = 0
    for s in t:
        s = s.split()
        first_pos, second_pos = map(int, s[0].split('-'))
        first_pos -= 1
        second_pos -= 1
        letter = s[1].strip(':')
        word = s[2]
        if any([word[first_pos] == letter, word[second_pos] == letter]) and not \
           all([word[first_pos] == letter, word[second_pos] == letter]):
            valid_count += 1
    print(valid_count)

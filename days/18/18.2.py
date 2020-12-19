class Order:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

    def __add__(self, other):
        return Order(self.value * other.value)

    def __radd__(self, other):
        return self.value + other

    def __mul__(self, other):
        return Order(self.value + other.value)


with open(r'days\18\input.txt', 'r') as f:
    t = f.read().split('\n')
    t = list(filter(None, t))
    total = 0
    for s in t:
        s = ''.join('*' if i == '+' else '+' if i == '*' else i for i in list(s))
        s = ''.join(f'Order({i})' if i.isdigit() else str(i) for i in list(s))
        total += eval(s)
        # print(eval(s))
    print(total)

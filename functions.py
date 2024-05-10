from collections import Counter


def multiply_diagonal(x):
    a = filter(lambda y: y != 0, [x[i][i] for i in range(min(len(x), len(x[0])))])
    q = 1
    for i in a:
        q *= i
    return q


def equal_multiset(x, y):
    return Counter(x) == Counter(y)


def max_before_zero(x):
    return x[max(filter(lambda y: x[y - 1] == 0, range(1, len(x))), key=lambda z: x[z])]



def convert_image(x, y):
    return [[sum([int(y[i] * a[i]) for i in range(3)]) for a in b] for b in x]


def run_length_encoding(x):
    if len(x) == 0:
        return [], []
    a, b = [x[0]], [1]
    for i in x[1:]:
        if i == a[-1]:
            b[-1] += 1
        else:
            a.append(i)
            b.append(1)
    return a, b


def pair_distance(x, y):
    ans = [[0] * len(y) for i in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            ans[i][j] = sum((a - b) ** 2 for a, b in zip(x[i], y[j])) ** 0.5
    return ans


from collections import Counter


def solution(A):
    d = {}
    count = 0
    for i in A:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    f = {}
    for k, v in d.items():
        if v > 1:
            f[k] = v
            count += 1

    if count < 2:
        if list(f.values()) < [4]:
            return -1

    x = list(f.keys())
    x.sort()
    if len(x) < 2:
        return 0
    a = x[-1]
    b = x[-2]

    if f[a] > 3:
        return 0
    else:
        return abs(a - b)

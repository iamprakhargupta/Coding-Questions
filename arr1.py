


def solution(A):
    counter = {}
    count = 0
    for i in A:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
    rect = {}
    for k, v in counter.items():
        if v > 1:
            rect[k] = v
            count += 1

    if count < 2:
        if list(rect.values()) < [4]:
            return -1

    x = list(rect.keys())
    x.sort()
    if len(x) < 2:
        return 0
    length = x[-1]
    breath = x[-2]

    if rect[length] > 3:
        return 0
    else:
        return abs(length - breath)

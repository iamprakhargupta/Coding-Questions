from typing import List


def min_cost_to_win(nums: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    d = {}
    flag = 0
    mini = len(nums)

    def mindiff(l):
        p = []
        for i in range(len(l) - 1):
            p.append(abs(l[i + 1] - l[i]))
        return min(p)

    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]].append(i)
        else:
            d[nums[i]] = [i]
    for k, v in d.items():
        if len(v) > 1:
            flag = 1
            x = mindiff(v)
            if x < mini:
                mini = x

    if flag == 1:

        return mini + 1
    else:
        return -1
l
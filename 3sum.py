def threeSum(nums):
    nums.sort()

    sol = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        else:
            l = i+1
            r = len(nums) - 1
            target = nums[i]
            while l < r:
                if nums[l] + nums[r] + target == 0:
                    sol.append([target, nums[l], nums[r]])
                    l = l + 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + target <= 0:
                    l = l + 1
                else:
                    r = r - 1

    return sol

print(threeSum([1,2,-2,-1]))
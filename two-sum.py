#  input  : nums = [2,7,11,15], target = 9
#  output : [0, 1]
#  nums[0] + nums[1] = 2 + 7 = 9

# 풀이 1.brute_force

def twoSum(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]


print(twoSum([2, 7, 11, 15], 18))

# 풀이 2.in 을 이용한 탐색


def twoSum2(nums, target):

    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return nums.index(n), nums[i + 1:].index(complement) + (i + 1)


print(twoSum([2, 7, 11, 15], 18))

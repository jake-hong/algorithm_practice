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


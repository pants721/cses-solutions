from typing import List
 
def increasing_array(nums: List[int]) -> int:
    sum = 0;
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            sum += nums[i] - nums[i + 1]
            nums[i + 1] = nums[i]
 
    return sum
 
_ = input()
nums = list(map(int, input().split()))
 
print(increasing_array(nums))

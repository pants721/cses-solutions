# # SUPER BAD TIME COMPLEXITY INITIAL SOLUTION
#
# n = int(input())
# nums = list(map(int, input().split()))
# # n = 8
# # nums = [-1, 3, -2, 5, 3, -5, 2, 2]
# # n = 2
# # nums = [-3, -2]
#
# ans = sum(nums)
#
# for i in range(len(nums)):
#     for rhs in range(i + 1, len(nums) + 1):
#         s = sum(nums[i:rhs])
#         # print(i, rhs, nums[i:rhs])
#         if s > ans:
#             ans = s
#
# print(ans)

n = int(input())
nums = list(map(int, input().split()))
# n = 2
# nums = [-3, -2]

max_ = nums[0]
curr_max = nums[0]

for i in range(1, n):
    curr_max = max(nums[i], curr_max + nums[i])
    max_ = max(max_, curr_max)

print(max_)

n, x = map(int, input().split())
nums = list(map(int, input().split()))

# m = {}
#
# for i in range(len(nums)):
#     if x - nums[i] in m:
#         pair = m[x - nums[i]]
#         assert pair is not None
#         print(pair + 1, i + 1)
#         exit()
#     m[nums[i]] = i
#
# print("IMPOSSIBLE")

srtd = sorted(nums)

lhs = 0
rhs = len(nums) - 1

while lhs < rhs:
    sum = srtd[lhs] + srtd[rhs]
    if sum == x:
        lhs_idx = nums.index(srtd[lhs])
        nums[lhs_idx] = -1
        rhs_idx = nums.index(srtd[rhs])
        print(lhs_idx + 1, rhs_idx + 1)
        exit()
    elif sum < x:
        lhs += 1
    else:
        rhs -= 1

print("IMPOSSIBLE")

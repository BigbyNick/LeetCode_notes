nums = [-2,1,-3,4,-1,2,1,-5,4]
mid_res = nums
max = -1000000
for index in range(len(nums)):
    if index == 0:
        mid_res[index] = nums[index]
    elif nums[index] >= mid_res[index-1] + nums[index]:
        mid_res[index] = nums[index]
    else:
        mid_res[index] = mid_res[index-1] + nums[index]
    if max < mid_res[index]:
        max = mid_res[index]

print(mid_res)
print(max)

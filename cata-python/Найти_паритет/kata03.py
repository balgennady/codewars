def find_outlier2(nums):

  base_parity = sum( x%2 for x in nums[:3] ) // 2
  
  for i in range(len(nums)):
    if nums[i] % 2 != base_parity:
      return nums[i]

l2 = [2, 4, 0, 100, 4, 11, 2602, 36]
find_outlier(l2)

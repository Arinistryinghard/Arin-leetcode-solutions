nums = [3,1,-2,-5,2,-4]
class Solution:
 def rearrangeArray(self, nums: list[int]) -> list[int]:
    n = len(nums)
    posi = 0
    neg = 0
    pos_arranged = []
    neg_arranged = []
    arranged = []
    for i in range(n):
        if nums[i] > 0:
            posi = nums[i]
            pos_arranged.append(posi)
        if nums[i] < 0:
            neg = nums[i]
            neg_arranged.append(neg)
    j = 0
    for i in range(0 ,len(pos_arranged)):
        arranged.append(pos_arranged[i])
        arranged.append(neg_arranged[j])
        j += 1
    
    return arranged

 def rearrangeArray2(self, nums: list[int]) -> list[int]:
    n = len(nums)
    result = [0] * n
    i = 0
    j = 1
    for k in range(n):
       if nums[k] > 0:
          result[i] = nums[k]
          i += 2
       else:
          result[j] = nums[k]
          j += 2
    
    return result   
         


sol = Solution()
ans = sol.rearrangeArray2(nums)
print(ans)
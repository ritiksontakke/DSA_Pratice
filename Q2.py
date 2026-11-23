nums = [3,4,5,6] 
target = 7
# Output: [0,1]

class Solution:

    def twoSum(self, nums:list[int],target:int):

        seen = {}

        for i,num in enumerate(nums):

            sum1 = target - num

            if sum1 in seen:
                return(seen[sum1],i)
            
            seen[num] = i

obj = Solution()
print(obj.twoSum(nums,target))

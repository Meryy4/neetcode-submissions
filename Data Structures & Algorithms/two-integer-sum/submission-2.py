class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        S=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i<j and nums[i]+nums[j]==target:
                    S=S+[i,j]
        return S
sol=Solution()
nums = [3,4,5,6]
target = 7
print(sol.twoSum(nums,target))
        
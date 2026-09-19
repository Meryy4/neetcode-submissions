class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min1=0
        max1=len(nums)-1
        if len(nums)==1:
            return 0 if nums[0]==target else -1
            
        while (min1<=max1):
            mid=(min1+max1)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                min1+=1
            else:
                max1-=1
        return -1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums)
        s=[]
        for i,char in enumerate(nums):
    
            min1 = i + 1
            max2 = len(nums) - 1
            while min1<max2 and min1!=max2:
                
                if nums[min1]+nums[max2]==-char :
                    k=sorted([nums[min1],nums[max2],char])
                    if   sorted([nums[min1],nums[max2],char]) in s : pass
                    else:
                         s.append(k)
                    min1=min1+1
                    max2=max2-1
                    if (nums[i] ==nums[i-1]) and (i>0):
                        break
                    if (max2< len(nums)-1 and  nums[max2] ==nums[max2+1]):
                        max2-=1
                    elif (min1< len(nums)-1 and  nums[min1] ==nums[min1-1]):
                        min1+=1
                
                    elif min1 >= max2:
                        break
                

                elif nums[min1]+nums[max2]>-char:
                    max2=max2-1
                    


                    
                else:
                    min1=min1+1
                
                
                
        return s



            
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        min=0
        max=len(numbers)-1
        while min<=max:

            if numbers[min]+numbers[max]==target:
                return list([min+1, max+1])
                break

            elif numbers[min]+numbers[max]>target:
                max=max-1
            else:
                min=min+1
            



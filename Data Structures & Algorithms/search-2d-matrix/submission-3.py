class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
        for i in range(len(matrix)):
            min1=0
            max1=len(matrix[0])-1
            while (min1<=max1):
                mid=(min1+max1)//2
                if matrix[i][mid]==target:
                    return True
                    break
                elif matrix[i][mid]<target:
                    min1+=1
                else:
                    max1-=1
        return False
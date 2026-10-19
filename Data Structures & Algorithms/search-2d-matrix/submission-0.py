class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten into a 1d array and then perform binary search on it
        flatArr = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                flatArr.append(matrix[i][j])
        
        print(flatArr)

        low = 0
        high = len(flatArr)-1

        while low <= high:
            mid = (high + low) // 2


            if flatArr[mid] == target:
                return True
            
            elif flatArr[mid] > target:
                high = mid-1
            
            else:
                low = mid+1
        
        return False

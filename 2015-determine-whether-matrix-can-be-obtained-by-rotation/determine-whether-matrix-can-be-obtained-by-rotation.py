class Solution:
    def findRotation(self, matrix: List[List[int]], target: List[List[int]]) -> bool:
        count,n=0,len(matrix)
        if matrix == target:
            return True
        while count<=4:
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            for i in range(n):
                matrix[i].reverse()
            
            if matrix==target and count<=n:
                return True
            count+=1
        else:
            return False
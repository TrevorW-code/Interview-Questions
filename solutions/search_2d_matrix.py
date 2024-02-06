class Solution:
 def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, (rows * cols) - 1

        while l <= r:
            print(f'looking for {target}')
            mid = (r + l) // 2

            mid_row = mid // cols
            mid_col = mid % cols
            matrix_mid = matrix[mid_row][mid_col]

            if target > matrix_mid:
                l = mid + 1
                print(f'{target} > {matrix_mid}')
                print(f'up next: {target}')

            elif target < matrix_mid:
                r = mid - 1
                print(f'{target} < {matrix_mid}')

            elif target == matrix_mid:
                return True

        return False
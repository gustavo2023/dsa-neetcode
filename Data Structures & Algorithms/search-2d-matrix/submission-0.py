class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1

        while low <= high:
            mid = (low + high) // 2
            curr_row = matrix[mid]

            if target >= curr_row[0] and target <= curr_row[-1]:
                l, r = 0, len(curr_row) - 1

                while l <= r:
                    m = (l + r) // 2

                    if curr_row[m] == target:
                        return True
                    elif curr_row[m] > target:
                        r = m - 1
                    else:
                        l = m + 1
                
                return False
            elif target < curr_row[0]:
                high = mid - 1
            else:
                low = mid + 1

        return False
            
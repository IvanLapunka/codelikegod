class Solution:
    found = False

    def searchMatrix(self, matrix, target):
        self.found = False
        if len(matrix) == 0:
            return False
        self.RecSearch(matrix, target, 0, 0, len(matrix) - 1, len(matrix[0]) - 1)
        return self.found

    def RecSearch(self, matrix, target, left_up_r, left_up_c, right_down_r, right_down_c):
        if left_up_r > right_down_r or left_up_c > right_down_c or self.found == True:
            return
        middle_r = (left_up_r + right_down_r) // 2
        middle_c = (left_up_c + right_down_c) // 2
        if matrix[middle_r][middle_c] == target:
            self.found = True
            return
        elif matrix[middle_r][middle_c] > target:
            self.RecSearch(matrix, target, left_up_r, left_up_c, middle_r - 1, middle_c - 1)
            self.RecSearch(matrix, target, middle_r, left_up_c, right_down_r, middle_c - 1)
            self.RecSearch(matrix, target, left_up_r, middle_c, middle_r - 1, right_down_c)
        else:
            self.RecSearch(matrix, target, middle_r + 1, middle_c + 1, right_down_r, right_down_c)
            self.RecSearch(matrix, target, middle_r + 1, left_up_c, right_down_r, middle_c)
            self.RecSearch(matrix, target, left_up_r, middle_c + 1, middle_r, right_down_c)

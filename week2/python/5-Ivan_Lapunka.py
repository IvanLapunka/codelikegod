class Solution:
    def setZeroes(self, matrix):
        '''
        :param matrix:
        :return:
        '''
        west, south, east, north = False, False, False, False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                north = True
                break
        for j in range(len(matrix[0])):
            if matrix[len(matrix) - 1][j] == 0:
                south = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                west = True
                break
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0]) - 1] == 0:
                east = True
                break

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for k in range(len(matrix[0])):
                    matrix[i][k] = 0

        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for k in range(len(matrix)):
                    matrix[k][j] = 0

        if south:
            for j in range(len(matrix[0])):
                matrix[len(matrix) - 1][j] = 0
        if north:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if west:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if east:
            for i in range(len(matrix)):
                matrix[i][len(matrix[0]) - 1] = 0

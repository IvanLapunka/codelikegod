class Solution:
    leng = 0
    pattern1 = [1, 0, -1, 0]
    pattern2 = [0, 1, 1, 0]

    def setLeng(self, matrix):
        self.leng = len(matrix[0]) - 1

    def rotate(self, matrix):
        self.setLeng(matrix)
        for i in range(len(matrix[0]) // 2):
            for j in range(i, len(matrix[0]) - i - 1):
                self.changeCell(matrix, i, j)

    def changeCell(self, matrix, i, j):
        tmp1 = matrix[self.genNextRow(0, i, j)][self.genNextCol(0, i, j)]
        for ind in range(0, 5):
            tmp2 = tmp1
            nInd = (ind + 1) % 4
            tmp1 = matrix[self.genNextRow(nInd, i, j)][self.genNextCol(nInd, i, j)]
            matrix[self.genNextRow(nInd, i, j)][self.genNextCol(nInd, i, j)] = tmp2

    def genNextRow(self, k, r, c):
        return r * self.pattern1[k] + c * self.pattern1[(k + 3) % 4] + self.leng * self.pattern2[(k + 3) % 4]

    def genNextCol(self, k, r, c):
        return r * self.pattern1[(k + 1) % 4] + c * self.pattern1[k] + self.leng * self.pattern2[k]
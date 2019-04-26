class Solution:
    def countBits(self, num):
        '''
        :param num: int value
        :return: List
        '''
        result = [0]
        powerTwo = 1
        for i in range(1, num + 1):
            if i == powerTwo:
                result.append(1)
                powerTwo *= 2
            else:
                result.append(1 + result[i - powerTwo])
        return result
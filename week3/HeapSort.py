class Solution:
    def __init__(self):
        self.mas = list()
        self.heapSize = 0

    def insert(self, value):
        self.heapSize += 1
        if len(self.mas) < self.heapSize:
            self.mas.append(value)
        else:
            self.mas[self.heapSize - 1] = value

        curr = self.heapSize - 1
        parent = (curr - 1) // 2

        while curr > 0 and self.mas[curr] > self.mas[parent]:
            self.mas[curr] , self.mas[parent] = self.mas[parent] , self.mas[curr]
            curr = parent
            parent = (curr - 1) // 2

    def delete(self):
        result = self.mas[0]
        self.mas[0] = self.mas[self.heapSize - 1]
        self.heapSize -= 1

        curr, left, right = 0,0,0
        while curr < self.heapSize:
            next = curr
            left, right = 2 * curr + 1, 2 * curr + 2
            if left < self.heapSize and right < self.heapSize:
                if self.mas[left] > self.mas[right]:
                    next = left
                else:
                    next = right
            elif left < self.heapSize:
                next = left

            if self.mas[curr] < self.mas[next]:
                self.mas[curr], self.mas[next] = self.mas[next], self.mas[curr]
                curr = next
            else:
                curr = self.heapSize

        return result

    def sortArray(self, nums):
        for i in range(len(nums)):
            self.insert(nums[i])
        for i in range(self.heapSize):
            tmp = self.delete()
            self.mas[self.heapSize] = tmp
        return self.mas

import random

class Solution:
    def sortArray(self, nums):
        n = 1000000
        testmas = []
        for i in range(n):
            testmas.append(int(random.randint(1, n)))
        # print(testmas)
        self.qSort(testmas, 0, len(testmas) - 1)
        print('done')

    def qSort(self, nums, left, right):
        if left >= right:
            return

        middle = left
        for i in range(left, right + 1):
            if nums[i] < nums[left]:
                middle += 1
                nums[middle], nums[i] = nums[i], nums[middle]

        nums[left], nums[middle] = nums[middle], nums[left]

        self.qSort(nums, left, middle - 1)
        self.qSort(nums, middle + 1, right)

    def qSort2(self, nums, left, right):
        if left >= right:
            return

        base = random.randint(left, right)
        nums[left], nums[base] = nums[base], nums[left]
        middle = left
        for i in range(left, right + 1):
            if nums[i] < nums[left]:
                middle += 1
                nums[middle], nums[i] = nums[i], nums[middle]

        nums[left], nums[middle] = nums[middle], nums[left]

        self.qSort(nums, left, middle - 1)
        self.qSort(nums, middle + 1, right)

s = Solution()
s.sortArray([])



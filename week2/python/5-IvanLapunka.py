class Solution:
    def search3(self, nums, target):
        found = False
        left, right = 0, len(nums) - 1
        while left <= right and not found:
            middle = (left + right) // 2
            if nums[middle] == target:
                found = True
            elif nums[middle] < target:
                if target > nums[right] >= nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target < nums[left] <= nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1

        if found:
            return middle
        return -1
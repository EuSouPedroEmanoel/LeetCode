class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer = 0

        for pointer in range(1, len(nums)):
            if nums[pointer] != nums[pointer -1]:
                writer += 1
                nums[writer] = nums[pointer]

        return writer + 1


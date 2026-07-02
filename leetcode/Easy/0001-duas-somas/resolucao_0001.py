class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size_of_nums = len(nums)
        solution_result: List[int] = []

        for i in range(size_of_nums):
            for j in range(size_of_nums):
                if j == i:
                    continue

                sum_result = nums[i] + nums[j]
                if sum_result == target:
                    solution_result = [i,j]
                    return solution_result

        return solution_result
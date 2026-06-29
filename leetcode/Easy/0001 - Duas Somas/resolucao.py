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


class Test:
    @staticmethod
    def test_TwoSum(
            numbers: List[int]=None, target=0,result: List[int]=None
    ):
        result_instance = Solution()

        test_result = result_instance.twoSum(numbers, target)

        try:
            assert test_result == result
            return True
        except:
            return False

if __debug__:
    mock = [
        {'numbers': [3,3], 'target': 6, 'result': [0,1]},
        {'numbers': [2,7,11,15], 'target': 9, 'result': [0,1]},
        {'numbers': [3,2,4], 'target': 6, 'result': [1,2]},
    ]


    for i in range(len(mock)):
        result = Test.test_TwoSum(**mock[i])
        status = 'PASS'
        if not result:
            status = 'NOT PASS'
        print(f'{mock[i]} - {status}')
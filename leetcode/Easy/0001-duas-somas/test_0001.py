import pytest
from typing import List
from resolucao_0001 import Solution

@pytest.mark.parametrize(
    "numbers, target, expected_result",
    [
        ([3, 3], 6, [0, 1]),
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([1, 2], 10, []),
    ]
)
def test_two_sum(numbers: List[int], target: int, expected_result: List[int]):
    solution_instance = Solution()

    actual_result = solution_instance.twoSum(numbers, target)
    assert actual_result == expected_result
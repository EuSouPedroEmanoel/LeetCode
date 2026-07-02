import pytest
from resolucao_0004 import Solution

@pytest.mark.parametrize(
    "array_1, array_2, expected_solution",
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
        ([2], [], 2.0),
    ]
)
def test_find_median_sorted_arrays(array_1: list[int], array_2: list[int], expected_solution: float):
    solution_instance = Solution()
    actual_result = solution_instance.findMedianSortedArrays(array_1, array_2)
    assert actual_result == expected_solution
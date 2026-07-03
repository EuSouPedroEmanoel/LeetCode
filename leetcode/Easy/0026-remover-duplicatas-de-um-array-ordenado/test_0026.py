import pytest
from resolucao_0026 import Solution


@pytest.mark.parametrize(
    "nums, expected_k, expected_nums",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ]
)
def test_removeDuplicates(nums: list[int], expected_k: int, expected_nums: list[int]):
    sl = Solution()

    actual_k = sl.removeDuplicates(nums)

    assert actual_k == expected_k

    assert nums[:actual_k] == expected_nums
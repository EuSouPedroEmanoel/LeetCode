import pytest
from resolucao_0009 import Solution

@pytest.mark.parametrize(
    "x, expected_output",
    [
        (121, True),
        (-121, False),
        (10, False),
    ]
)
def test_is_palindrome(x: int, expected_output: bool):
    solution_instance = Solution()
    actual_result = solution_instance.isPalindrome(x)

    assert actual_result == expected_output
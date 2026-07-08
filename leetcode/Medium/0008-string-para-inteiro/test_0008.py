import pytest
from resolucao_0008 import Solution


@pytest.mark.parametrize(
    "s, expected_result",
    [
        ("42", 42),
        (" -042", -42),
        ("1337c0d3", 1337),
        ("0-1", 0),
        ("4193 with words",4193),
        ("-91283472332", -2147483648),
        ("+1", 1)
    ]
)
def test_length_of_longest_substring(s: str, expected_result: int):
    solution_instance = Solution()

    actual_result = solution_instance.myAtoi(s)

    assert actual_result == expected_result
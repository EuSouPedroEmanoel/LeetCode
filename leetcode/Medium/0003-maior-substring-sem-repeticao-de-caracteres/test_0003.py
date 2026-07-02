import pytest
from resolucao_0003 import Solution


@pytest.mark.parametrize(
    "s, expected_result",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
    ]
)
def test_length_of_longest_substring(s: str, expected_result: int):
    solution_instance = Solution()

    actual_result = solution_instance.lengthOfLongestSubstring(s)

    assert actual_result == expected_result
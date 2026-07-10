import pytest
from resolucao_0006 import Solution


@pytest.mark.parametrize(
    "s, numRows, expected_result",
    [
        ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
        ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
        ("A", 1, "A"),
        ("BAB", 1, "BAB"),
    ]
)
def test_length_of_longest_substring(s: str, numRows,expected_result: int):
    solution_instance = Solution()

    actual_result = solution_instance.convert(s, numRows)

    assert actual_result == expected_result
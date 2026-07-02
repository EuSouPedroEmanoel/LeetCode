import pytest

from resolucao_0013 import Solution


@pytest.mark.parametrize(
    "s, expected_result",
    [
        ("III", (3)),
        ("LVIII", (58)),
        ("MCMXCIV", (1994)),
    ]
)
def test_romanToInt(s: str, expected_result: int):
    solution_instance = Solution()

    actual_result = solution_instance.romanToInt(s)

    assert actual_result == expected_result
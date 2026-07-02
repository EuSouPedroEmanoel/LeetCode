import pytest

from resolucao_0020 import Solution

@pytest.mark.parametrize(
    's, expected_result',
    [
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
    ]
)
def test_isValid(s: str, expected_result: bool):
    sl = Solution()

    actual_result = sl.isValid(s)

    assert actual_result == expected_result
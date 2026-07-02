import pytest

from resolucao_0014 import Solution


@pytest.mark.parametrize(
    'strs, expected_result',
    [
        (["flower","flow","flight"], "fl"),
        (["dog","racecar","car"], ""),
    ]
)
def test_longestCommo(strs: list[str], expected_result: str):
    sl = Solution()

    actual_reasult = sl.longestCommonPrefix(strs)

    assert actual_reasult == expected_result
import pytest
from resolucao_0002 import Solution, ListNode

@pytest.mark.parametrize(
    "l1, l2, expected_solution",
    [
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ]
)
def test_add_two_numbers(l1: list[int], l2: list[int], expected_solution: list[int]):
    l1_linked = Solution.from_list(l1)
    l2_linked = Solution.from_list(l2)

    solution_instance = Solution()

    result_linked = solution_instance.addTwoNumbers(l1_linked, l2_linked)

    actual_result = Solution.to_list(result_linked)

    assert actual_result == expected_solution

@pytest.mark.parametrize(
    "input_list",
    [
        ([1, 2, 3]),
    ]
)
def test_list_node_from_list(input_list: list[int]):
    result = Solution.to_list(Solution.from_list(input_list))

    assert result == input_list


def test_from_list_empty():
    assert Solution.from_list([]) is None
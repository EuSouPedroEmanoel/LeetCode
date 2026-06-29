from resolucao import Solution, ListNode

class Test:
    @staticmethod
    def test_addTwoNumbers():
        def test(
            l1: list[int],
            l2: list[int],
            solution_list: list[int]
        ):
            l1_linked = Solution.from_list(l1)
            l2_linked = Solution.from_list(l2)

            solution_instance = Solution()

            result_linked = solution_instance.addTwoNumbers(l1_linked, l2_linked)

            result = Solution.to_list(result_linked)

            try:
                assert result == solution_list
                return {'status': 'PASS', 'result': result}
            except AssertionError as e:
                return {'status': 'NOT PASS', 'result': result}

        mock = [
             {'l1': [2, 4, 3], 'l2': [5, 6, 4], 'solution_list': [7, 0, 8], },
             {'l1': [0], 'l2': [0], 'solution_list': [0], },
            {
                'l1': [9, 9, 9, 9, 9, 9, 9],
                'l2': [9, 9, 9, 9],
                'solution_list': [8, 9, 9, 9, 0, 0, 0, 1],
            },
        ]

        print('\nADD TWO NUMBERS\n')

        for i in range(len(mock)):
            result = test(**mock[i])

            print(f'{mock[i]}\n{result['result']}\n{result['status']}')

    @staticmethod
    def test_listNode_from_List(solution_instance: Solution):
        def test(list: List[int]):
            result = solution_instance.to_list(solution_instance.from_list(list))
            return result == list

        print('\nLIST NODE FROM LIST\n')

        mock = [
            {'list': [1, 2, 3]}
        ]

        for i in mock:
            status = 'PASS'
            result = test(i['list'])

            if not result:
                status = 'NOT PASS'

            print(f'{i['list']}\n{status}')




if __name__ == '__main__':
    solution_instance = Solution
    Test.test_listNode_from_List(solution_instance)
    Test.test_addTwoNumbers()
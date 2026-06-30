from resolucao import Solution


def test_solution():
    def test(x, output):
        result = solution_instance.isPalindrome(x)

        if result == output:
            return {'status': 'PASS', 'output': result}
        return {'status': 'NOT PASS', 'output': result}


    mock = [
        {'x': 121, 'output': True},
        {'x': -121, 'output': False},
        {'x': 10, 'output': False},
    ]

    solution_instance = Solution()

    for i in mock:
        result = test(**i)
        print(result)


if __name__ == '__main__':
    test_solution()
from resolucao import Solution

def test_solution():
    def test(array_1: list[int], array_2: list[int], solution: float):
        sttm = sulution_instance.findMedianSortedArrays(array_1, array_2)

        if sttm == solution:
            return {'status': 'PASS', 'media': sttm}
        return {'status': 'NOT PASS', 'media': sttm}


    mock = [
        {'array_1': [1,3], 'array_2': [2], 'solution': 2},
        {'array_1': [1,2], 'array_2': [3,4], 'solution': 2.5},
        {'array_1': [2], 'array_2': [], 'solution': 2},

    ]
    sulution_instance = Solution()

    for i in mock:
        result = test(**i)
        print(f'{result['status']} - Média: {result['media']}')

if __name__ == '__main__':
    test_solution()

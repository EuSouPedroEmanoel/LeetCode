from resolucao import Solution

def test_solution():
    def test(s: str, result_dict: int) -> dict:
        result = solution_instance.lengthOfLongestSubstring(s)
        if result == result_dict:
            return {'status': 'PASS', 'max_substring': result}
        else:
            return {'status': 'NOT PASS', 'max_substring': result}


    solution_instance = Solution()

    mock = [
        #{'s': 'abcabcbb', 'result_dict': 3},
        #{'s': 'bbbbb', 'result_dict': 1},
        {'s': 'pwwkew', 'result_dict': 3},
    ]

    for i in mock:
        result = test(**i)
        print(f"{i['s']} - {result['status']} - {result['max_substring']}")



if __name__ == '__main__':
    test_solution()
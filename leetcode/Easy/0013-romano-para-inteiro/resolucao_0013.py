dict_roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

def roman_char_to_int(c: str) -> int:
    return  dict_roman[c]

class Solution:
    def romanToInt(self, s: str) -> int:

        int_result = 0
        size = len(s)
        i = 0

        while i < size:
            pointer = roman_char_to_int(s[i])

            if i + 1 < size and pointer < roman_char_to_int(s[i+1]):
                next_pointer = roman_char_to_int(s[i+1])
                int_result += next_pointer - pointer
                i += 2
            else:
                int_result += pointer
                i += 1

        return int_result


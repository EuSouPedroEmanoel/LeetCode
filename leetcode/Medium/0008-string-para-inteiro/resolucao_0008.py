class Solution:
    def myAtoi(self, s: str) -> int:
        is_negative = False
        taut_i_taw_a_puddy_tat = False
        result = 0

        for i, ch in enumerate(s):

            match ch:
                case _ if '9' >= ch >= '0':
                    if result:
                        result *= 10
                    result += int(ch)
                    taut_i_taw_a_puddy_tat = True
                case ' ' if not taut_i_taw_a_puddy_tat:
                    continue
                case '-' if not taut_i_taw_a_puddy_tat:
                    if result or is_negative:
                        break
                    taut_i_taw_a_puddy_tat = True
                    is_negative = True
                case '+' if not taut_i_taw_a_puddy_tat:
                    taut_i_taw_a_puddy_tat = True
                case _:
                    break

        if is_negative:
            result = -result

        INT_MIN = -2 ** 31  # -2147483648
        INT_MAX = 2 ** 31 - 1  # 2147483647

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result
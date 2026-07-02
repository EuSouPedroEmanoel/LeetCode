import math


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x == 0: return True

        div = 10 ** math.floor(math.log10(x))

        while x > 0:
            digito_esquerda = x // div
            digito_direita = x % 10

            if digito_esquerda != digito_direita:
                return False

            x = (x % div) // 10
            div = div // 100

        return True
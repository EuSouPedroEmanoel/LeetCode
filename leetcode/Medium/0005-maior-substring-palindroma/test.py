import ctypes
import os


def inicializar_biblioteca():
    caminho_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_so = os.path.join(caminho_atual, "resolucao.so")

    lib = ctypes.CDLL(caminho_so)

    lib.longestPalindrome.argtypes = [ctypes.c_char_p]
    lib.longestPalindrome.restype = ctypes.c_char_p

    return lib


_lib_c = inicializar_biblioteca()


def test_longestPalindrome() -> str:
    def test(s: str, output: str):
        texto_bytes = s.encode('utf-8')
        resultado_bytes = _lib_c.longestPalindrome(texto_bytes)
        result = resultado_bytes.decode('utf-8')

        if result == output:
            return 'PASS', result
        return 'NOT PASS', result


    mock = [
        {'s': 'babad', 'output': 'bab'},
        {'s': 'cbbd', 'output': 'bb'},
    ]

    for i in mock:
        result = test(**i)
        print(result)


if __name__ == "__main__":
   test_longestPalindrome()
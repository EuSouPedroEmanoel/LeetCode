import ctypes
import os
import pytest


def inicializar_biblioteca():
    caminho_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_so = os.path.join(caminho_atual, "resolucao_0005.so")

    lib = ctypes.CDLL(caminho_so)
    lib.longestPalindrome.argtypes = [ctypes.c_char_p]
    lib.longestPalindrome.restype = ctypes.c_char_p

    return lib

_lib_c = inicializar_biblioteca()


@pytest.mark.parametrize(
    "s, expected_output",
    [
        ("babad", "bab"),
        ("cbbd", "bb"),
        ("a", "a"),
        ("ac", "a"),
    ]
)
def test_longest_palindrome(s: str, expected_output: str):
    texto_bytes = s.encode('utf-8')

    resultado_bytes = _lib_c.longestPalindrome(texto_bytes)

    actual_result = resultado_bytes.decode('utf-8')

    assert actual_result == expected_output
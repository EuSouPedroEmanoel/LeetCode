import ctypes
import os
import pytest


# ==============================================================================
# 1. FUNÇÕES DE EMBRULHO (WRAPPERS)
# ==============================================================================

def rodar_python(s: str) -> bool:
    from resolucao_0020 import Solution
    sl = Solution()
    return sl.isValid(s)


def rodar_c(s: str) -> bool:
    caminho_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_so = os.path.join(caminho_atual, "c_node", "resolucao_0020_c.so")

    try:
        lib = ctypes.CDLL(caminho_so)
    except OSError as e:
        pytest.fail(f"Não foi possível carregar a biblioteca em C. Erro: {e}")

    lib.isValid.argtypes = [ctypes.c_char_p]
    lib.isValid.restype = ctypes.c_bool

    return lib.isValid(s.encode('utf-8'))


# ==============================================================================
# 2. CENÁRIOS DE TESTE PARAMETRIZADOS
# ==============================================================================

@pytest.mark.parametrize(
    "s, expected",
    [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([])", True),
        ("(", False),
        ("]", False),
    ]
)
# Removido o rodar_go daqui
@pytest.mark.parametrize("executar_algoritmo", [rodar_python, rodar_c])
def test_valid_parentheses_multi_lang(executar_algoritmo, s: str, expected: bool):
    assert executar_algoritmo(s) == expected
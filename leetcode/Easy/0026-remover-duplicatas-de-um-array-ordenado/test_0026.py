import ctypes
import os
import pytest


# ==============================================================================
# 1. FUNÇÕES DE EMBRULHO (WRAPPERS)
# ==============================================================================

def rodar_python(nums: list[int]):
    from resolucao_0026 import Solution

    sl = Solution()
    nums_copia = nums.copy()
    actual_k = sl.removeDuplicates(nums_copia)

    return actual_k, nums_copia[:actual_k]


def rodar_c(nums: list[int]):
    caminho_atual = os.path.abspath(os.path.dirname(__file__))
    caminho_so = os.path.join(caminho_atual, "resolucao_0026_c.so")

    try:
        lib = ctypes.CDLL(caminho_so)
    except OSError as e:
        pytest.fail(f"Não foi possível carregar a biblioteca em C. Você compilou o .so? Erro: {e}")

    lib.removeDuplicates.argtypes = [ctypes.POINTER(ctypes.c_int), ctypes.c_int]
    lib.removeDuplicates.restype = ctypes.c_int

    tamanho = len(nums)
    arr_c = (ctypes.c_int * tamanho)(*nums)

    actual_k = lib.removeDuplicates(arr_c, tamanho)

    return actual_k, list(arr_c)[:actual_k]


# ==============================================================================
# 2. CENÁRIOS DE TESTE PARAMETRIZADOS
# ==============================================================================

@pytest.mark.parametrize(
    "nums, expected_k, expected_nums",
    [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ]
)
@pytest.mark.parametrize("executar_algoritmo", [rodar_python, rodar_c])
def test_remove_duplicates_multi_lang(
        executar_algoritmo,
        nums: list[int],
        expected_k: int,
        expected_nums: list[int]
):
    actual_k, actual_nums = executar_algoritmo(nums)

    assert actual_k == expected_k
    assert actual_nums == expected_nums
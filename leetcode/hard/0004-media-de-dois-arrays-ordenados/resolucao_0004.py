from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_size = m + n

        if total_size % 2 == 0:
            alvos = [(total_size // 2) - 1, total_size // 2]
        else:
            alvos = [total_size // 2]

        valores_alvo = []
        p1, p2 = 0, 0

        for i in range(max(alvos) + 1):
            if p1 < m and p2 < n:
                if nums1[p1] <= nums2[p2]:
                    val_atual = nums1[p1]
                    p1 += 1
                else:
                    val_atual = nums2[p2]
                    p2 += 1
            elif p1 < m:
                val_atual = nums1[p1]
                p1 += 1
            else:
                val_atual = nums2[p2]
                p2 += 1

            if i in alvos:
                valores_alvo.append(val_atual)

        return sum(valores_alvo) / len(valores_alvo)
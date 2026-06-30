import bisect
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            size = len(nums2)
            return nums2[size // 2] if size % 2 != 0 else (nums2[(size - 1) // 2] + nums2[size // 2]) / 2.0
        if not nums2:
            size = len(nums1)
            return nums1[size // 2] if size % 2 != 0 else (nums1[(size - 1) // 2] + nums1[size // 2]) / 2.0

        def sort_arrays(array_1, array_2):
            target = array_2[0]
            pos = bisect.bisect_right(array_1, target)
            size_of_virtual_array = len(array_1) + len(array_2)
            return pos, size_of_virtual_array

        def find_half_position_not_even(size):
            return [size // 2]

        def find_half_position_even(size):
            esquerda = (size // 2) - 1
            direita = size // 2
            return [esquerda, direita]

        def media_num_in_virtual_pos(nums_1, nums_2, pos, targets):
            result = 0
            for target in targets:
                if pos <= target < (pos + len(nums_2)):
                    result_pos = target - pos
                    result += nums_2[result_pos]
                elif target < pos:
                    result += nums_1[target]
                else:
                    result += nums_1[target - len(nums_2)]

            if len(targets) > 1:
                return result / 2.0
            return float(result)

        # Execução principal
        pos, size_of_virtual_array = sort_arrays(nums1, nums2)

        if size_of_virtual_array % 2 == 0:
            half_position = find_half_position_even(size_of_virtual_array)
            result = media_num_in_virtual_pos(nums1, nums2, pos, half_position)
        else:
            half_position = find_half_position_not_even(size_of_virtual_array)
            result = media_num_in_virtual_pos(nums1, nums2, pos, half_position)

        return result
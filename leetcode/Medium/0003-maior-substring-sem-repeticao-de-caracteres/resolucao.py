class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_letters = set()
        left = 0
        biggest_string_size = 0

        for right in range(len(s)):
            while s[right] in set_letters:
                set_letters.remove(s[left])
                left += 1

            set_letters.add(s[right])

            current_window_size = right - left + 1
            if current_window_size > biggest_string_size:
                biggest_string_size = current_window_size

        return biggest_string_size
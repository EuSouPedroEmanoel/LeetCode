class Solution:
    def convert(self, s: str, numRows: int) -> str:

        char_matrix = [[] for _ in range(numRows)]

        brinup = False
        index_row_writer = 0


        for i in range(len(s)):
            if brinup and index_row_writer == 0:
                brinup = False
            elif not brinup and index_row_writer == numRows -1:
                brinup = True

            char_matrix[index_row_writer].append(i)
            if not brinup and numRows > 1:
                index_row_writer += 1
            elif brinup and numRows > 1:
                index_row_writer -= 1

        result = "".join(s[ch] for line in char_matrix for ch in line)
        return result

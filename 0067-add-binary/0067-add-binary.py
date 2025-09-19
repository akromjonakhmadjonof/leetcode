class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += (ord(a[i]) - ord('0'))
                i -= 1
            if j >= 0:
                total += (ord(b[j]) - ord('0'))
                j -= 1

            bit = total % 2
            carry = total // 2
            res.append(str(bit))

        return ''.join(reversed(res))

        
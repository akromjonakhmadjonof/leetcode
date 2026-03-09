class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        prev = 0
        while prev < len(chars):
            curr = prev + 1
            count = 1
            while curr < len(chars) and chars[prev] == chars[curr]:
                count += 1
                curr += 1
            chars[write] = chars[prev]
            write += 1
            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1
            prev = curr
        return write
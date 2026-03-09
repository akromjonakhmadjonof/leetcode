class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        prev = 0

        while prev < len(chars):
            curr = prev +  1
            if curr < len(chars) and chars[prev] == chars[curr]:
                i = 1
                while curr < len(chars) and chars[prev] == chars[curr]:
                    i += 1
                    curr += 1
                s.extend(list(f"{chars[prev]}{i}"))
                prev = curr
            else:
                s.append(chars[prev])
                prev += 1
        chars[:] = s
        return len(chars)
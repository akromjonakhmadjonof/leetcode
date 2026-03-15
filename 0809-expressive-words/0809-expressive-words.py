class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def get_groups(s):
            groups = []
            i = 0
            while i < len(s):
                ch = s[i]
                count = 1
                while i + 1 < len(s) and s[i + 1] == ch:
                    count += 1
                    i += 1
                groups.append((ch, count))
                i += 1
            return groups

        def is_stretchy(s_groups, w_groups):
            if len(s_groups) != len(w_groups):
                return False
            for (sc, sn), (wc, wn) in zip(s_groups, w_groups):
                if sc != wc:
                    return False
                if sn < wn:
                    return False
                if sn != wn and sn < 3:
                    return False
            return True

        s_groups = get_groups(s)
        count = 0
        for word in words:
            if is_stretchy(s_groups, get_groups(word)):
                count += 1
        return count
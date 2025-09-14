from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set('aeiou')

        def devowel(s: str) -> str:
            s = s.lower()
            return ''.join('*' if c in vowels else c for c in s)

        # Exact words for O(1) exact-match checks
        exact = set(wordlist)

        # First occurrence for case-insensitive matches
        lower_map = {}
        # First occurrence for devoweled matches
        devowel_map = {}

        for w in wordlist:
            lw = w.lower()
            lower_map.setdefault(lw, w)          # keep first
            devowel_map.setdefault(devowel(lw), w)

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
                continue

            lq = q.lower()
            if lq in lower_map:
                ans.append(lower_map[lq])
                continue

            dq = devowel(lq)
            ans.append(devowel_map.get(dq, ""))
        return ans

from collections import Counter
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        # Lengths must match
        if len(s) != len(goal):
            return False

        # If strings are already equal:
        # valid only if there is a duplicate character (so we can swap duplicates and still keep the string the same)
        if s == goal:
            return any(count > 1 for count in Counter(s).values())

        # Otherwise, collect mismatched positions
        diffs = [(a, b) for a, b in zip(s, goal) if a != b]

        # Must be exactly 2 mismatches, and they must "cross-match" to be swappable
        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]
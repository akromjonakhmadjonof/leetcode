class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            ln, dn = email.split("@")
            index = ln.find("+")
            cleared = ln[:index] if index > -1 else ln
            cleared = cleared.replace(".", "")
            seen.add(f"{cleared}@{dn}")
        return len(seen)
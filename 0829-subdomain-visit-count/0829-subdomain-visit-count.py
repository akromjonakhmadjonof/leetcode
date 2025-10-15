class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        freq = {}

        for cpdomain in cpdomains:
            count, link = cpdomain.split(" ")
            parts = link.split(".")
            n = len(parts)
            for i in range(len(parts) - 1, -1, -1):
                part = ".".join(parts[i:n] if i!=n else parts[i])
                if part not in freq:
                    freq[part] = int(count)
                else:
                    freq[part] += int(count)
        results = []
        for domain, count in freq.items():
            results.append(f"{count} {domain}")
        return results     

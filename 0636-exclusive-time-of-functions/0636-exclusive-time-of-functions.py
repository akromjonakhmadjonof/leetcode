class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []

        prev_time = 0

        for log in logs:
            fid, typ, t = log.split(":")
            fid = int(fid)
            t = int(t)

            if typ == "start":
                if stack:
                    result[stack[-1]] += t - prev_time
                stack.append(fid)
                prev_time = t

            else:
                result[stack.pop()] += t - prev_time + 1
                prev_time = t + 1 

        return result
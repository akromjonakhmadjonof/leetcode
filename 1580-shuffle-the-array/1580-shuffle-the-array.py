class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x,y = 0, n
        answer = []
        while x < n and y < 2 * n:
            answer.append(nums[x])
            answer.append(nums[y])
            x += 1
            y += 1
        return answer
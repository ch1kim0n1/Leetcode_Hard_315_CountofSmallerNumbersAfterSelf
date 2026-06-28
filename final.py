class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ranks = {v: i + 1 for i, v in enumerate(sorted(set(nums)))}
        bit = [0] * (len(ranks) + 1)
        ans = [0] * len(nums)
        size = len(bit)

        for idx in range(len(nums) - 1, -1, -1):
            rank = ranks[nums[idx]]

            total = 0
            i = rank - 1
            while i:
                total += bit[i]
                i -= i & -i

            ans[idx] = total

            i = rank
            while i < size:
                bit[i] += 1
                i += i & -i

        return ans

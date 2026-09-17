class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float("inf")] * n

        left = 0
        curr_sum = 0
        ans = float("inf")
        curr_best = float("inf")

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target and left <= right:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                curr_len = right - left + 1

                # Check if there is a valid non-overlapping subarray before 'left'
                if left > 0 and min_len[left - 1] != float("inf"):
                    ans = min(ans, curr_len + min_len[left - 1])

                curr_best = min(curr_best, curr_len)

            min_len[right] = curr_best

        return ans if ans != float("inf") else -1
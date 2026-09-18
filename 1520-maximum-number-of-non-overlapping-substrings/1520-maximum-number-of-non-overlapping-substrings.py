class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        # Step 1: Find first and last occurrences of each character
        first = {}
        last = {}
        for idx, ch in enumerate(s):
            if ch not in first:
                first[ch] = idx
            last[ch] = idx

        # Step 2: Find all valid minimal intervals
        intervals = []
        for ch in first:
            i = first[ch]
            j = last[ch]
            valid = True

            k = i
            while k <= j:
                curr_ch = s[k]
                if first[curr_ch] < i:
                    valid = False
                    break
                j = max(j, last[curr_ch])
                k += 1

            if valid:
                intervals.append((i, j))

        # Step 3: Sort by end index and select greedily
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1
        for start, end in intervals:
            if start > prev_end:
                ans.append(s[start : end + 1])
                prev_end = end

        return ans
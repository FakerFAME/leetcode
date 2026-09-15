from collections import deque

class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        
        # 1. Manacher's algorithm for odd-length palindromes
        # rad[i] represents the radius around s[i], such that s[i-rad[i] : i+rad[i]+1] is a palindrome.
        rad = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(rad[l + r - i], r - i + 1)
            while 0 <= i - k and i + k < n and s[i - k] == s[i + k]:
                k += 1
            rad[i] = k - 1
            if i + rad[i] > r:
                l = i - rad[i]
                r = i + rad[i]
                
        # 2. left[i]: max odd palindrome length ending at or before i
        left = [1] * n
        q = deque()  # stores (center, right_boundary)
        for i in range(n):
            while q and q[0][1] < i:
                q.popleft()
            q.append((i, i + rad[i]))
            
            # The earliest center whose palindrome reaches at least index i
            center = q[0][0]
            curr_len = 2 * (i - center) + 1
            left[i] = max(left[i - 1] if i > 0 else 1, curr_len)
            
        # 3. right[i]: max odd palindrome length starting at or after i
        right = [1] * n
        q = deque()  # stores (center, left_boundary)
        for i in range(n - 1, -1, -1):
            while q and q[0][1] > i:
                q.popleft()
            q.append((i, i - rad[i]))
            
            # The latest center whose palindrome reaches at least index i
            center = q[0][0]
            curr_len = 2 * (center - i) + 1
            right[i] = max(right[i + 1] if i + 1 < n else 1, curr_len)
            
        # 4. Find max left[i] * right[i + 1]
        ans = 1
        for i in range(n - 1):
            prod = left[i] * right[i + 1]
            if prod > ans:
                ans = prod
                
        return ans
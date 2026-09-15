class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        last_end = -1  # End index of the last chosen palindrome
        
        # Check all possible centers: 2 * n - 1 centers
        # center // 2 is left, (center + 1) // 2 is right
        for center in range(2 * n - 1):
            l = center // 2
            r = (center + 1) // 2
            
            while l >= 0 and r < n and s[l] == s[r]:
                # If this palindrome starts after the last chosen one
                if l > last_end:
                    length = r - l + 1
                    if length >= k:
                        ans += 1
                        last_end = r
                        break  # Greedily pick the shortest/earliest-ending palindrome from this center
                else:
                    # Overlaps with the previous picked palindrome, cannot pick earlier start
                    break
                l -= 1
                r += 1
                
        return ans
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        # Combine s, a separator, and reversed s
        rev_s = s[::-1]
        combo = s + "#" + rev_s
        
        # Build KMP LPS (Longest Prefix Suffix) array
        n = len(combo)
        lps = [0] * n
        length = 0
        i = 1
        
        while i < n:
            if combo[i] == combo[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
                    
        # lps[-1] gives the length of the longest palindromic prefix of s
        longest_palindromic_prefix_len = lps[-1]
        
        # Remaining suffix must be reversed and prepended
        suffix_to_add = rev_s[:len(s) - longest_palindromic_prefix_len]
        
        return suffix_to_add + s
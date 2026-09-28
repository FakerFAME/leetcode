class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Vertical scanning
        for i in range(len(strs[0])):
            char = strs[0][i]
            # Check this character against all other strings
            for j in range(1, len(strs)):
                # If we exceed the length of another string or find a mismatch
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
                    
        return strs[0]
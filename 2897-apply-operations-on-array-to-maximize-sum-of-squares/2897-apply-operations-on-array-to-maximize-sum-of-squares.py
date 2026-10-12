class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        bit_counts = [0] * 32
        
        # Count the occurrences of each bit across all numbers
        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bit_counts[i] += 1
                    
        total_sum = 0
        
        # Greedily construct the k largest numbers
        for _ in range(k):
            current_num = 0
            for i in range(32):
                if bit_counts[i] > 0:
                    current_num |= (1 << i)
                    bit_counts[i] -= 1
            
            # Add the square of the constructed number modulo 10^9 + 7
            total_sum = (total_sum + current_num * current_num) % MOD
            
        return total_sum
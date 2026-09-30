#include <limits.h>

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    // Ensure nums1 is the smaller array to minimize the binary search range
    if (nums1Size > nums2Size) {
        return findMedianSortedArrays(nums2, nums2Size, nums1, nums1Size);
    }
    
    int m = nums1Size;
    int n = nums2Size;
    int low = 0, high = m;
    int half_len = (m + n + 1) / 2;
    
    while (low <= high) {
        int i = (low + high) / 2;
        int j = half_len - i;
        
        int max_left1 = (i == 0) ? INT_MIN : nums1[i - 1];
        int min_right1 = (i == m) ? INT_MAX : nums1[i];
        
        int max_left2 = (j == 0) ? INT_MIN : nums2[j - 1];
        int min_right2 = (j == n) ? INT_MAX : nums2[j];
        
        if (max_left1 <= min_right2 && max_left2 <= min_right1) {
            // If total length is odd
            if ((m + n) % 2 == 1) {
                return (double)(max_left1 > max_left2 ? max_left1 : max_left2);
            }
            // If total length is even
            int max_of_left = max_left1 > max_left2 ? max_left1 : max_left2;
            int min_of_right = min_right1 < min_right2 ? min_right1 : min_right2;
            return (double)(max_of_left + min_of_right) / 2.0;
        } 
        else if (max_left1 > min_right2) {
            high = i - 1; // Move left in nums1
        } 
        else {
            low = i + 1; // Move right in nums1
        }
    }
    
    return 0.0;
}
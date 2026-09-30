/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Create a dummy node to handle edge cases easily (like removing the head itself)
    struct ListNode* dummy = malloc(sizeof(struct ListNode));
    dummy->val = 0;
    dummy->next = head;
    
    struct ListNode* fast = dummy;
    struct ListNode* slow = dummy;
    
    // Move the fast pointer n + 1 steps ahead so the gap between fast and slow is n nodes
    for (int i = 0; i <= n; i++) {
        fast = fast->next;
    }
    
    // Move both pointers at the same speed until fast reaches the end of the list
    while (fast != NULL) {
        fast = fast->next;
        slow = slow->next;
    }
    
    // slow is now just before the node we want to remove
    struct ListNode* nodeToRemove = slow->next;
    slow->next = slow->next->next;
    
    // Free the removed node to prevent memory leaks
    free(nodeToRemove);
    
    // Keep a reference to the actual head before freeing the dummy
    struct ListNode* newHead = dummy->next;
    free(dummy);
    
    return newHead;
}
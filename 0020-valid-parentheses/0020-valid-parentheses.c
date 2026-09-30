#include <stdbool.h>
#include <string.h>

bool isValid(char* s) {
    int len = strlen(s);
    
    // An odd-length string can never have perfectly matched pairs
    if (len % 2 != 0) {
        return false;
    }
    
    // Use an array to simulate a stack
    char stack[len];
    int top = -1;
    
    for (int i = 0; i < len; i++) {
        char c = s[i];
        
        // Push opening brackets onto the stack
        if (c == '(' || c == '{' || c == '[') {
            stack[++top] = c;
        } 
        // Handle closing brackets
        else {
            // If the stack is empty but we have a closing bracket, it's invalid
            if (top == -1) {
                return false;
            }
            
            // Pop the top character and check for a mismatch
            char topChar = stack[top--];
            if ((c == ')' && topChar != '(') ||
                (c == '}' && topChar != '{') ||
                (c == ']' && topChar != '[')) {
                return false;
            }
        }
    }
    
    // If the stack is empty at the end, all brackets were matched correctly
    return top == -1;
}
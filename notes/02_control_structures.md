# Unit 2: Control Structures

## Conditional Statements
- if, if-else, nested if
- switch-case

## Loops
- for, while, do-while
- break and continue

### Example
```c
#include <stdio.h>
int main() {
    int n=5;
    for(int i=1; i<=n; i++) {
        if(i==3) continue;
        printf("%d\n", i);
    }
    return 0;
}
```

### Practice Problems
1. Write a C program to check whether a number is prime.
2. Print Fibonacci series up to n terms using while loop.
3. Use switch to make a simple calculator.

# Unit 3: Arrays and Strings

## Arrays
- Definition: contiguous memory blocks.
- Indexing starts from 0.
- 1D, 2D arrays.

## Strings
- Character arrays ending with '\0'.
- Common functions: strlen, strcpy, strcat.

### Example
```c
#include <stdio.h>
#include <string.h>
int main() {
    char name[20] = "Hello";
    printf("Length = %d", (int)strlen(name));
    return 0;
}
```

### Practice Problems
1. Store 10 integers in an array and find the largest.
2. Multiply two matrices (2D arrays).
3. Reverse a string without using strrev().

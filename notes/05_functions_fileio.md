# Unit 5: Functions & File Handling

## Functions
- Declaration, Definition, Call.
- Arguments: by value, by reference.
- Return types.

## Scope & Lifetime
- Local, Global, Static variables.

## File Handling
- fopen, fclose, fprintf, fscanf.

### Example
```c
#include <stdio.h>
int add(int a, int b) { return a+b; }
int main() {
    FILE *fp = fopen("output.txt", "w");
    int s = add(5,10);
    fprintf(fp, "Sum=%d", s);
    fclose(fp);
    return 0;
}
```

### Practice Problems
1. Write a function to calculate factorial using recursion.
2. Implement function to check palindrome.
3. Read and write student details to file.

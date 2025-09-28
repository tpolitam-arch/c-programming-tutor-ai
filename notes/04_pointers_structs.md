# Unit 4: Pointers & User Defined Data Types

## Pointers
- Variable that stores address of another variable.
- Operators: & (address), * (dereference).

## Pointer Arithmetic
- Increment/decrement moves by size of data type.

## Structures & Unions
- Group of related data items.
- Difference: Structure stores all members, Union shares memory.

### Example
```c
#include <stdio.h>
struct Student {
   int roll;
   char name[20];
};
int main() {
   struct Student s1 = {1, "Alice"};
   printf("Roll: %d Name: %s", s1.roll, s1.name);
   return 0;
}
```

### Practice Problems
1. Write a program to swap two numbers using pointers.
2. Create a struct for Book (title, author, price).
3. Implement array of structures for 5 students.

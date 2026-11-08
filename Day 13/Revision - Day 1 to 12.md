
#                                                                                                C++ Revision - Days 0 to 12
---

# Setup & Introduction

C++ is a high-performance, compiled, low-level language used for system software, game engines, and embedded systems.

Source code is stored in `.cpp` files and compiled into executable binaries.

---
# Compilation & Output

We use `g++` to compile source code into an executable. `std::cout` prints output to the console.

```
#include <iostream>

int main() {
    std::cout << "Hello World!\n"; // \n moves cursor to next line
    return 0; // return 0 tells OS program ran successfully
}
```

Compile and run via terminal:

```
g++ main.cpp -o main
./main
```

---
# Variables, Data Types & Sizeof

Variables store data of a specific type. `const` creates read-only variables. `sizeof` returns size in bytes.

```
int age = 20;               // Integer (typically 4 bytes)
double pi = 3.14159;        // Floating point (8 bytes)
char grade = 'A';           // Single character (1 byte)
bool isPassed = true;       // Boolean (1 byte)
const double GRAVITY = 9.8; // Constant variable

std::cout << sizeof(age);   // output: 4
```

`unsigned` types store only non-negative numbers, doubling their positive range.

---
# Type Conversion

Converting data from one type to another can be done automatically (implicit) or manually (explicit).

```
// Implicit conversion
int num = 10;
double val = num; // converts int to double automatically

// Explicit conversion (static_cast)
double price = 9.99;
int rounded = static_cast<int>(price); // output: 9
```

---
# Input & Strings

`std::cin` reads single space-delimited inputs. `std::getline` reads an entire line including spaces.

```
#include <iostream>
#include <string>

int main() {
    std::string name;
    std::cout << "Enter name: ";
    std::getline(std::cin, name); // reads full name with spaces
    return 0;
}
```

---
# Operators & Errors

C++ supports Arithmetic (`+`, `-`, `*`, `/`, `%`), Assignment (`+=`, `-=`), Comparison (`==`, `!=`, `>`, `<`), and Logical (`&&`, `||`, `!`) operators.

- **Compilation Error:** Syntax or undeclared variable errors caught at compile time.
    
- **Runtime Error:** Program crashes during execution (e.g., division by zero).
    
- **Logical Error:** Code compiles and runs but gives incorrect results.
    

---
# Conditionals & Ternary Operator

Conditions evaluate logic to execute specific code blocks.

```
int score = 85;

if (score >= 90) {
    std::cout << "Grade A\n";
} else if (score >= 80) {
    std::cout << "Grade B\n";
} else {
    std::cout << "Grade C\n";
}

// Ternary operator: condition ? true_expr : false_expr
int maxVal = (10 > 20) ? 10 : 20; // output: 20
```

`switch` compares a variable against fixed primitive values:

```
int day = 2;
switch (day) {
    case 1: std::cout << "Mon"; break;
    case 2: std::cout << "Tue"; break; // executed
    default: std::cout << "Invalid";
}
```

---
# Loops & Jump Statements

Loops repeat code while a condition remains `true`.

```
// For loop: fixed repetitions
for (int i = 1; i <= 3; i++) {
    std::cout << i << " "; // output: 1 2 3
}

// While loop: condition checked before execution
int count = 1;
while (count <= 3) {
    count++;
}

// Do-While loop: runs at least once
do {
    std::cout << "Runs once\n";
} while (false);
```

- `break`: Exits the loop completely.
    
- `continue`: Skips current iteration to the next cycle.
    
- `return`: Immediately exits the function.
    

---
# Functions & Passing Arguments

Functions encapsulate reusable logic.

- **Pass by Value:** Function gets a copy; original variable remains unchanged.
    
- **Pass by Reference (`&`):** Function accesses original variable directly.
    

```
void modify(int val, int& ref) {
    val = 100; // changes copy only
    ref = 100; // changes original variable
}

int main() {
    int a = 10, b = 10;
    modify(a, b);
    // a is still 10, b is now 100
    return 0;
}
```

Functions can also use **Default Arguments** (must be placed at the end of parameter lists) and **Function Overloading** (same name with different parameter types/counts).

---
# Inline Functions & Recursion

`inline` requests the compiler to substitute function calls directly with the function body for small performance gains.

**Recursion** is when a function calls itself. It requires a base case to prevent infinite recursion and stack overflow.

```
int factorial(int n) {
    if (n <= 1) return 1; // Base case
    return n * factorial(n - 1); // Recursive case
}

// factorial(4) output: 24
```

---
# Scope, Lifetime & Storage Duration

- **Local Scope:** Variables declared inside `{}` exist only within that block.
    
- **Global Scope:** Variables declared outside functions are accessible everywhere.
    
- **Shadowing:** Local variables mask global ones with the same name. Use `::` to access global variable.
    
- **Automatic Duration:** Local variables created on block entry, destroyed on exit.
    
- **Static Duration (`static`):** Variables created once when program starts and persist until exit while keeping their local scope.
    
- **Dynamic Duration (`new`/`delete`):** Variables allocated manually on the heap.
    

```
int* ptr = new int(42); // allocated dynamically
std::cout << *ptr;      // output: 42
delete ptr;             // free memory to prevent memory leak
```

---
# Header Files & Multi-File Projects

Header files (`.h` / `.hpp`) store function declarations, while source files (`.cpp`) store definitions.

Use include guards (`#ifndef` / `#define` / `#endif` or `#pragma once`) to prevent duplicate definition errors.

```
// math_utils.h
#ifndef MATH_UTILS_H
#define MATH_UTILS_H
int add(int a, int b);
#endif

// math_utils.cpp
#include "math_utils.h"
int add(int a, int b) { return a + b; }
```

Compile multi-file programs together:

```
g++ main.cpp math_utils.cpp -o program
```

---
# Arrays

Arrays store fixed-size contiguous collections of elements of the same data type.

```
int numbers[4] = {10, 20, 30, 40};

// Accessing & Modifying
numbers[0] = 15;

// Array Size Calculation
int length = sizeof(numbers) / sizeof(numbers[0]); // output: 4

// Range-based for loop
for (int val : numbers) {
    std::cout << val << " "; // output: 15 20 30 40
}
```

Character arrays (strings) automatically end with a null terminator character `'\0'`.
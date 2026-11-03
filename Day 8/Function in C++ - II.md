#                                                                                                                  Functions in C++ - II
---

# Function overloading

Function overloading is when we create multiple functions that have the exact same name but different parameters. We use it so we do not have to remember many different function names for doing the same kind of task.

Multiple functions can have the same name if they have different parameter lists. We can achieve this by:
- Using different parameter types (like `int` and `double`).
- Using a different number of parameters.

**Note:-** Function overloading cannot be achieved by changing only the return type of the functions.

```cpp
#include <iostream>

// Function with two integer parameters
int add(int num1, int num2) {
	return num1 + num2;
}

// Function overloading using different parameter types
double add(double num1, double num2) {
	return num1 + num2;
}

// Function overloading using different numbers of parameters
int add(int num1, int num2, int num3) {
	return num1 + num2 + num3;
}

int main() {
	
	std::cout<< add(5, 5)<< "\n"; // output: 10
	std::cout<< add(5.5, 2.5)<< "\n"; // output: 8
	std::cout<< add(2, 3, 4)<< "\n"; // output: 9
	
	return 0;
	
}
```

---
# Default arguments

Default arguments are default values we assign to a function's parameters. We use them so that if the person calling the function does not provide an argument, the function will automatically use the default value instead of giving an error. 

```cpp
<return_type> <function_name>(<data_type> <variable_name> = <default_value>) {
	// code
}
```

**Note:-** The basic rule is that parameters with default arguments must always be placed after the normal parameters (parameters without default arguments).

```cpp
#include <iostream>

// Assigning a default value of 10 to num2
int add(int num1, int num2 = 10) {
	return num1 + num2;
}

int main() {

	// Here we provide both arguments
	std::cout<< add(5, 5)<< "\n"; // output: 10
	
	// Here we do not provide the second argument, so it uses the default value 10
	std::cout<< add(5)<< "\n"; // output: 15

	return 0;

}
```

---
# Inline functions

Inline functions are normal functions declared with the `inline` keyword. We use them for very small functions to make the program run a little faster. When we call an inline function, the compiler attempts to replace the function call directly with the function's code.

```cpp
inline <return_type> <function_name>(<parameters>) {
	// code
}
```

**Warning :-** The `inline` keyword is only a request to the compiler. It does not guarantee that the compiler will replace every function call with the function body.

```cpp
#include <iostream>

// Declaring an inline function
inline int multiply(int num1, int num2) {
	return num1 * num2;
}

int main() {

	// The compiler might replace this call directly with: 4 * 5
	std::cout<< multiply(4, 5)<< "\n"; // output: 20

	return 0;

}
```

---
# Recursion

Recursion is a process where a function calls itself. We use it to solve larger problems by breaking them down into smaller, similar sub-problems. 

For recursion to work properly, we need a **base condition**. This is a simple condition that stops the function from calling itself again. 

**Warning :-** If a recursive function does not have a proper base condition, it will keep calling itself infinitely until the program crashes.

```cpp
#include <iostream>

int countNumbers(int value) {
	// Base condition to stop recursion
	if (value == 0) {
		return 0;
	}
	
	std::cout<< value<< "\n";
	
	// The function calls itself with a smaller value
	return countNumbers(value - 1);
}

int main() {

	countNumbers(3); 
	/* 
	output: 
	3
	2
	1
	*/

	return 0;

}
```

---
# Scope: local and global variables

Variable scope means the specific region in the code where a variable can be accessed and used.

- `Local variables`: These are variables declared inside a function or a block of code `{}`. They can only be accessed inside that specific block.
- `Global variables`: These are variables declared outside of all functions. They can be accessed from anywhere in the entire program.

The main difference is that local variables are hidden to the outside of their function, while global variables are shared across the whole program.

```cpp
#include <iostream>

// This is a global variable
int globalNum = 100;

void printNumbers() {
	// This is a local variable
	int localNum = 10;
	std::cout<< "Local: "<< localNum<< "\n";
	std::cout<< "Global accessed in function: "<< globalNum<< "\n";
}

int main() {

	printNumbers();
	// output: Local: 10
	// output: Global accessed in function: 100
	
	std::cout<< "Global accessed in main: "<< globalNum<< "\n"; 
	// output: Global accessed in main: 100
	
	// std::cout<< localNum; // Error: localNum cannot be accessed here

	return 0;

}
```

---
# Variable lifetime and storage duration

Variable lifetime means how long a variable stays active in the computer's memory before it gets destroyed. Storage duration is the underlying rule that determines this lifetime at a basic level.

- **Lifetime of local variables**: It starts when the function or block runs, and ends the moment the block finishes.
- **Lifetime of global variables**: It starts when the program begins and ends when the whole program closes.
- **Lifetime of static local variables**: If we use the `static` keyword on a local variable, its lifetime extends to the end of the program, even though it can still only be accessed inside its block.

**Note:-** Scope is about **where** you can use the variable, but lifetime is about **how long** the variable exists in memory.

```cpp
#include <iostream>

void counter() {
	// static local variable
	static int value = 0; 
	
	// normal local variable
	int num1 = 0; 
	
	value += 1;
	num1 += 1;
	
	std::cout<< "Static value: "<< value<< ", Local num1: "<< num1<< "\n";
}

int main() {

	counter(); // output: Static value: 1, Local num1: 1
	counter(); // output: Static value: 2, Local num1: 1
	counter(); // output: Static value: 3, Local num1: 1
	
	// The static variable remembers its value across function calls because its lifetime lasts until the program ends.

	return 0;

}
```
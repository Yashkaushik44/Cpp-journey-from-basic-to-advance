#                                                                                                               C++ Functions

---

# What are functions?

A function is a block of code which has a name and does one specific task. We write the function once and then we can use it (call it) as many times as we want.

- Functions stop us from writing the same code again and again.
- They make the code easy to read and easy to fix.
- `main()` is also a function. It is the function from where our program starts.

```cpp
#include <iostream>

void sayHello() {

	std::cout << "Hello!"; // this function prints Hello!

}

int main() {

	sayHello(); // calling the function, output: Hello!

	return 0;
	
}
```

---

# Function declarations and definitions

- A **declaration** tells the compiler that a function exists. It has the return type, name and parameters but no body. It ends with a semicolon `;`.
- A **definition** is the full function. It has the same things as the declaration and also the body `{ }` which has the code of the function.

```cpp
#include <iostream>

int add(int num1, int num2); // declaration (no body)

int main() {

	std::cout << add(2, 3); // output: 5

	return 0;
	
}

int add(int num1, int num2) { // definition (has the body)

	return num1 + num2;
	
}
```

- A function must be declared before we call it. Here `add` is called inside `main()` but defined after it, so the declaration at the top is needed.
- If we define the function before `main()`, we do not need a separate declaration.

```cpp
<return_type> <function_name>(<parameters>); // declaration

<return_type> <function_name>(<parameters>) { // definition

	// code

}
```

==🔴**Warning :-** This above code is the syntax for declaring and defining a function in C++. I used `<>` to enter the input and these symbols should not be considered as syntax.==

---

# Function parameters and arguments

- **Parameters** are the variables written inside the brackets `( )` when we define the function.
- **Arguments** are the actual values we pass inside the brackets `( )` when we call the function.
- The argument value gets stored in the parameter.

```cpp
#include <iostream>

void printDouble(int value) { // value is the parameter

	std::cout << value * 2;
	
}

int main() {

	printDouble(5); // 5 is the argument, output: 10

	return 0;
	
}
```

**Note:-** The number of arguments and their data types should match the parameters of the function.

---

# Return types and return values

- The **return type** is the data type written before the function name. It tells what type of value the function will give back.
- The **return value** is the actual value that the function gives back using the `return` keyword.
- When `return` runs, the function stops and the value goes back to the place where the function was called.

```cpp
#include <iostream>

int multiply(int num1, int num2) { // return type is int

	return num1 * num2; // return value

}

int main() {

	int result = multiply(4, 5);
	
	std::cout << result; // output: 20

	return 0;
	
}
```

- `void` means the function does not return any value. So we do not use `return` with a value in it.

```cpp
#include <iostream>

void printMessage() { // return type is void

	std::cout << "Learning functions"; // output: Learning functions

}

int main() {

	printMessage();

	return 0;
	
}
```

---

# Pass by value

- In pass by value, the function gets a copy of the argument.
- If the function changes the parameter, only the copy changes.
- The original variable stays the same.

```cpp
#include <iostream>

void changeValue(int value) {

	value = 50; // changes only the copy

}

int main() {

	int num1 = 10;
	
	changeValue(num1);
	
	std::cout << num1; // output: 10 (original did not change)

	return 0;
	
}
```

---

# Pass by reference

- In pass by reference, the function does not get a copy. The parameter becomes another name for the original variable.
- We use the `&` symbol after the data type in the parameter to pass by reference.
- If the function changes the parameter, the original variable also changes.

```cpp
#include <iostream>

void changeValue(int& value) { // & makes it pass by reference

	value = 50; // changes the original variable

}

int main() {

	int num1 = 10;
	
	changeValue(num1);
	
	std::cout << num1; // output: 50 (original changed)

	return 0;
	
}
```

**Note:-** The `&` is written only in the function parameter. We call the function normally, like `changeValue(num1);`.

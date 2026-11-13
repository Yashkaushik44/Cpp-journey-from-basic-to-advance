#                                                           Introduction to pointers and memory addresses in C++
---

# Understanding Memory Addresses

Every variable we create is stored inside our computer's memory(RAM) and a memory address is simply the **unique** location where that variable lives inside the memory.

We use `& -> Ampersand or Address of`  to fetch the memory.

```cpp
//example

#include <iostream>

int main() {

	int age = 18;
	
	std::cout<< &age<< "\n";

	return 0;
	
}
```

**Note:-** The address will always be different from the previous one because the memory is located on run time and after the program is completely executed it is flushed and re allocated again when the program is executed again.

---

# Introduction to Pointers

It is a special variable that stores the memory address of another variable. It basically points at the address of a variable it is assigned.

```cpp
//The below is the syntax of pointers in C++. I used <> to insert and it should not be treated as a syntax

#include <iostream>

int main() {

	<data_type> <variable_name> = <value>;
	
	<data_type>* <pointer_name> = &<variable_name>;

	return 0;
	
}
```

**Note:-** The data type of the pointer and the variable you are storing in it should be the same.

```cpp
//example

#include <iostream>

int main() {

	int age = 18;
	
	int* ptr_Age = &age;
	
	std::cout<< ptr_Age<< "\n"; // output: Address of age
	
	std::cout<< *ptr_Age<< "\n"; // output: Value of age, 18

	return 0;
	
}
```

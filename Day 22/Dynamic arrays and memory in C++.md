
#                                                                        Dynamic arrays and memory leaks in C++
---

# Dynamic Arrays

An array created on the Heap at runtime using `new[]` so you can choose its size while program is running. 

```cpp
//example

#include <iostream>

int main() {

	int n = 5;
	int* arr = new int[n]; //size decide at runtime
	
	delete[] arr;

	return 0;
	
}
```

---
# Limitations of Dynamic Arrays

They still cannot automatically resize, do not know their own size when passed to function, lack bounds checking, and require manual cleanup.

```cpp
//example

#include <iostream>

int main() {
	
	int* arr = new int[3];
	arr[5] = 10;
	
	delete[] arr;

	return 0;
	
}
```

---

# Dangling Pointers 

A pointer that still holds the memory address of data that has already been deleted or destroyed.

```cpp
//example

#include <iostream>

int main() {

	int* ptr = new int(10);
	
	delete ptr;
	
	ptr = nullptr;

	return 0; 
	
}
```

---

# Memory Leak

Memory reserved on the Heap with `new` that is never freed with `delete` staying locked and unusable until the program ends.

```cpp
//example

#include <iostream>

	void leak() {
	
	int* ptr = new int(50); // "ptr" disappears when the function ends, leaving 50 trapped on the Heap forever
	
	};
```

---

# Undefined Behaviour

Unpredictable program execution (like - crashing, garbage values or silent bugs) cause by breaking C++ memory rules.

```cpp
//example

#include <iostream>

int main() {

	int* ptr = new int(10);
	
	delete ptr;
	
	std::cout<< *ptr; // Reading deleted memory might crash or print garbage value

	return 0;
	
}
```


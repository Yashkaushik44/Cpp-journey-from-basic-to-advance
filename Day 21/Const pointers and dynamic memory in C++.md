#                                                                           Const pointers and dynamic memory in C++
---

# Const Pointers and Pointers to `const`

Using `const` with pointers restricts either modifying the value pointed to, changing the memory address stored in the pointer, or both.

A pointer to `const` (`const int* ptr`) points to a constant value. The value cannot be changed through the pointer, but the pointer itself can be reassigned to point to another address.

A `const` pointer (`int* const ptr`) is a constant pointer that cannot be reassigned to another memory address once initialized, though the value at that address can be modified.

A `const` pointer to `const` (`const int* const ptr`) locks both the address and the value, so neither can be modified through the pointer.

```
//example

#include <iostream>

int main() {
	
	int a = 10;
	int b = 20;
	
	// Pointer to const: cannot change value, can change address
	const int* ptr1 = &a;
	// *ptr1 = 15; // Error: value is read-only through ptr1
	ptr1 = &b; // Allowed: ptr1 can point to a different variable
	std::cout << "ptr1 value: " << *ptr1 << "\n"; //output 20
	
	// Const pointer: can change value, cannot change address
	int* const ptr2 = &a;
	*ptr2 = 15; // Allowed: value of a becomes 15
	// ptr2 = &b; // Error: ptr2 cannot be reassigned
	std::cout << "ptr2 value: " << *ptr2 << std::endl; //output 15
	
	// Const pointer to const: cannot change value or address
	const int* const ptr3 = &a;
	// *ptr3 = 30; // Error: value cannot be changed
	// ptr3 = &b; // Error: address cannot be changed
	std::cout << "ptr3 value: " << *ptr3 << "\n"; //output 15

	return 0;
	
}
```

Use:- Read pointer declarations from right to left to avoid confusion (`int* const ptr` is a constant pointer to an int, while `const int* ptr` is a pointer to a constant int). Also, a `const` pointer must be initialized at the time of declaration.

---

# Dynamic Memory Allocation with `new`

Dynamic memory allocation is the process of requesting memory from the heap at runtime instead of using fixed stack memory at compile time. It is used when the required memory size is not known beforehand or when data needs to survive beyond the scope in which it was created.

The `new` operator allocates memory on the heap for a variable or an array and returns the starting memory address, which is stored in a pointer.

```
//example

#include <iostream>

int main() {
	
	// Allocating and initializing a single variable on the heap
	int* ptr = new int(42);
	
	std::cout << "Dynamic value: " << *ptr << "\n"; //output 42
	
	*ptr = 99; // Modifying the value stored in dynamic memory
	std::cout << "Updated value: " << *ptr << std::endl; //output 99
	
	// Allocating a dynamic array on the heap
	int size = 3;
	int* arr = new int[size]{10, 20, 30};
	
	std::cout << "First element: " << arr[0] << "\n"; //output 10
	std::cout << "Second element: " << *(arr + 1) << "\n"; //output 20
	
	delete ptr;
	delete[] arr;

	return 0;
	
}
```

Use:- Always store the address returned by `new` inside a pointer immediately; otherwise, the allocated memory address is lost and cannot be accessed or freed later.

---
# Releasing Memory with `delete`

Dynamically allocated memory on the heap is not released automatically when a function or block ends, so it must be manually freed to prevent memory leaks.

The `delete` operator releases memory allocated for a single variable using `new`. The `delete[]` operator releases memory allocated for an array using `new[]`.

Using `delete` does not destroy the pointer variable itself; the pointer still holds the old memory address and becomes a dangling pointer until it is reassigned or set to `nullptr`.

```
//example

#include <iostream>

int main() {
	
	int* ptr = new int(50);
	std::cout << "Value before delete: " << *ptr << "\n"; //output 50
	
	delete ptr; // Releases the heap memory
	ptr = nullptr; // Prevents dangling pointer
	
	if(ptr == nullptr) {
	
		std::cout << "Memory released and pointer is safely null\n";
		
	}
	
	int* scores = new int[3]{70, 80, 90};
	std::cout << "Score 1: " << scores[0] << std::endl; //output 70
	
	delete[] scores; // Releases the entire dynamic array
	scores = nullptr;

	return 0;
	
}
```

Use:- Always pair `new` with `delete` and `new[]` with `delete[]`, and immediately set the pointer to `nullptr` after releasing memory.

🔴**Warning:- Never use `delete` on normal stack variables, never mix `delete` with `new[]`, and never dereference a pointer after deleting it. Doing so causes undefined behavior, memory corruption, or program crashes.**
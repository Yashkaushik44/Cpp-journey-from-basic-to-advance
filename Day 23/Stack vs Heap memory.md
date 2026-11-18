#                                                                                              Stack vs Heap memory

---

# Stack Memory

A fast, automatically managed region of memory used for static allocation of local variable variables and function call tracking in a Last in first out (LIFO) order.

```cpp
//example

#include <iostream>

void stackExample() {

	int count = 10;
	double scores[3] = {95.5, 99.0, 88.2};
} // both the score and count are automatically destroyed here when the function exits
```

---
# Heap Memory

 A larger, dynamically manged pool of memory used for manual or smart pointer allocation of data whose size or lifetime is determined at runtime.

```cpp
//example

#inlcude <memory>

void heapExample() {

	int* ptr = new int(42);
	
	delete ptr; // must be freed manually to avoid a memroy leak

}
```

---
# Difference between Stack and Heap memory

| Stack Memory                                                                          | Heap Memory                                                                                                            |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Automatically allocated and freed by the<br>compiler when variables go out of scope.  | Manually allocated and freed by the<br>programmer (or via smart pointers) and <br>persists until explicitly destroyed. |
| Extremely fast because allocation only requires<br>moving a single CPU stack pointer. | Slower because the runtime must search for a free memory<br>block of sufficient size and handle book keeping.          |
| Strictly limited in size with zero fragmentation.                                     | Limited mainly by system RAM/virtual memory, though frequent<br>allocations de allocations  can fragment it.           |

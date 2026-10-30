
#                                                                                         Type conversion's in C++
---

# Type conversion

There are two types of type conversions in C++.

- Implicit
	In implicit type conversion, the compiler itself converts one data type into another.
	example:- 
	```cpp
	#include <iostream>
	
	int main() {
		
		int num = 10;
		
		double value = num; //This makes a variable names value with datatype double (floating data type) and stores num's value after convering it into double data type.
		
		return 0;
		
	}
	```
	
- Explicit
	In explicit type conversion, the developer has to manually convert one data type into another using `static_cast`.
	example:-
	```cpp
	#include <iostream>
	
	int main() {
	
		double value = 10.5;
		int num = static_cast<int>(value); // syntax for static cast:- static_cast<<data_type>>(<variable>)	
		
		return 0;
	}
	```



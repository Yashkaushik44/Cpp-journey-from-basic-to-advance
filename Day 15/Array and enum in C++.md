
#                                                                                          Array and enum in C++
---

# Std::array

It is a fixed-size list in C++ that works like a classic C-array but gives you modern safety features and helper functions without sacrificing any speed. To use this we need to include `array` in our code.

```cpp
// this is the syntax for std::array in C++. I used <> to specify input and this should not be considered syntax.

#include <iostream>
#include <array>

int main() {
	
	std::array<<data_type>, <size>> <variable_name> = {<value>};
	
	//access the elements:- 
	
	for(<iterator> : <variable_name>) {
	
		std::cout<< <iterator> << " ";
		
	}

	return 0;
	
}
```

```cpp
//example

#include <iostream>
#include <array>

int main() {

	std::array<int, 4> numbers = {1,2,3,4};
	
	for(int num : numbers) {
		
		std::cout<< num<< " ";
	
	}
	
	return 0;
	
}
```

---

# enum 

It is a simple way to create a list of named choices that automatically maps each item to a position number that converts directly into a regular integer.

```cpp
//example

#include <iostream>

int main() {
	
	enum Color {Red, Green, Blue};
	
	Color c = Red;
	
	int val = Red; // it converts Implicitly to its value (index number by default)
	
	return 0;
	
}
```

---

# enum class

A safer version of `enum` that locks choices inside its own group and requires `GroupName::Choice so` so different lists don't mix up or accidentally compare as regular numbers.

```cpp
//example

#include <iostream>

int main() {

	enum class Status {Success, Warning, Error};
	
	Status s = Status::Success; // cannot access without this syntax format
	
	int val = static_cast<int>(Status::Success); // Requires explicit cast

	return 0;
	
}
```

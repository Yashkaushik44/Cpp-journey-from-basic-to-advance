
#                                                                          Type alias and structure bindings in C++

---

# Type aliasing

It's used to create a cleaner and more readable alternative name for an existing data type.

```cpp
// This is the syntax of type aliasing "using" in C++. I used <> to take input and this should not be considered syntax

#include <iostream>

int main() {

	using <alias_name> = <data_type>;
	
	<alias_name> <variable_name> = <value>;

	return 0;
	
}
```

```cpp
//example

#include <iostream>

int main() {

	using Score = int;
	
	Score player = 84;

	return 0;
	
}
```

---

# Structured bindings 

It is used to instantly unpack a multi value object (like a tuple, array, or struct) into separate, named variables.

```cpp
//example

#include <iostream>
#include <string>
#include <utility>

int main() {

	std::pair<int, std::string> student = {101, "User"}; // pair is used to give a variable multiple data types to hold multiple data type values as an array.
	
	auto [id, name] = student; // auto automatically assigns the variables to there respective positional value in the array.
	
	return 0;
	
}
```

#                                                                                                                   Functions in C++ - III
---

# Function Overloading 

We use function overloading when we want to have multiple functions with the exact same name but different parameters.

```cpp
//this is the syntax for using function overloading. We are using <> for getting your input in it and it is not a syntax

#include <iostream>

<return_type> <function_name>(<data_type> <variable_name1>) {
	
	<code_block>
	
}

<return_type> <function_name>(<data_type> <variable_name1>, <data_type> <variable_name2>) {
	
	<code_block>
	
}

int main() {
	
	<function_name>(<value1>);
	<function_name>(<value1>, <value2>);
	
	return 0;
	
}
```

**Warning:-** Function overloading only works if the parameters are different in type, number, or sequence. You cannot overload functions by only changing the return type.

example:

```cpp
#include <iostream>

void add(int a, int b) { //this function takes two integers
	
    std::cout<< "Sum of two is: " << a + b << "\n";
	
}

void add(int a, int b, int c) { //this function shares the same name but takes three integers
	
    std::cout<< "Sum of three is: " << a + b + c << "\n";
	
}

int main() {

	add(5, 10); //this will call the first function
	
	add(5, 10, 15); //this will call the second function
	
	return 0;
	    
}
```
---

# Default Arguments


We use default arguments to assign a default value to a parameter. If we don't pass a value when calling the function, it will use this default value automatically.

```cpp
//this is the syntax for using default arguments. We are using <> for getting your input in it and it is not a syntax.

#include <iostream>

<return_type> <function_name>(<data_type> <variable_name> = <default_value>) {
	
	<code_block>
	
}

int main() {
	
	<function_name>(); //this will use the default value
	
	<function_name>(<custom_value>); //this will override the default value
	
	return 0;
	
}
```

**Note:-** Default arguments must always be placed at the very end of the parameter list.

example:-

```cpp
 /*We want this function to greet a user with a default name if no name is provided*/

#include <iostream>
#include <string>

void greet(std::string name = "Guest") { //"Guest" is the default value here

	std::cout<< "Hello " << name << "!\n"; 
	
}

int main() { 

	greet("Alice"); //we provide a value, so it outputs Hello Alice!
	
	greet(); //we don't provide a value, so it uses the default and outputs Hello Guest!
	
	return 0;	
	
}
```
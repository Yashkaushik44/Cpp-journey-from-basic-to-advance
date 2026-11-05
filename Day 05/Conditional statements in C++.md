
#                                                                                                                   Conditional statements
---

# if - else if - else

We use conditions in C++ to perform case based logical programming.

For this we use `if else if else` .

```cpp
//this is the syntax for using conditons. We are using <> for getting your input in it and it is not a syntax

#include <iostream>

int main() {
	
	if (<condition>) {
		
		<code_block>
		
	}else if (<condition>) {
		
		<code_block>
		
	}else{
	
		<code_block>
	
	}
	
		return 0;
		
}
```

**Note:-** You can only use `if` and `else` one time in a condition block but you can use `else if `as much times as needed.

It is not necessary to use `else if` every time, you can also use `if - else` pair if needed.

example:-

```cpp
 /*We want this function to check if num1 `is odd or even*/

#include <iostream>

int main() {

	int num1 = 4;
	
	if (num1 % 2 == 0) { //we are checking if the remainder is equals to 0.
	
		std::cout<< "num1 is even\n"; //if num1 is zero then this code block will execute 
		
	}else{ //if the value doesn't satisfy the above if statement then this else condition will work
	
		std::cout<< "num1 is odd\n"; //this code will run if num1 doesn't satisfy any of the other condition statements
		
	}
	
	return 0;
	
}
```

---

# Nested conditions 

We use nested conditions when we need to check a second condition only after the first condition is satisfied.

```cpp
//this is the syntax for using nested conditions. We are using <> for getting your input in it and it is not a syntax

#include <iostream>

int main() {
	
	if (<condition>) {
		
		if (<condition>) {
		
			<code_block>
		
		}
		
	}else if (<condition>) {
		
		if (<condition>) {
		
			<code_block>
		}
		
	}else {
	
		if (<condition>) {
		
			<code_block>
			
		}
	}
	
		return 0;
	
}
```

This is useful to solve problems that need multiple conditions to be satisfied.

example:

```cpp
#include <iostream>

int main() {

	int marks;
	
	std::cout<< "Enter your marks: "; 
	std::cin>> marks; //this prompt's the user to enter their marks in integer data type and store it in marks variable.
	
	if (marks >= 33) { //parent conditon
	
	    std::cout<< "You passed!\n";
	
	    if (marks >= 90) { //this only works when the parent conditon is fullfilled 
	    
	        std::cout<< "You got a distinction!\n";
	    
	    }
	        
	}else {
	
	    std::cout<< "You failed.\n";
	    
	}
	    
	    return 0;
	    
}
```
---

# switch and cases


We use switch and cases to compare a value against multiple patterns and execute the code for the first matching case. It can be used as an alternative for `if else if else` in some cases.

**Warning:-** For applying conditions on range, we have to use `if else if else` statements. Switch statement only works on certain values not on range.

```cpp
//this is the syntax for using match and cases. We are using <> for getting your input in it and it is not a syntax.

#include <iostream>

int main() {
	
	<data_type> <variable_name>;
	
	switch (<variable_to_compare_against>) {
	
		case <value1>:
		
			<code_block>
			
			break;
			
		case <value2>:
		
			<code_block>
			
			break;
			
		case <value3>:
		
			<code_block>
			
			break;
			
		default:
		
			<code_block>
			
	}
			
	return 0;
	
}
```

**See this file for the example: ![example.cpp](code1.cpp)**

---

# Logical operators

Operators used to combine or reverse conditions to get a result.

**They are of 3 types:-**

- && (and)
- || (or)
- ! (not)

```cpp
//this is the syntax for using logical operators. We are using <> for getting your input in it and it is not a syntax.

#include <iostream>

int main() {
 
	if (<condition> && <condition>) { //Strictly only works when both condtions are True.
		
		<code_block>
		
	}else if (<condition> || <condition>) { //works when even one of the conditon is True
		
		<code_block>
		
	}else if (!<condition>) { //This reverse the boolean value, changing True to False and False to True, example:- not True -> False
	
		<code_block>
		
	}else {
	
		<code_block>
		
	}

	return 0;	
	
}
```

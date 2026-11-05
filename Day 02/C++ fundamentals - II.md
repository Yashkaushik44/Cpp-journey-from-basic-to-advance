
#                                                                                              C++ basics
---

# Using namespace

On day - 1 we had written a code that prints hello world. 

```cpp
#include <iostream>

int main() {

	std::cout<< "Hello World!\n";
	
	return 0;
	
}
```

We use `std` library function a lot, there is a way to actually skip writing the library name for using the function, that was is by using namespace.

```cpp
#include <iostream>

using namespace std; // By writing this line we can skip writing std again and again in the code

int main() {

	cout<< "Hello World!\n";

	return 0;
	
}
```

**Warning :-** using namespace function for some libraries is considered a bad practice because at the time of code review or bug fixing it becomes hectic to pin point which function comes from which library so, avoid using them at maximum time.

---
# Operators

## Arithmetic operators

Arithmetic operators are maths operators used to perform arithmetic calculations.

**The following operators are in descending priority order**

- `()`
	anything inside the brackets will be given the highest priority.
	`
- `+x, -x`
	these are unary number's -> -5, +8.
	
- ` *,  /, %`
	`*` -> This is the operator symbol used for multiplication
	`/` -> This is the operator symbol used for float division.
	`%` -> This is the operator used for getting the remainder after division (Modulo operator). 
	
- `+, -`
	`+` -> This is the operator used for addition.
	`-` -> This is the operator used for subtraction.

If the priority of a set of operators are same then they will be solved from left to right.

```cpp
'''example code'''
#include <iostream>

int main() {

	int num = (5 + 5) - 5 * 4 % 2 / 2;
	
	std::cout<< num<< "\n"; // output: 10
	
	return 0;
	
}
```

## Assignment operators 

operators used for assigning values to a variable.

- `=`
	This is used to assign a value equal to a variable.
	
- `-=` 
	This is used to assign a value to a variable after subtracting the variable to the value.
	example:- `num = num - 3` and `num -= 3` are the same thing.
	
- `+=` 
	This is used to assign a value to a variable after adding the variable to the value.
	example:- `num = num + 3` and `num += 3` are the same thing.
	
- `*=`
	This is used to assign a value to a variable after multiplying the variable to the value.
	example:- `num = num * 2` and `num *= 2` are the same thing.
	
- `/=` 
	This is used to assign a value to a variable after float dividing the variable to the value.
	example:- `num = num / 2` and `num /= 2` are the same thing.
	
- `%=`
	This is used to assign a value to a variable after getting the remainder of their division.
	example:- `num = num % 2` and `num %= 2`.


## Comparison Operators

Operators used to compare two values and return a Boolean result.

- `==`
	This checks if the left side value is equal's to the right side value.
	
- `!=`
	This checks if the left side value is **not equal's** to the right side value.
	
- `>` 
	This checks if the left side value is greater than the right side value.
	
- `<`
	This checks if the left side value is less than the right side value.
	
- `>=` 
	This checks if the left side value is greater than or equal to the right side value.
	
- `<=`
	This checks if the left side value is less than or equal to the right side value.

---
# Compilation Error

It occurs when we use an undeclared variable, wrong syntax or rules.

```cpp
#include <iostream>

int main() {

    cout << "Hello\n"; // Error: cout is undeclared without the use of std:: or namespace.
    
    return 0;
    
}
```

# Run Time Error

It occurs when we run the code after compiling it but the code trips into an unexpected bug or error.

```cpp
#include <iostream>

int main() {

	int num = 10 / 0; // this code compiles but at the time of running, the code will unexpectedly be dumped due to division by zero error.

	return 0;

}
```

# Logical Error

This error occurs when the program does not produces the desired output even though the program compiles and runs.
It's more of a bug because it does not crash the program itself but gives trash output. 
It occurs when you write the logic of your code wrongly.

```cpp
#include <iostream>

int main() {

	/* We want this code to give us the sum of two numbers */
	
	int num1 = 4;
	int num2 = 5;
	
	std::cout<< "The sum of num1 and num2 is: "<< num1 * num2<< "\n";

	return 0;

}
```

In the above example we wanted the sum of `num1` and `num2` but we by mistakenly multiplied them and because of this, we didn't get the desired output.

#                                                                                             C++ Syntax and fundamentals
---

# How to compile code

for compiling your code, type the following in your terminal.

```
// If your code file is in your current working directory:-

g++ file_name.cpp -o executable_name

./executable_name

// If your code file is in different directory:-

g++ path_to_the_file -o executable_name

./executable_name
```
---
# std::cout<< 

## Hello world!

To print a statement in C++, we use `std::cout<<` function inside the main function after including the `iostream` library.  This function is used to print an object.

```cpp
#include <iostream>

int main() {

	std::cout<< "Hello World!\n";
	
	return 0;
}
```

`The name of "" symbol is double quotes and ; is semi colon.`

When printing words we have to enclose them in `""`, this is the syntax for printing a word through the `std::cout` statement. Everything enclosed in `""` will be printed as it is.

We must write `return 0;` at the last of our code so that we can tell our OS that code ran without errors.

**note**:- After finishing every line of code using `;` semicolon is necessary to tell the compiler that this line is finished.

---

# What is \n ?

`\n` stands for escape sequence that moves the cursor or text to the next line. In this syntax `\` is a escape character and it is used to give certain character special meaning inside a string.

**note**:- `std::cout<<` function in C++ does not add `\n` by default and have to be specified by the programmer.

---

# Single and multi line comments

### Why to use comments?

Comments are used to write text in the code, it is mainly used to explain and describe a specific code block. 

```c++
// This is a single line comment
```

**note**:- A single line comment is best used to give a quick one line summary of a specific code.

```c++
/* 
*this is a multi line comment
*/
```

unlike single line comment, multi line comments are enclosed between a special sequence `/*` .

**note**:- Multi line comments are best used to describe a long summary, function, specify instruction or add long notes in the code file.

---

# Data types

Data types define's what kind of information a piece of data represents.

**There are mainly four types of data types:-**

1. Integer :- every non decimal number. It can be negative, positive and zero.
2. Float :- every decimal number. It can be negative, positive and zero. It can even be 1.0, 0.0, 5.0, -9.0 and etc.
3. string/char:- It is a sequence of alphabets or characters enclosed in quotes(""). example:- "Hello World!"
4. Boolean:- They are true and false value.

---
# Variable 

Variable's in C++ are the same as variable's in maths. Variable can be visualised as an empty box where you can store the same type of object. 

### Rules for creating a variable 

There are some rules to create a variable in C++.

- Variable name can only start from alphabets and `_`
- Variable name can not contain whitespace  and special characters except `_`
- Variable name cannot be a keyword
- Data type of that data type must be defined first.

```c++
int num = 3;
```

---

# std::cin>> 

By using `std::cin>>` function we can ask the user for their input and store it in a variable.

```cpp
//syntax

#include <iostream>
#include <string> // this library allow us to work on strings.

int main() {
	
	std::string name; // the std::string is a type used to create string type variable.
	
	std::cout<< "Enter your name: ";
	std::getline(std::cin, name); //std::getline takes the whole input line including whitespaces.

	return 0;
	
}
```

```cpp
// another example

#include <iostream>

int main() {

	int num_1;
	
	std::cout<< "Enter a number: ";
	std::cin>> num_1; // this stores user int input into num_1.
	
	return 0;

}

```

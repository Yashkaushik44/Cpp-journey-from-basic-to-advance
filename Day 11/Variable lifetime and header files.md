
#                                                                                          Variable lifetime and header files

---

# Variable lifetime

Lifetime of a variable is the period of time during the execution of a program in which the variable exists in memory and can be used safely.

A variable is created at some point, used, and then destroyed. The time between creation and destruction is its lifetime.

```cpp
//this is the syntax for the lifetime of a variable. We are using <> for getting your input in it and it is not a syntax.

#include <iostream>

int main() {

	<data_type> <variable_name> = <value>; //the lifetime of this variable starts here

	{

		<data_type> <variable_name> = <value>; //the lifetime of this variable starts here

	} //the lifetime of the inner variable ends here

	return 0;

} //the lifetime of the outer variable ends here
```

**Note:-** Scope, lifetime and storage duration are not the same thing. Scope is the part of the code where the name of a variable can be used. Lifetime is the part of the program's execution where the variable exists.

example:-

```cpp
#include <iostream>

int main() {

	int num1 = 10; //num1 is created here

	{

		int num2 = 20; //num2 is created here

		std::cout<< num2 << "\n";

	} //num2 is destroyed here

	std::cout<< num1 << "\n";

	return 0;

} //num1 is destroyed here
```

output:-

```
20
10
```

---

# Storage duration

Storage duration decides how long the memory of a variable stays alive. It tells us when the storage of a variable is created and when it is released.

The lifetime of a variable depends on its storage duration.

**They are of 3 types:-**

- Automatic storage duration
- Static storage duration
- Dynamic storage duration

---

# Automatic storage duration

Variables declared inside a function or a block without the `static` keyword have automatic storage duration. They are created when the program reaches their declaration and are destroyed automatically when the block ends.

Normal local variables are of this type.

example:-

```cpp
#include <iostream>

void show() {

	int num1 = 5; //num1 is created every time the function is called

	num1++;

	std::cout<< num1 << "\n";

} //num1 is destroyed every time the function ends

int main() {

	show();

	show();

	return 0;

}
```

output:-

```
6
6
```

---

# Static storage duration

Variables with static storage duration are created when the program starts and are destroyed when the program ends.

Global variables and variables declared with the `static` keyword have static storage duration.

When we use `static` on a local variable, it is initialized only one time and it keeps its value between function calls.

**Note:-** A static local variable can only be used inside its own function (scope) but it lives till the end of the program (lifetime).

example:-

```cpp
#include <iostream>

void counter() {

	int autoCount = 0; //automatic storage duration, it is created again every time

	static int staticCount = 0; //static storage duration, it is initialized only one time

	autoCount++;

	staticCount++;

	std::cout<< "autoCount: " << autoCount << ", staticCount: " << staticCount << "\n";

}

int main() {

	counter();

	counter();

	counter();

	return 0;

}
```

output:-

```
autoCount: 1, staticCount: 1
autoCount: 1, staticCount: 2
autoCount: 1, staticCount: 3
```

---

# Dynamic storage duration

Variables with dynamic storage duration are created and destroyed manually by the programmer. We use `new` to create them and `delete` to destroy them.

```cpp
//this is the syntax for using dynamic storage duration. We are using <> for getting your input in it and it is not a syntax.

#include <iostream>

int main() {

	<data_type>* <pointer_name> = new <data_type>(<value>); //lifetime starts here

	<code_block>

	delete <pointer_name>; //lifetime ends here

	return 0;

}
```

**Warning:-** If we forget to use `delete`, the memory will not be released until the program ends. This is called a memory leak.

example:-

```cpp
#include <iostream>

int main() {

	int* num1 = new int(25); //creates an int in the memory and stores its address in num1

	std::cout<< *num1 << "\n";

	delete num1; //destroys the int, the memory is released

	return 0;

}
```

output:-

```
25
```

---

# Header files and multiple source files

---

# Header files

A header file is a file that contains declarations which can be shared with multiple source files. It usually has the extension `.h` or `.hpp`.

A source file has the extension `.cpp` and it contains the definitions (the actual code) of the functions.

Declaration only tells the compiler that something exists. Definition gives the actual body of it.

```cpp
//this is the syntax for declaration and definition. We are using <> for getting your input in it and it is not a syntax.

<return_type> <function_name>(<parameters>); //declaration, goes in the header file

<return_type> <function_name>(<parameters>) { //definition, goes in the source file

	<code_block>

}
```

---

# Include directive

We use `#include` to copy the content of a file into the current file before compilation.

- `#include <file>` is used for standard library headers.
- `#include "file"` is used for our own header files.

---

# Include guards

If a header file gets included more than one time in the same source file, the compiler gives a redefinition error. To avoid this, we use include guards.

```cpp
//this is the syntax for using include guards. We are using <> for getting your input in it and it is not a syntax.

#ifndef <HEADER_NAME_H>
#define <HEADER_NAME_H>

<declarations>

#endif
```

We can also use `#pragma once` at the top of the header file, it does the same work.

---

# Multiple source files

We use multiple source files to divide a big program into small parts. Each `.cpp` file is compiled separately and then they are linked together to make one executable.

example:-

**math_utils.h:-**

```cpp
#ifndef MATH_UTILS_H
#define MATH_UTILS_H

int add(int a, int b); //declaration

#endif
```

**math_utils.cpp:-**

```cpp
#include "math_utils.h"

int add(int a, int b) { //definition

	return a + b;

}
```

**main.cpp:-**

```cpp
#include <iostream>
#include "math_utils.h" //this gives main.cpp the declaration of add

int main() {

	std::cout<< add(3, 4) << "\n";

	return 0;

}
```

For compiling all the files together we use:-

```
g++ main.cpp math_utils.cpp -o program
```

To run the program:-

```
./program
```

output:-

```
7
```

**Note:-** We only give `.cpp` files to the compiler. Header files are not compiled by themselves, they get copied into the source files by `#include`.
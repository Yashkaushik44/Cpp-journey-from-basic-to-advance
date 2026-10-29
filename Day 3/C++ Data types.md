

#                                                                                                   C++ Data types
---

# Constant variables

In C++, we use `const` function for declaring a constant variable.
When a variable is declared constant it's value can not change throughout the program.

```cpp
#include <iostream>

int main() {

	const <data_type> <variable_name> = <value>; // the value in this function will remain constant throughout the program

	return 0;
	
}
```

==🔴**Warning :-** This above code is the syntax for using const variable in C++. I used `<> `to enter the input and these symbols should not be considered as syntax.==

---

# Range of data types

- `bool`: `false` (0) or `true` (1).
    
- `char`: `-128 to 127` or `0 to 255`, depending on implementation.
    
- `signed char`: `-128 to 127`.
    
- `unsigned char`: `0 to 255`.
    
- `short int`: `-32,768 to 32,767`.
    
- `unsigned short int`: `0 to 65,535`.
    
- `int`: `-2,147,483,648 to 2,147,483,647`.
    
- `unsigned int`: `0 to 4,294,967,295`.
    
- `long int`: At least `-2,147,483,647 to 2,147,483,647`; commonly 64-bit on Linux.
    
- `unsigned long int`: At least `0 to 4,294,967,295`; commonly 64-bit on 64-bit Linux.
    
- `long long int`: `-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807`.
    
- `unsigned long long int`: `0 to 18,446,744,073,709,551,615`.
    
- `float`: Approximately `±3.4 × 10³⁸` (about 6–7 significant decimal digits).
    
- `double`: Approximately `±1.7 × 10³⁰⁸` (about 15–16 significant decimal digits).
    
- `long double`: Implementation-dependent; commonly the same range as `double` or a wider range.


**Note:-** Using a data type with more range gives your code more flexibility and range but it comes with the price of more memory usage, lower cache efficiency, slower performance, increased storage space. So, it is the best thing that we choose the data type which fits the task best.

---

# Unsigned int and signed int data types

`signed int` stores both negative and positive value including zero while, `unsigned int `stores only whole number and non negative numbers in them.

---

# Sizeof operator 

The size of operator is a very useful operator which gives the size of a variable or data types in bytes.

```cpp
#include <iostream>

int main() {

	int num1 = 10;
	
	std::cout<< sizeof(num1); //output: 4 (bytes)

	return 0;
	
}
```


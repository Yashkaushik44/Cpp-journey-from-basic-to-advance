
#                                                                                                Inline functions, Recursion and Scope in C++

---

# Inline functions

An inline function is a function that is declared using the `inline` keyword. It is a request to the compiler to replace the function call with the function's body, instead of doing a normal function call.

- Syntax
    
    ```cpp
    inline <return_type> <function_name>(<parameters>) {
    	// function body
    }
    ```
    
- Example example:-
    
    ```cpp
    #include <iostream>
    
    inline int square(int num) { // inline keyword is written before the return type
    	return num * num;
    }
    
    int main() {
    	
    	std::cout << square(5) << std::endl; // the compiler may replace this call with 5 * 5
    	
    	return 0;
    	
    }
    ```
    
    output:-
    
    ```
    25
    ```
    
- Role of the `inline` keyword The `inline` keyword is only a request to the compiler, not a command. The compiler can ignore it, and it can also inline functions on its own even when the keyword is not used.
    
- Advantages
    
    - Can avoid the overhead of a normal function call (jumping to the function and coming back).
    - Useful for small functions which are called many times.
- Limitations
    
    - Can increase the size of the program if a big function is inlined at many places.
    - Not suitable for big functions, or functions with loops or recursion.
    - The compiler decides in the end whether the function is actually inlined or not.
- Important points
    
    - Use inline functions only for small and simple functions.
    - An inline function must be defined in every file where it is used, so it is usually written in a header file.

# Recursion

Recursion is when a function calls itself. It is used to solve a big problem by breaking it into smaller problems of the same kind.

A recursive function has two parts:

- Base case The condition where the function stops calling itself and returns a value directly. Without it the function will keep calling itself forever.
    
- Recursive case The part where the function calls itself with a smaller (simpler) input, so that it moves closer to the base case.
    
- Example (factorial) example:-
    
    ```cpp
    #include <iostream>
    
    int factorial(int num) {
    	
    	if (num == 0) { // base case
    		return 1;
    	}
    	
    	return num * factorial(num - 1); // recursive case
    	
    }
    
    int main() {
    	
    	std::cout << factorial(4) << std::endl;
    	
    	return 0;
    	
    }
    ```
    
    output:-
    
    ```
    24
    ```
    
- How it works Each call waits for the next call to give its result. When the base case is reached, the results start coming back one by one.
    
    ```
    factorial(4) = 4 * factorial(3)
    factorial(3) = 3 * factorial(2)
    factorial(2) = 2 * factorial(1)
    factorial(1) = 1 * factorial(0)
    factorial(0) = 1  // base case
    ```
    
    So the final result is 4 * 3 * 2 * 1 * 1 = 24.
    
- Example (countdown) example:-
    
    ```cpp
    #include <iostream>
    
    void countdown(int num) {
    	
    	if (num == 0) { // base case
    		std::cout << "Done" << std::endl;
    		return;
    	}
    	
    	std::cout << num << std::endl;
    	countdown(num - 1); // recursive case
    	
    }
    
    int main() {
    	
    	countdown(3);
    	
    	return 0;
    	
    }
    ```
    
    output:-
    
    ```
    3
    2
    1
    Done
    ```
    
- Advantages
    
    - Code is shorter and cleaner for problems that can be broken into smaller similar problems.
- Limitations
    
    - Uses more memory because every function call is stored in memory until it returns.
    - Can be slower than a loop because of the repeated function calls.
    - If the base case is missing or never reached, the program will crash (stack overflow).
- Important points
    
    - Always write the base case first.
    - Make sure every recursive call moves closer to the base case.

# Scope: Local and Global Variables

Scope means the part of the program where a variable can be accessed.

- Local variables A local variable is declared inside a function (or a block `{ }`). It can be used only inside that function (or block). It is created when the function starts and destroyed when the function ends. example:-
    
    ```cpp
    #include <iostream>
    
    void show() {
    	
    	int num = 10; // local variable
    	std::cout << num << std::endl;
    	
    }
    
    int main() {
    	
    	show();
    	// std::cout << num; // error: num is not accessible here
    	
    	return 0;
    	
    }
    ```
    
    output:-
    
    ```
    10
    ```
    
- Global variables A global variable is declared outside all functions. It can be used by every function written after its declaration. It is created when the program starts and exists until the program ends. example:-
    
    ```cpp
    #include <iostream>
    
    int num = 20; // global variable
    
    void show() {
    	std::cout << num << std::endl;
    }
    
    int main() {
    	
    	show();
    	std::cout << num << std::endl;
    	
    	return 0;
    	
    }
    ```
    
    output:-
    
    ```
    20
    20
    ```
    
- Difference between local and global variables
    
    |Local variable|Global variable|
    |---|---|
    |Declared inside a function or block|Declared outside all functions|
    |Accessible only inside that function or block|Accessible in all functions after its declaration|
    |Destroyed when the function or block ends|Exists until the program ends|
    
- Shadowing If a local variable has the same name as a global variable, the local variable is used inside that function. This is called shadowing. To access the global variable, use the scope resolution operator `::`. example:-
    
    ```cpp
    #include <iostream>
    
    int num = 20; // global variable
    
    int main() {
    	
    	int num = 10; // local variable, hides the global variable
    	
    	std::cout << num << std::endl; // prints the local num
    	std::cout << ::num << std::endl; // prints the global num
    	
    	return 0;
    	
    }
    ```
    
    output:-
    
    ```
    10
    20
    ```
    
- Important points
    
    - Prefer local variables, because global variables can be changed from anywhere in the program which makes bugs harder to find.
    - Local variables are not initialized automatically, so always give them a value.
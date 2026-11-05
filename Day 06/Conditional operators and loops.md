
#                                                                                                        C++ Control flow and loops

---

# Conditional operator `?:`

## What is the conditional operator?

The conditional operator `?:` is an operator that chooses one of two values depending on a condition. It is also called the ternary operator because it works on three parts.

### Why to use it?

It is used when we want to pick one of two values in a single line, instead of writing a full `if-else` statement.

### Syntax

```cpp
// syntax

condition ? true_expression : false_expression;
```

- `condition` -> this is checked first. It gives `true` or `false`.
- `true_expression` -> this value is used when the condition is `true`.
- `false_expression` -> this value is used when the condition is `false`.

```cpp
#include <iostream>

int main() {

	int num1 = 10;
	int num2 = 20;

	int bigger = (num1 > num2) ? num1 : num2; // if num1 > num2 is true, bigger = num1, otherwise bigger = num2

	std::cout<< "The bigger number is: "<< bigger<< "\n"; // output: The bigger number is: 20

	return 0;

}
```

### Difference between `?:` and `if-else`

- `?:` is an operator and it makes an expression, so it produces a value that we can store in a variable or print directly.
- `if-else` is a statement, it only decides which block of code runs and does not produce a value by itself.

```cpp
#include <iostream>

int main() {

	int num1 = 10;
	int num2 = 20;
	int bigger;

	// using if-else
	if (num1 > num2) {
		bigger = num1;
	} else {
		bigger = num2;
	}

	std::cout<< bigger<< "\n"; // output: 20

	return 0;

}
```

**Note:-** Use `?:` only for small and simple choices, for bigger logic `if-else` is easier to read.

---

# Introduction to loops

## What are loops?

Loops are used to run a block of code again and again as long as a condition is `true`.

### Why to use loops?

Suppose we want to print `Hello` 5 times. Without a loop we have to write the same line 5 times.

```cpp
#include <iostream>

int main() {

	std::cout<< "Hello\n";
	std::cout<< "Hello\n";
	std::cout<< "Hello\n";
	std::cout<< "Hello\n";
	std::cout<< "Hello\n";

	return 0;

}
```

With a loop we write the code once and the loop repeats it for us. This reduces repetitive code and if we want to print 1000 times we only change a number.

```cpp
#include <iostream>

int main() {

	for (int i = 0; i < 5; i++) {
		std::cout<< "Hello\n";
	}

	return 0;

}
```

### How a loop works

1. The condition is checked.
2. If the condition is `true`, the code inside the loop runs once.
3. Then the condition is checked again.
4. This continues until the condition becomes `false`, then the loop stops.

## Types of loops in C++

- `for` loop Generally used when we know how many times the loop should run.
    
- `while` loop Generally used when we do not know how many times the loop will run and it depends on a condition.
    
- `do-while` loop Generally used when the code must run at least once before the condition is checked.
    

---

# `for` loop

## What is a `for` loop?

A `for` loop repeats a block of code a fixed number of times. We use it when we already know how many times we want to repeat something, like counting.

### Syntax

```cpp
// syntax

for (initialization; condition; update) {
	// code to repeat
}
```

- `initialization` It runs only once at the start of the loop. It is used to create the counter variable, example:- `int i = 1`.
    
- `condition` It is checked before every iteration. The loop runs only when it is `true`.
    
- `update` It runs after every iteration. It is used to change the counter variable, example:- `i++`.
    

```cpp
#include <iostream>

int main() {

	for (int i = 1; i <= 5; i++) { // starts from 1, runs while i <= 5, increases i by 1 every time

		std::cout<< i<< "\n";

	}

	return 0;

}
```

Output:-

```
1
2
3
4
5
```

### How it executes step by step

1. `int i = 1` runs once.
2. `i <= 5` is checked, it is `true` so the code inside runs and prints `1`.
3. `i++` runs and `i` becomes `2`.
4. `i <= 5` is checked again, and the same steps repeat.
5. When `i` becomes `6`, `i <= 5` is `false` and the loop stops.

**Note:-** A variable created in the initialization part (like `i`) can only be used inside the `for` loop.

---

# `while` loop

## What is a `while` loop?

A `while` loop repeats a block of code as long as its condition is `true`. We use it when we do not know in advance how many times the loop will run.

### Syntax

```cpp
// syntax

while (condition) {
	// code to repeat
}
```

The condition is checked **before** every iteration. If it is `true` the code inside runs, if it is `false` the loop is skipped.

```cpp
#include <iostream>

int main() {

	int i = 1; // the counter is created outside the loop

	while (i <= 5) { // loop runs while i is less than or equal to 5

		std::cout<< i<< "\n";
		i++; // this changes i so that the condition will become false at some point

	}

	return 0;

}
```

Output:-

```
1
2
3
4
5
```

When `i` becomes `6`, the condition `i <= 5` becomes `false`, the loop stops and the program moves to the next line after the loop.

### Infinite loop

If the condition never becomes `false`, the loop will never stop. This is called an infinite loop.

```cpp
#include <iostream>

int main() {

	int i = 1;

	while (i <= 5) {

		std::cout<< i<< "\n";
		// i++ is missing, so i is always 1 and the condition is always true

	}

	return 0;

}
```

**Warning :-** Always make sure something inside the `while` loop changes the condition variable, otherwise the loop will run forever. Press `Ctrl + C` in the terminal to stop it.

---

# `do-while` loop

## What is a `do-while` loop?

A `do-while` loop is similar to a `while` loop but it checks the condition **after** running the code. We use it when the code must run at least once, like showing a menu or asking input.

### Syntax

```cpp
// syntax

do {
	// code to repeat
} while (condition);
```

```cpp
#include <iostream>

int main() {

	int num = 10;

	do {

		std::cout<< "This runs once\n"; // runs first, then the condition is checked

	} while (num < 5); // 10 < 5 is false, so the loop stops after one run

	return 0;

}
```

Output:-

```
This runs once
```

### Difference between `while` and `do-while`

- In `while`, the condition is checked first. If it is `false` in the beginning, the code never runs.
- In `do-while`, the code runs first and then the condition is checked. So, the code always runs **at least once**.

If we use the same example with a `while` loop, nothing will be printed because `10 < 5` is `false` from the start.

**Note:-** A semicolon `;` is necessary after the `while (condition)` in a `do-while` loop. Forgetting it gives a compilation error.

---

# `break`, `continue` and `return`

These are jump statements, they change the normal flow of the code.

## `break`

`break` immediately stops the loop that it is inside and the program continues from the line after that loop. We use it when we want to stop a loop early.

```cpp
#include <iostream>

int main() {

	for (int i = 1; i <= 10; i++) {

		if (i == 5) {
			break; // when i is 5, the loop is terminated completely
		}

		std::cout<< i<< "\n";

	}

	return 0;

}
```

Output:-

```
1
2
3
4
```

## `continue`

`continue` skips the rest of the current iteration and moves to the next iteration of the loop. We use it when we want to skip some values but keep the loop running.

```cpp
#include <iostream>

int main() {

	for (int i = 1; i <= 5; i++) {

		if (i == 3) {
			continue; // skips the printing for i = 3 and goes to the next iteration
		}

		std::cout<< i<< "\n";

	}

	return 0;

}
```

Output:-

```
1
2
4
5
```

**Note:-** In a `for` loop, `continue` still runs the update part (`i++`) before the next iteration. In a `while` loop, make sure the update statement is not skipped by `continue`, otherwise the loop can become infinite.

## `return`

`return` exits the current function immediately. If the function has a return type, `return` also sends a value back to the place where the function was called. In `main()`, `return 0;` ends the program.

```cpp
#include <iostream>

int add(int a, int b) {

	return a + b; // exits the function and sends the sum back

}

int main() {

	int result = add(3, 4); // result stores the returned value 7

	std::cout<< result<< "\n"; // output: 7

	return 0;

}
```

`return` can also be used inside a loop, then it exits the whole function and not just the loop.

```cpp
#include <iostream>

int main() {

	for (int i = 1; i <= 10; i++) {

		if (i == 3) {
			return 0; // exits main(), so the program ends here
		}

		std::cout<< i<< "\n";

	}

	std::cout<< "This line will never run\n";

	return 0;

}
```

Output:-

```
1
2
```

### Difference between `break`, `continue` and `return`

- `break` -> stops the loop and the code after the loop runs.
- `continue` -> skips only the current iteration and the loop keeps running.
- `return` -> exits the whole function, the loop and any code after it inside that function will not run.

#                                                                                                Arrays in C++ - I
---
# What are arrays?

Arrays are a fixed size list that stores multiple items of the exact same data type in one continuous row.

---

# Declaring, initialising arrays and null terminator

```cpp
// Below is the syntax of arrays in c++. I used <insert> for insertion and it should not be treated as a syntax.

#include <iostream>

int main() {

	<data_type> <array_name>[<size_of_array>] = {<insert_data>};
	
	return 0;
	
}
```

Arrays data are always enclosed withing curly brackets.

```cpp
// example:-

#include <iostream>

int main() {

	int numbers[4] = {1,2,3,4};

	return 0;
	
}
```

---

# Null terminator

`\0` is a default invisible character automatically placed at the end of a character type array to tell the program that the text ends here.

---
# Modify and access an index in arrays

We can access a value through and index and can modify it with the same.

```cpp
// Below is the syntax of modifying and accessing indexes in arrays in c++. I used <insert> for insertion and it should not be treated as a syntax.

#include <iostream>

int main() {

	<data_type> <array_name>[<size_of_array>] = {<insert_data>};
	
	<variable> = <array_name>[<index_no>]; // storing the value of the array on the specific index into the variable. This is accessing.
	
	<array_name>[<index_no.>] = <new_value>; // this will replace the value on that specific value with the new value
	
	return 0;
	
}

```

```cpp
// example

#include <iostream>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    // Accessing an element (index starts at 0)
    std::cout << "Original value at index 2: " << numbers[2] << "\n";

    // Modifying an element
    numbers[2] = 99;

    // Accessing the modified element
    std::cout << "Modified value at index 2: " << numbers[2] << "\n";

    return 0;
    
}
```

---

# Printing an array in C++ and size of an array

In C++, if you try to directly print an array you will get the memory location of that array rather then the values.
So, we need to use for loop to access and print every element in the array.

```cpp
// Below is the syntax of printing the elements of an array in c++. I used <insert> for insertion and it should not be treated as a syntax.

#include <iostream>

int main() {

	<data_type> <array_name>[<size_of_array>] = {<insert_data>};
	
	size_of_array = sizeof(<array_name>) / sizeof(<array_name>[0]); // this gets the size of an array
	
	for(int num = 0; num < size_of_array; num++) {
	
		std::cout<< num<< ", "; // this prints all the values of array one at a time seprated by ,
		
	}
	
	return 0;
	
}
```

Note: The above syntax is good for learning the logic but you can write a more cleaner code by using `:` operator. It means `in`.

```cpp
//example

#include <iostream>

int main() {

    int numbers[5] = {10, 20, 30, 40, 50};

    // "For each 'num' in 'numbers'"
    for (int num : numbers) {
    
        std::cout<< num<< ", ";
        
    }
    
    return 0;
}

```


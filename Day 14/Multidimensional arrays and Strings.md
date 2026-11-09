
#                                                                                                               Multidimensional arrays and Strings
---

# Multi Dimensional arrays

A multidimensional array is a data structure that organises elements across multiple axes in rows and columns.
Multidimensional arrays are of 3 types:- 

- 2D Array(Matrix)
	Stores data across two axes using row and column indices.`(arr[row][col])`
	
- 3D Array(Volume)
	Adds a third depth axis to grid using three indices. `(arr[depth][row][col])`
	
- N- Dimensional Array(Tensor)
	Extends to four or more spatial or logical axes. `(arr[i][j][k][l]...)`

---

# Character arrays and C-style strings

**Character array** - It is a sequential collection of `char` data types elements is memory. 

**C-Style string** - It is a character array terminated by a null character (`\0`) to mark the end of the text.

---

# std:: string

It is a class used to create string in C++ replacing the C-style strings. It is used best to define a string. It also tracks its own length and cleans up its memory when you're done. To use string we need to include `string`. 

```cpp
// This is the syntax of std::string in c++. I used <insert> to specify insert and it should not be treated as syntax.

#include <iostream>
#include <string>
int main() {

	std::string <variable_name> = "<string>";

	return 0;
	
}
```

```cpp
// example

#include <iostream>
#include <string>

int main() {

	std::string name = "user";
	
	std::cout<< name<< std::endl; //the endl is a endline character used to flush all the buffer value after executing this line.
	return 0;
	
}
```

---

# Common string operations

- Concatenation(+ or .append())
	It is used to join two strings together end-to-end into a single string.
	```cpp
	//example
	
	#include <iostream>
	#include <string>
	
	int main() {
		
		std::string result = std::string ("Hello ") + "World"; // output : "Hello World"
		
		return 0;
		
	}
	```
	
- Length/size(.length() or .size())
	It is used to count the total number of characters in a string.
	```cpp
	//example
	
	#include <iostream>
	#include <string>
	
	int main() {
	
		std::string word = "Code";
		
		size_t count = word.length(); //size_t is an unsigned integer to match string::size_type
		
		count = word.size();
		
		// both will give 4 as an output.
	
		return 0;
		
	}
	```

- Element Access (`[]` or `.at()`)
	Retrieves a character at a specific zero-based index.
    
    ```cpp
    //example
    
    #include <iostream>
    #include <string>
    
    int main() {
    
	    std::string word = "User";
	    
	    char first = word[0]; // output: "U"
    
	    return 0;
	    
    }
    ```
    
- Substring (`.substr()`)
	Extracts a section of the string starting at an index for a specific length.
    
	```cpp
	// example
	
	#include <iostream>
	#include <string>
	
	int main() {
	
		std::string word = "User is a student";
		
		std::string substr = word.substr(0, 4); // output: "User"
	
		return 0;
		
	}
	```
    
- Find / Search (`.find()`)
	Returns the first index where a substring appears, or `std::string::npos` if missing.
    
	```cpp
	//example
	
	#include <iostream>
	#include <string>
	
	int main() {
	
		std::string word = "User is a student";
		
		size_t pos = word.find("student"); //output: 10
	
		return 0;
		
	}
	```
    
- Comparison (`==`, `!=`, `<`, `>`)
	Compares two strings character-by-character based on ASCII values.
    
    ```cpp
    //example
    
    #include <iostream>
    #include <string>
    
    int main() {
    
	    std::string str1 = "ABC";
	    std::string str2 = "ABC";
	    
	    bool match = (str1 == str2); //return true if identical else false
    
	    return 0;
	    
    }
    ```
    
- Insertion (`.insert()`)
	Places a new string sequence at a designated index position inside the existing string.
    
    ```cpp
    // example
    
    #include <iostream>
    #include <string>
    
    int main() {
	    
	    std::string str1 = "User is a ";
	    
	    str1.insert(10, "student"); // Inserts "student into the str1 at index 10"
    
	    return 0;
	    
    }
    ```
    
- Erasure (`.erase()`)
	Removes a specified number of characters starting from a given index.
    
    ```cpp
    //example
    
    #include <iostream>
    #include <string>
    
    int main() {
    
	    std::string str = "Hello World";
	    
	    str.erase(0, 6); // output: "Hello " is removed from str
	    
	    return 0;
	    
    }
    ```
    
- Replacement (`.replace()`)
	Overwrites a section of characters starting from an index with a new string.
    
	```cpp
	//example
	
	#include <iostream>
	#include <string>
	
	int main() {
	
		std::string str = "Hello World";
		
		str.replace(0, 5, "Hi"); // replaces "Hello" with "Hi" in str variable
	
		return 0;
		
	}
	```
    
- Numeric Conversion (`std::to_string()`, `std::stoi()`)
	Converts a number into a `std::string` or parses a `std::string` into an `int`.
    
    ```cpp
    //example
    
    #include <iostream>
    #include <string>
    
    int main() {
    
	    std::string str = std::to_string(42); // convert 42 into str. "42"
	    
	    int num = std::stoi("42"); // convert the string "42" into int
    
	    return 0;
	    
    }
    ```

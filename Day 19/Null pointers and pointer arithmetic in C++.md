#                                                                   Null pointers and pointer arithmetic in C++

---

# # Null Pointers `nullptr`

Null pointers are pointers which points to nothing. 
We use `nullptr` to a pointer to clearly mark that it points to nothing yet.
It is used to prevent crashes from accidentally accessing random garbage memory.

```cpp
//example

#include <iostream>

int main() {
	
	int* ptr = nullptr;
	
	if(ptr == nullptr) {
	
		std::cout<< "Pointer is empty, safe to skip\n";
		
	}
	
	int score = 67;
	ptr = &score;
	
	if(ptr != nullptr) {
	
		std::cout<< "Score: "<< *ptr<< std::endl; //output 67
	
	}

	return 0;
	
}
```
 
Use:- It is a good practice to declare a pointer with `nullptr` and then use it afterwards, this practice creates a safety net for edge cases and protects the code.

==🔴**Warning:- Pointers and any memory influencing methods should be used with upmost safety checks because a small error can corrupt the system memory to no return. Only run a program after creating security nets for edge cases! If you are using a sandbox editor like VScode it won't impact much but in industry grade code where you work on metal it can become devastating  **== 

---

# Pointer arithmetic

Adding or subtracting from a pointer to jump forward or backward through neighbouring memory slots, such as moving through an array. 

Adding `1` to a pointer moves it forward by the byte size of its data type landing directly on the next element in contiguous memory.

```cpp
//example

#include <iostream>

int main() {

	int numbers[] = {10, 20, 30 , 40};
	int* ptr = numbers; // points to the 0 index of the array. 10 in this case
	
	ptr++; // jump forward one int (4 bytes) to the next index. 20 in this case
	
	std::cout << *(ptr + 2)<< "\n"; // peeks 2 ints ahead without moving ptr. Pointer value doesnt change but the outuput is 40.
	
	ptr--; // moves backwards 1 int. Back to index 0.
	

	return 0;
	
}
```

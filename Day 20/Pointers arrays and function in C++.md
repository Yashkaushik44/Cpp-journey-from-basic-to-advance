#                                                                                               Pointers arrays and function in C++

# Pointers and Arrays

An array stores multiple values side by side in memory, while a pointer stores a memory address. An array name is not a pointer itself, though in most expressions it automatically converts to a pointer to its first element.

- Array name and pointer :- Using `arr` in an expression gives the address of `arr[0]`, so `int* ptr = arr;` points to the first element.
    
- Pointer arithmetic :- Adding `1` to a pointer (`ptr + 1`) moves it forward to the next element in memory, not just one byte.
    
- Pointer notation vs indexing :- Array indexing `arr[i]` works the exact same way as pointer notation `*(arr + i)` or `*(ptr + i)`.
    

```
// example
#include <iostream>

int main() {
    int arr[3] = {10, 20, 30};
    int* ptr = arr; // points to the first element (10)

    std::cout << *ptr << "\n";       // output: 10
    std::cout << *(ptr + 1) << "\n"; // output: 20
    std::cout << *(arr + 2) << "\n"; // output: 30

    return 0;
}
```

# Pointers and Functions

Passing a pointer to a function sends a copy of a memory address instead of copying the actual variable. Inside the function, dereferencing that pointer lets you read or modify the original variable directly.

- Passing addresses :- Pass `&num` when calling a function that expects a pointer parameter like `int* ptr`.
    
- Modifying original values :- Using `*ptr` inside the function accesses the value at that address and updates the original variable.
    
- Arrays in functions :- Passing an array to a function passes a pointer to its first element, allowing the function to work with the original array.
    

```
// example
#include <iostream>

void updateValue(int* ptr) {
    *ptr = 50; // dereferences ptr to modify the original variable
}

void doubleFirst(int* arr) {
    *arr = *arr * 2; // modifies the first element of the original array
}

int main() {
    int num = 10;
    updateValue(&num); // passes the memory address of num
    std::cout << num << "\n"; // output: 50

    int arr[3] = {5, 15, 25};
    doubleFirst(arr); // arr converts to a pointer to arr[0]
    std::cout << arr[0] << "\n"; // output: 10

    return 0;
}
```

# References vs Pointers

Both references and pointers let you access existing variables indirectly, but they work differently and are not interchangeable.

- References (`&`) :- Acts as an alias (another name) for an existing variable. A reference must be initialized when declared, cannot be null, and cannot be changed to refer to another variable later.
    
- Pointers (`*`) :- Stores the memory address of a variable. A pointer can be reassigned to point to a different address and can be set to `nullptr` when it points to nothing.
    
- Accessing values :- A reference accesses the original variable directly like a normal variable, while a pointer needs `*` (dereferencing) to reach the value.
    

```
// example
#include <iostream>

int main() {
    int num = 10;
    int value = 20;

    int& ref = num;  // ref is an alias for num (must be initialized)
    int* ptr = &num; // ptr stores the address of num

    ref = 15; // changes num directly to 15
    std::cout << num << "\n"; // output: 15

    *ptr = 25; // dereferences ptr to change num to 25
    std::cout << num << "\n"; // output: 25

    ptr = &value; // ptr can be reassigned to point to value
    std::cout << *ptr << "\n"; // output: 20

    ptr = nullptr; // pointers can hold nullptr, references cannot

    return 0;
}
```
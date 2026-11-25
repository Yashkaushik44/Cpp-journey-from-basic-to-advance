#                                                                                               Copy assignment shallow deep copy and move constructors in C++

# Copy Assignment Operators

A copy assignment operator copies the state of one existing object to another existing object. A copy constructor initializes a new object, while a copy assignment operator updates an object that has already been created.

- Default copy assignment :- If no copy assignment operator is defined by the user, the compiler normally provides one that assigns the members individually (though it can be deleted for certain classes).
    
- User-defined copy assignment :- Using `ClassName& operator=(const ClassName& other)` lets you define how the members are copied when using `=` between existing objects. Returning `*this` by reference lets you assign multiple objects using `=`.
    
- Self-assignment :- Assigning an object to itself (`obj = obj`) should not change its state. Using `this != &other` checks whether both objects are different, which is useful when replacing dynamically allocated memory.
    

```cpp
// example
#include <iostream>

class Number {
public:
    int value;

    Number(int num) {
        value = num;
    }

    Number& operator=(const Number& other) {
        value = other.value; // copies the value from the other object
        return *this; // returns the current object
    }
};

int main() {
    Number obj1(10);
    Number obj2(20);

    obj2 = obj1; // calls the copy assignment operator
    std::cout << obj2.value << "\n"; // output: 10

    return 0;
}
```

# Shallow Copy vs Deep Copy

Both shallow copy and deep copy copy data from one object to another, but they work differently when the objects contain pointers to dynamically allocated memory.

- Shallow copy :- Copies the pointer's memory address instead of copying the data it points to, so both pointers refer to the same memory location. Changing the value through one pointer also changes the value accessed through the other pointer.
    
- Deep copy :- Creates a separate copy of the data pointed to by the original pointer, allowing both objects to work with their own data without affecting each other.
    
- Copying pointer members :- A default copy constructor copies members individually, so raw pointer members store the same address after copying. A user-defined copy constructor can allocate separate memory and copy the value instead. If both objects own the same memory, deleting it through both objects is invalid. Copy assignment must also handle owned memory correctly.
    

```cpp
// example
#include <iostream>

class Number {
public:
    int* ptr;

    Number(int num) {
        ptr = new int(num);
    }

    Number(const Number& other) {
        ptr = new int(*other.ptr); // creates a separate copy of the value
    }

    Number& operator=(const Number& other) {
        *ptr = *other.ptr; // copies the value into existing memory
        return *this;
    }

    ~Number() {
        delete ptr;
    }
};

int main() {
    Number obj1(10);
    int* ptr = obj1.ptr; // shallow copy of the pointer (same address)
    *ptr = 20;
    std::cout << *obj1.ptr << "\n"; // output: 20

    Number obj2 = obj1; // deep copy using the copy constructor
    *obj2.ptr = 30;
    std::cout << *obj1.ptr << "\n"; // output: 20
    std::cout << *obj2.ptr << "\n"; // output: 30

    return 0;
}
```

# Move Constructors

A move constructor initializes a new object from another object and can transfer its resources instead of creating separate copies of them. Move constructors were introduced in C++11.

- Rvalue references (`&&`) :- Using `ClassName(ClassName&& other)` lets a move constructor accept an rvalue of the class type. Using `std::move(obj)` from the `<utility>` header allows an existing object to be passed this way, though `std::move()` itself does not transfer any data.
    
- Transferring ownership :- Copy the memory address stored in the original object's owning pointer and set that pointer to `nullptr`, so only the new object owns the allocated memory. The original object still exists and must remain safe to destroy.
    
- Default move constructor :- The compiler can provide a move constructor that moves members individually if no copy or move operations or destructor are user-declared. Using `noexcept` on a user-defined move constructor specifies that it does not throw exceptions.
    

```cpp
// example
#include <iostream>
#include <utility>

class Number {
public:
    int* ptr;

    Number(int num) {
        ptr = new int(num);
    }

    Number(Number&& other) noexcept {
        ptr = other.ptr; // transfers the memory address
        other.ptr = nullptr; // original object no longer owns the memory
    }

    ~Number() {
        delete ptr;
    }
};

int main() {
    Number obj1(10);
    Number obj2 = std::move(obj1); // calls the move constructor

    std::cout << *obj2.ptr << "\n"; // output: 10
    std::cout << (obj1.ptr == nullptr) << "\n"; // output: 1

    return 0;
}
```

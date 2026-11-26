#                                                                         Move assignment, lvalues and rvalues in C++
---

# Move assignment operators

A move assignment operator is a special member function that overloads `operator=` to assign one existing object to another by moving its members rather than copying its resources. Unlike a move constructor, it does not initialise a new object and has to handle the resources already owned by the calling object.

The compiler can implicitly generate a move assignment operator depending on the other special member functions declared inside the class.

```cpp
//example

#include <utility>

class Box {

	int* value;

public:

	Box(int num) : value(new int(num)) {}

	~Box() {
	
		delete value;
	}

	Box& operator=(Box&& other) noexcept {
	
		if (this != &other) {
		
			delete value; // Deletes the resource owned by the current object
			value = other.value;
			other.value = nullptr; // The other object no longer owns the resource
		}
		
		return *this;
	}
};

int main() {

	Box a(10);
	Box b(20);

	a = std::move(b); // Allows the move assignment operator to be called

	return 0;
}
```

---

# Lvalues and rvalues

- Lvalues
	An lvalue is an expression that refers to an object or function with an identity, which is not being treated as an expiring value. An lvalue can also appear on the right hand side of an assignment and does not necessarily have to be modifiable.
- Rvalues
	An rvalue is an expression that either produces a value (prvalue) or refers to an object whose resources can be reused (xvalue).

```cpp
//example

#include <utility>

int main() {

	int num = 10; // num is an lvalue whereas 10 is an rvalue
	int value = num; // num is still an lvalue
	int result = num + 5; // num + 5 is an rvalue
	const int a = 20; // a is an lvalue but cannot be modified
	int b = std::move(num); // std::move(num) is an xvalue

	return 0;
}
```

---

# Lvalue and rvalue references

- Lvalue references
	An lvalue reference is declared using `&` and can be used to access and modify an existing object. A const lvalue reference can also bind to a temporary value but cannot be used to modify it.
- Rvalue references
	An rvalue reference is declared using `&&` and can bind to an rvalue. `std::move()` can be used to convert an ordinary lvalue expression into an xvalue, but it does not itself move any resources.

```cpp
//example

#include <utility>

int main() {

	int num = 10;
	int& ref = num; // Lvalue reference
	ref = 20; // Changes num's value to 20

	const int& value = 30; // Const lvalue reference
	int&& a = 40; // Rvalue reference
	int&& b = std::move(num);

	int& c = a; // a itself is an lvalue when accessed by its name

	return 0;
}
```

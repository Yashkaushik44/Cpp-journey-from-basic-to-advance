#                                                                         Object Oriented Programming - VI in C++ 
---

# Friend functions and friend classes

A friend function is a function declared using the `friend` keyword inside a class that allows the function to access the private and protected members of that class without being its member function. A friend class allows all its member functions to access those members of another class.

```cpp
//example

class BankAccount {

	double balance = 1000;

	friend double getBalance(BankAccount &account); // Friend function
	friend class Manager; // Friend class
};

double getBalance(BankAccount &account) {

	return account.balance;
}

class Manager {

public:

	void deposit(BankAccount &account, double amount) {

		account.balance += amount;

	}
};
```

---

# Operator overloading

Operator overloading allows an existing operator to perform a specific operation on objects of a class by defining a function using the `operator` keyword. A unary operator operates on one operand, while a binary operator operates on two operands.

```cpp
//example

class Number {

public:

	int value;

	Number(int v) : value(v) {}

	Number operator-() const { // Unary operator

		return Number(-value);

	}

	friend Number operator+(const Number &a, const Number &b) { // Binary operator

		return Number(a.value + b.value);

	}
};

Number a(10);
Number b(20);
Number c = a + b;
Number d = -a;
```

---

# Copy constructors

A copy constructor is a special constructor that initialises a new object using an existing object of the same class. It commonly accepts a constant reference to the existing object as its argument.

```cpp
//example

class Box {

public:

	int width;

	Box(int w) : width(w) {} // Parameterised constructor
	Box(const Box &b) : width(b.width) {} // Copy constructor
};

Box b1(10);
Box b2 = b1; // Copy construction
```

An implicitly generated copy constructor copies the base-class subobjects and non-static data members of the existing object. In the case of a raw pointer, copying its address is called shallow copying, whereas creating a separate copy of the data it points to is called deep copying.

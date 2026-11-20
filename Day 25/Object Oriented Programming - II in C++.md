#                                                                         Object Oriented Programming - II in C++ 
---

# Data Members and member functions 

Data members are variables inside a class that hold an object's state, while member functions are methods inside the class that define its behaviour and manipulate those variables.

```cpp
//example

class BankAccount {

public:

	double balance; // Data member
	
	void deposit(double amount) { 
	
		balance += amount;

	} // member function
};
```

---

# The `this` pointer 

The `this` pointer is an implicit pointer accessible inside non-static member functions that holds the memory address of the current calling object.

```cpp
//exmaple

class Player {
	
	int score;
	
public:

	void setScore(int score) {
	
		this-> score = score;
	
	}
};
```

---

# Constructors

A constructor is a special member function with the exact same name as the class and no return type that runs automatically to initialise an object when it is created.

```cpp
//example

class Server {

public:

	Server() { // Runs automatically upon object creation
	
		std::cout << "Server initialised\n";
	
	}
};
```

---

# Default and parameterised constructors 

A default constructor takes no arguments to initialise an object with baseline values, whereas a parameterised constructor accepts arguments initialise an object with specific custom values at creation.

```cpp
//example

class Box {

public:

	int width;
	
	Box() : width(10) {} // Default constructor
	Box(int w) : width(w) {} //Parameterised constructor
	
};
```


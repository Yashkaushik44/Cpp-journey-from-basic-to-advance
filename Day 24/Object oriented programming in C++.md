#                                                                           Object oriented programming in C++
---

# Introduction 

OOP is used to organise code around the real world entities called "objects" rather than just functions logic. It bundles related data and behaviours together so your programs are easier to manage, reuse and scale.

```cpp
//example

#include <iostream>
#include <string>

class Car {

public:

	std::string brand = "Toyota";
	
	void drive() {
	
		<code block>
	
	}
};
```

---

# Classes and objects

A class is a blueprint that defines properties (variables) and actions (functions), while an object is the actual working item built from that blueprint. You create one class, and from it, you can generate as many independent objects as you need.

```cpp
//example

#include <iostream>
#include <string>

class Car {

public:

	std::string color;
	
	void honk() {std::cout<< "Beep!";}

};

int main() {

	Car myCar;
	
	myCar.color = "Red";
	
	myCar.honk();

}
```

---

# Access Specifies 

Access specifiers act like security locks controlling who can view or modify data inside a class. 
There are different type of access specifiers.

## `public` 

Functions and variables that are declared under `public` access specifier is open to everyone.

```cpp
//example

#include <iostream>
#include <string>

class CarColour {

public:

	std::string colour;
	
	void showColour() {
	
		std::cout<< colour;
	
	}
};
```

## `private`

Functions and variables that are declared under `private` access specifier is locked strictly inside the class itself.

```cpp
//example 

#include <iostream>
#include <string>

class BankAccount {

private: 

	double balance = 500; // it is locked and only BankAccount functions can touch this

};
```

## `protected`

Functions and variables declared under this access specifier are accessible only to the class and its child classes (inheritance).

```cpp
//example

#include <iostream>
#include <string>

class BankAccount {

protected:

	int accountID = 101; // it is semi locked and only be accessable to BankAccount and inheritance classes

};
```
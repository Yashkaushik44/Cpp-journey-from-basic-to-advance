#                                                                         Object Oriented Programming - IV in C++
---

# Encapsulation

Encapsulation is the OOP principle of keeping data members and the functions that operate on them together inside a class, with a controlled public interface for using them.

```cpp
//example

#include <iostream>

class BankAccount {

private:

	double balance = 0;

public:

	void deposit(double amount) {

		if (amount > 0) balance += amount;
	}

	double getBalance() const {

		return balance;
	}
};

int main() {

	BankAccount account;
	account.deposit(250);
	std::cout << account.getBalance() << '\n';
}
```

Output:

```text
250
```

Encapsulation makes a class easier to maintain because callers use its public operations instead of depending on how its data is stored.

---

# Data Hiding vs Encapsulation

Data hiding restricts direct access to implementation details, while encapsulation groups related state and behaviour behind an interface. Data hiding supports encapsulation, but the two terms do not mean exactly the same thing.

A public balance could be changed to an invalid value such as `-500` from outside the class. Making it private and providing a validated `deposit()` operation prevents that particular invalid update.

```cpp
//example of unrestricted public access

#include <iostream>

class Wallet {

public:

	int balance = 100;
};

int main() {

	Wallet wallet;
	wallet.balance = -500; // Allowed, but invalid for this example
	std::cout << wallet.balance << '\n';
}
```

Output:

```text
-500
```

---

# Access Specifiers in Encapsulation

`public` members are accessible through an object, `private` members are accessible by the class's own member functions and friends, and `protected` members are also accessible to derived classes under the usual access rules.

```cpp
//example

#include <iostream>

class Device {

private:

	int serialNumber = 42;

protected:

	bool connected = true;

public:

	void showSerial() const {

		std::cout << serialNumber << '\n';
	}
};

class Phone : public Device {

public:

	void showConnection() const {

		std::cout << connected << '\n';
	}
};

int main() {

	Phone phone;
	phone.showSerial();
	phone.showConnection();
}
```

Output:

```text
42
1
```

A derived class cannot directly access `serialNumber` because it is private in `Device`.

---

# Getters, Setters and Validation

A getter reads an object's state, while a setter changes it through a controlled operation. Validation inside a setter can reject values that would make the object's state invalid.

```cpp
//example

#include <iostream>

class Student {

private:

	int marks = 0;

public:

	void setMarks(int value) {

		if (value >= 0 && value <= 100) marks = value;
	}

	int getMarks() const {

		return marks;
	}
};

int main() {

	Student student;
	student.setMarks(85);
	student.setMarks(150); // Invalid value is ignored
	std::cout << student.getMarks() << '\n';
}
```

Output:

```text
85
```

`const` after `getMarks()` means the member function cannot modify the object's non-`mutable` data members through `this`. A getter or setter is optional: expose an operation only when the class actually needs it.

---

# Maintaining Valid Object State

A class should keep its own rules valid from construction onward. A setter alone cannot protect an object if its constructor or another member function introduces invalid data.

```cpp
//example

#include <iostream>

class Temperature {

private:

	int celsius;

public:

	Temperature(int value) : celsius(value >= -273 ? value : -273) {}

	void setCelsius(int value) {

		if (value >= -273) celsius = value;
	}

	int getCelsius() const {

		return celsius;
	}
};

int main() {

	Temperature temperature(-300);
	temperature.setCelsius(20);
	std::cout << temperature.getCelsius() << '\n';
}
```

Output:

```text
20
```

Common mistakes include exposing all data publicly, adding setters that allow invalid changes, and automatically writing getters and setters for every private member. Private members alone do not guarantee a good class design.

---

# Abstraction

Abstraction means showing the essential operations an object provides while keeping unnecessary implementation details out of the code that uses it.

```cpp
//example

#include <iostream>

class Printer {

private:

	void warmUp() const {

		std::cout << "Printer ready\n";
	}

public:

	void printDocument() const {

		warmUp();
		std::cout << "Document printed\n";
	}
};

int main() {

	Printer printer;
	printer.printDocument();
}
```

Output:

```text
Printer ready
Document printed
```

The caller needs to know what `printDocument()` does, not how the printer prepares itself.

---

# Abstraction vs Encapsulation

Abstraction focuses on which operations the user sees; encapsulation focuses on organizing data and behaviour within a class and controlling access to them.

An ordinary class with a clear public interface can provide abstraction. An abstract class is one way to define an interface, but abstraction does not require an abstract class.

---

# Abstract Classes and Pure Virtual Functions

An abstract class has at least one pure virtual function, either declared directly or inherited without a final overrider. A pure virtual function uses `virtual` and `= 0`, and defines a function that a concrete derived class must implement.

```cpp
//example

#include <iostream>

class Shape {

public:

	virtual double area() const = 0; // Pure virtual function
	virtual ~Shape() = default; // Safe polymorphic base destructor
};

class Rectangle : public Shape {

private:

	double width;
	double height;

public:

	Rectangle(double w, double h) : width(w), height(h) {}

	double area() const override {

		return width * height;
	}
};

int main() {

	Rectangle rectangle(4, 5);
	Shape& shape = rectangle;
	std::cout << shape.area() << '\n';
}
```

Output:

```text
20
```

`Shape` cannot be instantiated directly, but a reference or pointer to `Shape` can refer to a `Rectangle`. `override` asks the compiler to verify that the derived function really overrides a virtual base function.

---

# Members of an Abstract Class

An abstract class can also contain data members, constructors, ordinary member functions, and virtual functions that are not pure virtual. Not every function inside an abstract class must use `= 0`.

```cpp
//example

#include <iostream>

class Employee {

protected:

	int id;

public:

	Employee(int value) : id(value) {}

	void showId() const {

		std::cout << "ID: " << id << '\n';
	}

	virtual void work() const = 0;
	virtual ~Employee() = default;
};

class Developer : public Employee {

public:

	Developer(int value) : Employee(value) {}

	void work() const override {

		std::cout << "Writing code\n";
	}
};

int main() {

	Developer developer(7);
	developer.showId();
	developer.work();
}
```

Output:

```text
ID: 7
Writing code
```

Common mistakes include trying to instantiate an abstract class, forgetting to implement an inherited pure virtual function, and giving a derived override the wrong `const` or parameter signature. A base class intended for polymorphic deletion should have a public virtual destructor.

---

# Inheritance

Inheritance allows a derived class to reuse and extend the members of a base class. With public inheritance, a derived object generally represents an `is-a` kind of its base class.

```cpp
//example

#include <iostream>

class Animal {

public:

	void eat() const {

		std::cout << "Eating\n";
	}
};

class Dog : public Animal {

public:

	void bark() const {

		std::cout << "Barking\n";
	}
};

int main() {

	Dog dog;
	dog.eat(); // Inherited function
	dog.bark();
}
```

Output:

```text
Eating
Barking
```

`Animal` is the base (parent) class and `Dog` is the derived (child) class. Public inheritance is appropriate here because a dog is an animal.

---

# Inheritance Access Modes

The keyword after `:` controls how inherited public and protected members are exposed through the derived class; it does not change the original access specifiers in the base class.

- `public` inheritance keeps inherited public members public and protected members protected.
- `protected` inheritance makes inherited public and protected members protected.
- `private` inheritance makes inherited public and protected members private.

Base-class private members remain part of the base subobject but cannot be accessed directly by ordinary derived-class member functions, regardless of inheritance mode.

```cpp
//example

#include <iostream>

class Account {

private:

	int pin = 1234;

protected:

	int balance = 500;

public:

	void showBalance() const {

		std::cout << balance << '\n';
	}
};

class Savings : public Account {

public:

	void showProtectedBalance() const {

		std::cout << balance << '\n';
	}
};

int main() {

	Savings savings;
	savings.showBalance();
	savings.showProtectedBalance();
}
```

Output:

```text
500
500
```

`Savings` cannot read `pin` directly. It can use the inherited public function `showBalance()` because the inheritance mode is public.

---

# Protected and Private Inheritance

Protected and private inheritance restrict public access to inherited members, and do not provide the same public `is-a` substitutability as public inheritance.

```cpp
//example

#include <iostream>

class Engine {

public:

	void start() const {

		std::cout << "Engine started\n";
	}
};

class Machine : private Engine {

public:

	void run() const {

		start(); // Accessible inside Machine
	}
};

class ProtectedMachine : protected Engine {

public:

	void run() const {

		start(); // Accessible inside derived class
	}
};

int main() {

	Machine machine;
	machine.run();

	ProtectedMachine protectedMachine;
	protectedMachine.run();
}
```

Output:

```text
Engine started
Engine started
```

Calling `machine.start()` or `protectedMachine.start()` from `main()` would be an access error. Protected inheritance still permits further derived classes to access eligible inherited protected members; private inheritance does not.

---

# Single Inheritance

Single inheritance means that one derived class inherits directly from one base class.

```cpp
//example

#include <iostream>

class Vehicle {

public:

	void move() const { std::cout << "Moving\n"; }
};

class Bike : public Vehicle {};

int main() {

	Bike bike;
	bike.move();
}
```

Output:

```text
Moving
```

---

# Multilevel Inheritance

Multilevel inheritance forms a chain where a derived class becomes the base class of another class.

```cpp
//example

#include <iostream>

class LivingThing {

public:

	void live() const { std::cout << "Living\n"; }
};

class Animal : public LivingThing {};
class Cat : public Animal {};

int main() {

	Cat cat;
	cat.live();
}
```

Output:

```text
Living
```

---

# Multiple Inheritance

Multiple inheritance means that one derived class inherits directly from two or more base classes. Ambiguity arises only if inherited names or paths conflict in a particular use.

```cpp
//example

#include <iostream>

class Scanner {

public:

	void scan() const { std::cout << "Scanning\n"; }
};

class Printer {

public:

	void print() const { std::cout << "Printing\n"; }
};

class MultiFunctionDevice : public Scanner, public Printer {};

int main() {

	MultiFunctionDevice device;
	device.scan();
	device.print();
}
```

Output:

```text
Scanning
Printing
```

---

# Hierarchical Inheritance

Hierarchical inheritance means that several derived classes inherit from the same base class.

```cpp
//example

#include <iostream>

class Shape {

public:

	void identify() const { std::cout << "A shape\n"; }
};

class Circle : public Shape {};
class Square : public Shape {};

int main() {

	Circle circle;
	Square square;
	circle.identify();
	square.identify();
}
```

Output:

```text
A shape
A shape
```

---

# Hybrid Inheritance

Hybrid inheritance combines two or more inheritance structures, such as hierarchical and multiple inheritance.

```cpp
//example

#include <iostream>

class Device {

public:

	void powerOn() const { std::cout << "Powered on\n"; }
};

class Camera : public Device {};
class MusicPlayer {};
class SmartCamera : public Camera, public MusicPlayer {};

int main() {

	SmartCamera camera;
	camera.powerOn();
}
```

Output:

```text
Powered on
```

---

# Constructor and Destructor Order in Inheritance

A base class is constructed before the derived class. Destruction happens in reverse order: the derived-class destructor body runs first, followed by the base-class destructor.

```cpp
//example

#include <iostream>

class Base {

public:

	Base() { std::cout << "Base constructed\n"; }
	~Base() { std::cout << "Base destroyed\n"; }
};

class Derived : public Base {

public:

	Derived() { std::cout << "Derived constructed\n"; }
	~Derived() { std::cout << "Derived destroyed\n"; }
};

int main() {

	Derived object;
}
```

Output:

```text
Base constructed
Derived constructed
Derived destroyed
Base destroyed
```

Base-class constructors are not automatically inherited like ordinary member functions. C++ does allow explicitly inheriting eligible constructors using `using Base::Base;`.

---

# Calling a Base-Class Constructor

A derived constructor can call a particular base constructor using its member initializer list. If it does not specify one, C++ attempts to use an accessible default base constructor.

```cpp
//example

#include <iostream>

class Person {

protected:

	int age;

public:

	Person(int value) : age(value) {}
};

class Student : public Person {

public:

	Student(int value) : Person(value) {}

	void showAge() const {

		std::cout << age << '\n';
	}
};

int main() {

	Student student(19);
	student.showAge();
}
```

Output:

```text
19
```

---

# Member Name Hiding

If a derived class declares a member with the same name as a base-class member, base-class declarations of that name are hidden during ordinary name lookup in the derived class. Scope resolution can select the base-class member explicitly.

```cpp
//example

#include <iostream>

class Base {

public:

	void show() const { std::cout << "Base\n"; }
};

class Derived : public Base {

public:

	void show(int value) const {

		std::cout << "Derived " << value << '\n';
	}
};

int main() {

	Derived object;
	object.show(5);
	object.Base::show(); // Explicitly access hidden base member
}
```

Output:

```text
Derived 5
Base
```

`object.show()` would fail to compile here because the base function is hidden, even though it takes no arguments. `using Base::show;` inside `Derived` could instead bring the base overload into consideration.

---

# Function Overriding vs Function Hiding

Overriding occurs when a derived-class function overrides a virtual base-class function with a matching overriding signature. Hiding is a name-lookup effect and does not require a virtual function or matching parameters.

```cpp
//example

#include <iostream>

class Animal {

public:

	virtual void speak() const {

		std::cout << "Animal sound\n";
	}

	virtual ~Animal() = default;
};

class Dog : public Animal {

public:

	void speak() const override {

		std::cout << "Bark\n";
	}
};

int main() {

	Dog dog;
	Animal& animal = dog;
	animal.speak(); // Calls Dog's override
}
```

Output:

```text
Bark
```

The `virtual` keyword enables runtime dispatch through a base reference or pointer. Without virtual dispatch, a same-named derived function may hide the base function instead of overriding it.

---

# Diamond Inheritance Problem

The diamond problem arises when two intermediate classes inherit from the same base class and a final class inherits from both, potentially creating two separate base subobjects and ambiguous access paths.

```cpp
//example using virtual inheritance

#include <iostream>

class Person {

public:

	int id = 10;
};

class Student : virtual public Person {};
class Worker : virtual public Person {};
class Intern : public Student, public Worker {};

int main() {

	Intern intern;
	std::cout << intern.id << '\n'; // One shared Person base
}
```

Output:

```text
10
```

`virtual public Person` makes `Student` and `Worker` share one `Person` base subobject in `Intern`. Without virtual inheritance, accessing `intern.id` would be ambiguous because two `Person` subobjects would exist.

---

# Benefits, Limitations and Common Mistakes in Inheritance

Inheritance can reuse implementation and express an `is-a` relationship, but unnecessary inheritance creates tight coupling and fragile class hierarchies. If one object merely uses another, a member object (composition) is often a better fit.

Common mistakes include directly accessing private base members, assuming private inheritance supports public `is-a` conversion, forgetting to initialize a non-default-constructible base class, confusing name hiding with overriding, and omitting a virtual destructor when deleting derived objects through a base pointer.

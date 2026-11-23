#                                                                         Object Oriented Programming - III in C++
---

# Constructor Overloading

Constructor overloading allows a class to have multiple constructors with different parameter lists so objects can be initialised in different ways.

Like function overloading, the compiler selects a constructor based on the number and types of arguments passed. Every constructor has the same name as its class and no return type.

```cpp
//example

#include <iostream>

class Box {

	int width;
	int height;

public:

	Box() : width(10), height(10) {} // Default constructor

	Box(int side) : width(side), height(side) {} // One parameter

	Box(int w, int h) : width(w), height(h) {} // Two parameters

	void display() const {

		std::cout << width << " x " << height << '\n';

	}
};

int main() {

	Box first;
	Box second(5);
	Box third(4, 8);

	first.display();
	second.display();
	third.display();
}
```

Output:

```text
10 x 10
5 x 5
4 x 8
```

---

# Overloading Constructors with Different Parameter Types

Constructors can also be overloaded by parameter type, even when they take the same number of arguments.

```cpp
//example

#include <iostream>

class Measurement {

public:

	Measurement(int value) {

		std::cout << "Whole number: " << value << '\n';

	}

	Measurement(double value) {

		std::cout << "Decimal number: " << value << '\n';

	}
};

int main() {

	Measurement first(5);
	Measurement second(5.5);
}
```

Output:

```text
Whole number: 5
Decimal number: 5.5
```

The compiler chooses the best matching overload; if no unique best match exists, the constructor call is ambiguous and compilation fails.

---

# Default Arguments and Constructor Ambiguity

Default arguments let a constructor omit certain arguments, but overlapping overloads can make a constructor call ambiguous.

```cpp
//example - ambiguous code (does not compile)

class Account {

public:

	Account() {}
	Account(int balance = 0) {}
};

int main() {

	Account account; // Error: both constructors can be called without arguments
}
```

A constructor with all parameters defaulted can itself serve as a default constructor. Avoid adding another zero-argument constructor that matches the same call.

---

# Constructor Delegation

Constructor delegation, introduced in C++11, lets one constructor call another constructor of the same class to reuse initialisation logic.

```cpp
//example

#include <iostream>

class Player {

	int health;
	int level;

public:

	Player(int h, int l) : health(h), level(l) {}

	Player() : Player(100, 1) {} // Delegates to the two-parameter constructor

	void display() const {

		std::cout << health << " " << level << '\n';

	}
};

int main() {

	Player player;
	player.display();
}
```

Output:

```text
100 1
```

A delegating constructor must delegate to just one constructor in its initializer list; it cannot initialise other members in that same list. Constructor overloading is valid, but constructor overriding is not a C++ feature.

---

# Member Initializer Lists

A member initializer list is the part after a constructor's parameter list and before its body that directly initialises data members and base classes.

```cpp
//example

#include <iostream>

class Student {

	int rollNumber;
	int marks;

public:

	Student(int roll, int score) : rollNumber(roll), marks(score) {}

	void display() const {

		std::cout << rollNumber << " " << marks << '\n';

	}
};

int main() {

	Student student(12, 95);
	student.display();
}
```

Output:

```text
12 95
```

The colon `:` starts the initializer list, and each member is initialised using its corresponding value or expression.

---

# Initialization vs Assignment in a Constructor

Member initialization sets up a member as the object is created, whereas assignment inside a constructor body changes a member after it has already been initialised.

```cpp
//example

#include <iostream>
#include <string>

class Message {

	std::string text;

public:

	Message(const std::string& value) : text(value) {} // Direct initialization

	void display() const {

		std::cout << text << '\n';

	}
};

int main() {

	Message message("Hello");
	message.display();
}
```

Output:

```text
Hello
```

Writing `text = value;` in the constructor body would assign after `text` was first default-initialised. An initializer list is therefore not just a performance optimisation; some members cannot be initialised correctly through later assignment.

---

# Initializing `const` and Reference Data Members

A `const` member must receive its value during initialization, and a reference member must be bound to an existing object when it is created.

```cpp
//example

#include <iostream>

class Employee {

	const int employeeId;
	int& salary;

public:

	Employee(int id, int& amount) : employeeId(id), salary(amount) {}

	void display() const {

		std::cout << employeeId << " " << salary << '\n';

	}
};

int main() {

	int pay = 30000;
	Employee employee(101, pay);
	employee.display();
}
```

Output:

```text
101 30000
```

Neither `employeeId = id;` nor binding `salary` later in the constructor body can replace the required initialization. The referenced variable must remain alive while the reference is used.

---

# Initializing Class-Type Members

A class-type data member can be initialised by calling its constructor from the containing class's initializer list, which is necessary when that member has no usable default constructor.

```cpp
//example

#include <iostream>

class Engine {

public:

	Engine(int power) {

		std::cout << "Engine power: " << power << '\n';

	}
};

class Car {

	Engine engine;

public:

	Car(int power) : engine(power) {} // Constructs engine directly
};

int main() {

	Car car(150);
}
```

Output:

```text
Engine power: 150
```

---

# Member Initialization Order

Non-static data members are initialised in the order they are declared inside the class, not in the order written in the initializer list.

```cpp
//example

#include <iostream>

class Counter {

	int first;
	int second;

public:

	Counter() : second(20), first(10) {

		std::cout << first << " " << second << '\n';

	}
};

int main() {

	Counter counter;
}
```

Output:

```text
10 20
```

Here `first` is initialised before `second` despite appearing second in the initializer list. Write initializer lists in declaration order to avoid confusion, especially when one member depends on another.

---

# Member Initializer Lists with Overloaded Constructors

Each overloaded constructor can provide its own initializer list, while a delegating constructor can reuse another constructor's initialisation instead.

```cpp
//example

#include <iostream>

class Rectangle {

	int width;
	int height;

public:

	Rectangle(int w, int h) : width(w), height(h) {}

	Rectangle(int side) : Rectangle(side, side) {} // Delegation

	void area() const {

		std::cout << width * height << '\n';

	}
};

int main() {

	Rectangle rectangle(6);
	rectangle.area();
}
```

Output:

```text
36
```

Avoid using a member's value to initialise an earlier-declared member, assuming list order controls initialization, or trying to initialise members alongside a delegating constructor call.

---

# Destructors

A destructor is a special member function named `~ClassName()` that runs when an object's lifetime ends and is used to clean up resources owned by that object.

Unlike constructors, destructors have no return type, cannot take ordinary parameters, and cannot be overloaded; a class has at most one destructor.

```cpp
//example

#include <iostream>

class Session {

public:

	Session() {

		std::cout << "Session started\n";

	}

	~Session() {

		std::cout << "Session ended\n";

	}
};

int main() {

	Session session;
}
```

Output:

```text
Session started
Session ended
```

---

# Destructors and Scope

A destructor for an automatic local object normally executes when the object leaves its scope, and multiple local objects in the same scope are destroyed in reverse construction order.

```cpp
//example

#include <iostream>

class Task {

	int number;

public:

	Task(int n) : number(n) {

		std::cout << "Create " << number << '\n';

	}

	~Task() {

		std::cout << "Destroy " << number << '\n';

	}
};

int main() {

	Task first(1);

	{

		Task second(2);
		Task third(3);

	} // third, then second are destroyed here
}
```

Output:

```text
Create 1
Create 2
Create 3
Destroy 3
Destroy 2
Destroy 1
```

Member objects are also destroyed automatically after the containing object's destructor body runs, in the reverse order of their declaration.

---

# Destructors with `new` and `delete`

An object created using `new` is constructed during allocation, and calling `delete` on its owning raw pointer runs its destructor before releasing its allocated storage.

```cpp
//example

#include <iostream>

class Worker {

public:

	Worker() {

		std::cout << "Worker created\n";

	}

	~Worker() {

		std::cout << "Worker destroyed\n";

	}
};

int main() {

	Worker* worker = new Worker();

	delete worker; // Calls destructor and releases storage
	worker = nullptr;
}
```

Output:

```text
Worker created
Worker destroyed
```

A raw pointer member does not automatically delete the memory it points to. Dynamically allocated objects need proper ownership management, and every `new[]` allocation must be paired with the appropriate `delete[]` if raw ownership is used.

---

# Destructors and Resource Cleanup

Destructors can release resources explicitly owned by an object, such as dynamically allocated memory, when that object's lifetime ends.

```cpp
//example

#include <iostream>

class Buffer {

	int* data;

public:

	Buffer() : data(new int[3]{10, 20, 30}) {}

	~Buffer() {

		delete[] data; // Releases the owned array

	}

	Buffer(const Buffer&) = delete; // Prevents accidental copying
	Buffer& operator=(const Buffer&) = delete;

	void display() const {

		std::cout << data[0] << '\n';

	}
};

int main() {

	Buffer buffer;
	buffer.display();
}
```

Output:

```text
10
```

The destructor is responsible for cleanup here because the class owns the array. Copying this raw-owning class without appropriate copy handling could cause multiple objects to delete the same memory.

---

# Resource Acquisition Is Initialization (RAII)

RAII is a C++ resource-management technique where a resource's ownership is tied to an object's lifetime so cleanup happens automatically through its destructor.

```cpp
//example

#include <iostream>
#include <memory>

class Resource {

public:

	~Resource() {

		std::cout << "Resource released\n";

	}
};

int main() {

	std::unique_ptr<Resource> resource = std::make_unique<Resource>();

} // unique_ptr destroys the Resource automatically
```

Output:

```text
Resource released
```

RAII is generally safer than manually pairing `new` with `delete`. Prefer standard-library ownership tools such as `std::unique_ptr`, `std::vector`, and `std::string` rather than managing raw allocations directly. Manually invoking a destructor is not normal resource-management practice.

---

# Virtual Destructors

A virtual destructor allows a derived object's full destructor chain to run when it is deleted through a pointer to its base class.

```cpp
//example

#include <iostream>

class Animal {

public:

	virtual ~Animal() {

		std::cout << "Animal destroyed\n";

	}
};

class Dog : public Animal {

public:

	~Dog() override {

		std::cout << "Dog destroyed\n";

	}
};

int main() {

	Animal* animal = new Dog();
	delete animal;
}
```

Output:

```text
Dog destroyed
Animal destroyed
```

When a class is intended for polymorphic deletion through a base pointer, its destructor should normally be public and virtual. Deleting a derived object through a base pointer without a virtual destructor is generally undefined behaviour.

---

# Static Data Members

A static data member belongs to the class rather than to each individual object, so every object of that class shares the same variable.

```cpp
//example

#include <iostream>

class Player {

public:

	static int totalPlayers; // Declaration

	Player() {

		++totalPlayers;

	}
};

int Player::totalPlayers = 0; // Definition and initialization

int main() {

	Player first;
	Player second;

	std::cout << Player::totalPlayers << '\n';
}
```

Output:

```text
2
```

Unlike a non-static data member, which each object stores separately, `totalPlayers` is shared. The `::` scope resolution operator accesses the member through its class name.

---

# Accessing Static Members Through Objects

Static data members can be accessed using either the class name or an object, but class-name access makes their shared nature clearer.

```cpp
//example

#include <iostream>

class Settings {

public:

	static int volume;
};

int Settings::volume = 50;

int main() {

	Settings first;
	Settings second;

	first.volume = 80;

	std::cout << Settings::volume << '\n';
	std::cout << second.volume << '\n';
}
```

Output:

```text
80
80
```

---

# Static Member Functions

A static member function belongs to the class and can be called without creating an object; unlike a non-static member function, it has no `this` pointer.

```cpp
//example

#include <iostream>

class Employee {

	static int count;

public:

	Employee() {

		++count;

	}

	static int getCount(); // Declaration
};

int Employee::count = 0;

int Employee::getCount() { // Definition

	return count; // Can directly access private static data

}

int main() {

	Employee first;
	Employee second;

	std::cout << Employee::getCount() << '\n';
}
```

Output:

```text
2
```

A static member function can directly use static members, including private ones, but cannot directly access a particular object's non-static data members without an object or reference to one.

---

# Accessing Non-Static Members from Static Functions

Because a static member function has no current object, it must receive or otherwise obtain an object to access non-static members.

```cpp
//example

#include <iostream>

class Calculator {

	int value;

public:

	Calculator(int number) : value(number) {}

	static void display(const Calculator& calculator) {

		std::cout << calculator.value << '\n';

	}
};

int main() {

	Calculator calculator(25);
	Calculator::display(calculator);
}
```

Output:

```text
25
```

Trying to write `std::cout << value;` directly inside `display()` would fail because `value` belongs to an object, not to the class itself.

---

# `inline static` Data Members in C++17

Starting in C++17, an `inline static` data member can be declared and initialised inside the class without a separate out-of-class definition.

```cpp
//example - C++17 or later

#include <iostream>

class Game {

public:

	inline static int highScore = 0;
};

int main() {

	Game::highScore = 120;
	std::cout << Game::highScore << '\n';
}
```

Output:

```text
120
```

Traditional non-inline static data members generally need a definition outside the class when odr-used, while C++17 inline static data members do not. Static class members are different from static local variables, which are declared inside functions and retain their values between calls.

---

# Common Mistakes with Static Class Members

Common mistakes include forgetting a required traditional static-member definition, assuming each object has its own static value, and accessing non-static members directly from a static member function.

For accurate object counting, increment the count for every construction path, including copy or move construction if those operations are allowed, and decrement it in the destructor if the goal is to track objects currently alive rather than total constructions.

---

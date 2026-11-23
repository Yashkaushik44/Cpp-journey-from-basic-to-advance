#                                                                         Object Oriented Programming - V in C++
---

# Single Inheritance

Single inheritance occurs when one derived class inherits from exactly one direct base class. The derived class can reuse accessible base-class functionality and add its own members.

```cpp
//example

#include <iostream>

class Employee {

protected:

	int employeeId = 101;

public:

	void showEmployee() const {

		std::cout << "Employee ID: " << employeeId << '\n';
	}
};

class Developer : public Employee { // One direct base class

public:

	void writeCode() const {

		std::cout << "Writing code\n";
	}
};

int main() {

	Developer developer;
	developer.showEmployee(); // Inherited public function
	developer.writeCode();
}
```

Output:

```text
Employee ID: 101
Writing code
```

`public Employee` means public base members remain public in `Developer`, and protected base members remain protected. A derived member function can access `employeeId`, but code in `main()` cannot access it directly. Private base members still exist in the base subobject but are not directly accessible to ordinary derived-class functions.

---

# Multilevel Inheritance

Multilevel inheritance forms a chain in which a class derives from another derived class. The last class has both a direct base and one or more indirect bases.

```cpp
//example

#include <iostream>

class Device {

public:

	void powerOn() const {

		std::cout << "Device powered on\n";
	}
};

class Computer : public Device {

public:

	void startSystem() const {

		std::cout << "System started\n";
	}
};

class Laptop : public Computer {

public:

	void useBattery() const {

		std::cout << "Battery in use\n";
	}
};

int main() {

	Laptop laptop;
	laptop.powerOn();    // From indirect base Device
	laptop.startSystem(); // From direct base Computer
	laptop.useBattery();
}
```

Output:

```text
Device powered on
System started
Battery in use
```

Here `Laptop` directly inherits `Computer` and indirectly inherits `Device`. Accessible members can be used throughout the chain; private base members do not become directly accessible merely because another class derives from them. Base constructors execute from the oldest base toward the most-derived class, and destructors execute in reverse order.

---

# Multiple Inheritance

Multiple inheritance allows a derived class to inherit directly from two or more base classes. Unlike multilevel inheritance, it combines separate base classes rather than creating a single inheritance chain.

```cpp
//example

#include <iostream>

class Printer {

public:

	void print() const {

		std::cout << "Printing document\n";
	}
};

class Scanner {

public:

	void scan() const {

		std::cout << "Scanning document\n";
	}
};

class MultiFunctionDevice : public Printer, public Scanner {};

int main() {

	MultiFunctionDevice device;
	device.print();
	device.scan();
}
```

Output:

```text
Printing document
Scanning document
```

`MultiFunctionDevice` has two direct base classes, `Printer` and `Scanner`. Multiple inheritance does not automatically create member-name ambiguity when the inherited names are distinct.

---

# Member Name Ambiguity in Multiple Inheritance

An unqualified member call can be ambiguous when lookup finds conflicting inherited members with the same name. Specify the desired base class using the scope resolution operator `::`.

```cpp
//example

#include <iostream>

class Camera {

public:

	void start() const {

		std::cout << "Camera started\n";
	}
};

class Microphone {

public:

	void start() const {

		std::cout << "Microphone started\n";
	}
};

class Recorder : public Camera, public Microphone {};

int main() {

	Recorder recorder;
	// recorder.start(); // ERROR: ambiguous call
	recorder.Camera::start();
	recorder.Microphone::start();
}
```

Output:

```text
Camera started
Microphone started
```

The commented call is intentionally invalid; both base classes offer `start()`. Qualified calls identify the intended base. Ambiguity depends on the actual candidates found by name lookup, not simply on having multiple base classes.

---

# Hierarchical Inheritance

Hierarchical inheritance occurs when several derived classes share one common base class. Each derived class can reuse the base interface and extend it independently.

```cpp
//example

#include <iostream>

class Vehicle {

public:

	void start() const {

		std::cout << "Vehicle started\n";
	}
};

class Car : public Vehicle {

public:

	void openTrunk() const {

		std::cout << "Car trunk opened\n";
	}
};

class Bike : public Vehicle {

public:

	void lowerStand() const {

		std::cout << "Bike stand lowered\n";
	}
};

int main() {

	Car car;
	Bike bike;
	car.start();
	car.openTrunk();
	bike.start();
	bike.lowerStand();
}
```

Output:

```text
Vehicle started
Car trunk opened
Vehicle started
Bike stand lowered
```

`Car` and `Bike` each have their own `Vehicle` base subobject. Hierarchical inheritance branches from a common base, whereas multilevel inheritance forms a chain.

---

# Hybrid Inheritance

Hybrid inheritance is a descriptive term for combining inheritance structures, such as multilevel and multiple inheritance. It is not a separate C++ keyword or language feature.

```cpp
//example

#include <iostream>

class Machine {

public:

	void turnOn() const {

		std::cout << "Machine on\n";
	}
};

class Computer : public Machine {

public:

	void process() const {

		std::cout << "Processing data\n";
	}
};

class NetworkDevice {

public:

	void connect() const {

		std::cout << "Network connected\n";
	}
};

class Server : public Computer, public NetworkDevice {};

int main() {

	Server server;
	server.turnOn();
	server.process();
	server.connect();
}
```

Output:

```text
Machine on
Processing data
Network connected
```

`Server` inherits directly from `Computer` and `NetworkDevice`, while `Computer` inherits from `Machine`. This combines multiple and multilevel inheritance without a diamond or duplicate `Machine` subobjects.

---

# Diamond Problem in Hybrid Inheritance

A diamond occurs when two inheritance paths lead to the same base class. With ordinary non-virtual inheritance, the most-derived object can contain two separate subobjects of that common base.

```cpp
//example

#include <iostream>

class Person {

public:

	int id = 10;
};

class Student : public Person {};
class Worker : public Person {};
class Intern : public Student, public Worker {};

int main() {

	Intern intern;
	// std::cout << intern.id; // ERROR: two Person subobjects
	std::cout << intern.Student::id << '\n';
	std::cout << intern.Worker::id << '\n';
}
```

Output:

```text
10
10
```

`Student` and `Worker` each contribute a different `Person` subobject to `Intern`. The direct call `intern.id` is ambiguous; qualification selects which subobject to use. Not every hybrid structure forms a diamond.

---

# Virtual Inheritance

Virtual inheritance lets different paths share a common virtual base subobject within the most-derived object. Write `virtual` in the inheritance declaration for the paths that should share that base.

```cpp
//example

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
	intern.id = 42; // One shared Person subobject
	std::cout << intern.Student::id << '\n';
	std::cout << intern.Worker::id << '\n';
}
```

Output:

```text
42
42
```

Both paths refer to the same `Person` subobject. Virtual inheritance addresses duplicate shared-base subobjects, but it does not resolve every possible conflicting name in multiple inheritance.

---

# Constructor Order in Single Inheritance

When a derived object is created, its base subobject must be initialized before the derived class constructor body runs. Destruction takes place in the opposite order.

```cpp
//example

#include <iostream>

class Base {

public:

	Base() { std::cout << "Base constructor\n"; }
	~Base() { std::cout << "Base destructor\n"; }
};

class Derived : public Base {

public:

	Derived() { std::cout << "Derived constructor\n"; }
	~Derived() { std::cout << "Derived destructor\n"; }
};

int main() {

	Derived object;
}
```

Output:

```text
Base constructor
Derived constructor
Derived destructor
Base destructor
```

The local object is destroyed when `main()` ends. The derived destructor body runs first, followed by the base destructor.

---

# Constructor Order in Multilevel Inheritance

In a multilevel chain, constructors run from the oldest base to the most-derived class, while destructors run from the most-derived class back to the oldest base.

```cpp
//example

#include <iostream>

class A {

public:

	A() { std::cout << "A constructed\n"; }
	~A() { std::cout << "A destroyed\n"; }
};

class B : public A {

public:

	B() { std::cout << "B constructed\n"; }
	~B() { std::cout << "B destroyed\n"; }
};

class C : public B {

public:

	C() { std::cout << "C constructed\n"; }
	~C() { std::cout << "C destroyed\n"; }
};

int main() {

	C object;
}
```

Output:

```text
A constructed
B constructed
C constructed
C destroyed
B destroyed
A destroyed
```

---

# Constructor Order in Multiple Inheritance

Direct non-virtual base classes are initialized in the order they appear in the class's inheritance list, regardless of the order written in its constructor initializer list. Their destruction order is reversed.

```cpp
//example

#include <iostream>

class Engine {

public:

	Engine(int power) {

		std::cout << "Engine: " << power << '\n';
	}

	~Engine() { std::cout << "Engine destroyed\n"; }
};

class Radio {

public:

	Radio() { std::cout << "Radio constructed\n"; }
	~Radio() { std::cout << "Radio destroyed\n"; }
};

class Car : public Engine, public Radio {

public:

	Car() : Radio(), Engine(120) { // Written order does not control construction

		std::cout << "Car constructed\n";
	}

	~Car() { std::cout << "Car destroyed\n"; }
};

int main() {

	Car car;
}
```

Output:

```text
Engine: 120
Radio constructed
Car constructed
Car destroyed
Radio destroyed
Engine destroyed
```

`Engine(120)` initializes the parameterized base constructor as part of object construction; it is not an ordinary function call made inside the derived constructor body. Declaring `Car : public Engine, public Radio` fixes the base initialization order.

---

# Construction and Destruction of Member Objects

After all base classes are initialized, non-static data members are initialized in their declaration order. The constructor body runs afterward. During destruction, the class destructor body runs first, then members are destroyed in reverse declaration order, followed by base classes.

```cpp
//example

#include <iostream>

class Base {

public:

	Base() { std::cout << "Base constructed\n"; }
	~Base() { std::cout << "Base destroyed\n"; }
};

class Part {

	const char* name;

public:

	Part(const char* partName) : name(partName) {

		std::cout << name << " constructed\n";
	}

	~Part() { std::cout << name << " destroyed\n"; }
};

class Device : public Base {

	Part first;
	Part second;

public:

	Device() : second("Second"), first("First") {

		std::cout << "Device constructed\n";
	}

	~Device() { std::cout << "Device destroyed\n"; }
};

int main() {

	Device device;
}
```

Output:

```text
Base constructed
First constructed
Second constructed
Device constructed
Device destroyed
Second destroyed
First destroyed
Base destroyed
```

Although `second` appears first in the initializer list, `first` is declared first and therefore initializes first. Reordering initializers to match declarations is recommended because it avoids misleading code and compiler warnings.

---

# Constructor Order with Virtual Base Classes

Virtual bases are initialized before non-virtual direct bases and members. For multiple virtual bases, their order follows the first encounters in a depth-first, left-to-right traversal of the inheritance graph. The most-derived class is responsible for initializing each virtual base.

```cpp
//example

#include <iostream>

class Person {

public:

	Person(int id) {

		std::cout << "Person: " << id << '\n';
	}

	~Person() { std::cout << "Person destroyed\n"; }
};

class Student : virtual public Person {

public:

	Student() : Person(1) { // Ignored for Person when constructing Intern

		std::cout << "Student constructed\n";
	}

	~Student() { std::cout << "Student destroyed\n"; }
};

class Worker : virtual public Person {

public:

	Worker() : Person(2) { // Ignored for Person when constructing Intern

		std::cout << "Worker constructed\n";
	}

	~Worker() { std::cout << "Worker destroyed\n"; }
};

class Intern : public Student, public Worker {

public:

	Intern() : Person(99), Worker(), Student() {

		std::cout << "Intern constructed\n";
	}

	~Intern() { std::cout << "Intern destroyed\n"; }
};

int main() {

	Intern intern;
}
```

Output:

```text
Person: 99
Student constructed
Worker constructed
Intern constructed
Intern destroyed
Worker destroyed
Student destroyed
Person destroyed
```

`Person(99)` is selected by `Intern`, the most-derived class. The `Person(1)` and `Person(2)` initializers apply when `Student` or `Worker` is itself the most-derived object, but not when either is a base subobject of `Intern`. The virtual `Person` subobject is destroyed last.

---

# Virtual Destructors in Inheritance

When a derived object may be deleted through a pointer to its polymorphic base class, the base destructor should be virtual. This ensures the derived destructor and then the base destructor run correctly.

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
	delete animal; // Calls both destructors safely
}
```

Output:

```text
Dog destroyed
Animal destroyed
```

With an ordinary non-virtual base destructor, deleting a derived object through this kind of base pointer can cause undefined behavior. In real programs, standard-library smart pointers are generally preferable for owning dynamically allocated objects.

---

# Common Mistakes in Inheritance and Object Lifetime

Common mistakes include trying to access a private base member directly, confusing multiple inheritance with a multilevel chain, assuming every hybrid hierarchy is a diamond, and making an unqualified call when inherited names are ambiguous.

Construction-order mistakes include assuming initializer-list order overrides base or member declaration order, forgetting to initialize a base that has no default constructor, and expecting a base constructor to run like an ordinary function inside a derived constructor body. Destruction reverses the actual completed construction order; an unsafe non-virtual base-pointer deletion must not be used to test that rule.

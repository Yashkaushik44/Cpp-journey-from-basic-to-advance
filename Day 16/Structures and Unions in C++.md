#                                                                                     Structures and Unions in C++

---

# Structure using struct 

`struct` is a user-defined data type that groups related variables of different types together under a single name.  Members are public by default. 

```cpp
// The following is the syntax of stuct in c++. I used <> to insert and this should not be treated as syntax.

#include <iostream>

struct <structure_name> {

	<data_type1> <variable_name1>;
	<data_type2> <variable_name2>;
	<data_type3> <variable_name3>;
	
};

int main() {
	
	<structure_name> <vatiable_name> = { <value_of_data_type1>, <value_of_data_type2>, <value_of_data_type3};

	return 0;
	
}
```

**Note**:- You can only use data types specified in the structure when using struct.

```cpp
//example

#include <iostream>
#include <string>

struct Student {

	std::string name;
	int age;
	float percentage;

};

int main() {

	Student student1 = {"User", 18, 99.9};

	return 0;
	
}
```

---

#  Union

It is a user defined data type that stores different member variables in the exact same memory location. Only one member can hold a valid value at any given time.

## Uses of Union

1. Memory Efficiency
	Used in resource constrained systems to save RAM by sharing memory between variables that are never needed simultaneously.
	```cpp
	//example
	#include <iostream>

	union Data {
	
		int integer;
		char character;
		
	};
	
	int main() {
	
		Data x;
		
		x.integer = 65;
		
		x.character = 'A'; //this overwrites the memory of integer and stores its own value at that location
	
		return 0;
		
	}
	```
	
	
2. Tagged Unions
	It is used to store safely store different data types inside a single dynamically typed payload.
	```cpp
	//exmaple
	
	#include <iostream>
	
	enum Data {INT_TYPE, FLOAT_TYPE};
	
	struct InputValue {
	
		Data value;
	
		union {
	
			int i_val;
			float f_val;
	
		};
	};
	
	int main() {
	
		ImputValue val;
		val.value = INT_TYPE;
		val.i_val = 100;
		
		if(val.value == INT_TYPE) {
			
			std::cout<< "Stored an int: "<< val.i_val<< "\n";
		
		}
	
		return 0;
		
	}
	```
	
3. Vector Aliasing
	Access the exact same coordinates by name `(x, y)` or by index position (`arr[0]`, `arr[1]`).
	```cpp
	//example
	
	#include <iostream>
	
	struct Point2D {
	
		union {
		
			struct {float x, y;};
			float arr[2];
		
		}
	}
	
	int main() {
	
		Point2D pt = {3.5f, 7.2f};
		
		std::cout<< "Access by name: "<< pt.x<< "\n"; // output: 3.5
		std::cout<< "Access by index: "<<pt.arr[0]<< "\n"; //output: 3.5
		
		return 0;
		
	}
	```
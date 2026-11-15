#                                                                                                   Functional Programming in Python
---
# functools.reduce() and Functional Programming Basics

Functional programming is a way of writing code by breaking tasks into small, reusable functions that take inputs and return outputs without changing outside data.

Unlike `map()` (which changes every item) and `filter()` (which picks specific items), `reduce()` combines all items in a group into one single result (like a sum, product, or combined string).

To use it, you must import `reduce` from the built-in `functools` module.

```
# syntax
from functools import reduce

result = reduce(function, iterable, initial_value)
```

- **How it works:** It takes two values at a time: the **accumulator** (the running result so far) and the **current element** (the next item from the list).
    
- **Initial value (optional):** Gives the accumulator a starting value. It is very useful to prevent errors if the list is empty.
    

```
from functools import reduce

numbers = [1, 2, 3, 4]

# Multiply all numbers together
total = reduce(lambda acc, curr: acc * curr, numbers) #output: 24

# Watch how the accumulator changes step-by-step:
# Step 1: acc = 1, curr = 2 -> 1 * 2 = 2
# Step 2: acc = 2, curr = 3 -> 2 * 3 = 6
# Step 3: acc = 6, curr = 4 -> 6 * 4 = 24

# Using an initial value of 10 with an empty list
empty_result = reduce(lambda acc, curr: acc + curr, [], 10) #output: 10
```

# Pure Functions

A function that relies only on the inputs passed to it and does not touch anything outside itself. They are predictable, easy to test, and safe from unexpected bugs.

- **Two main rules:**
    
    - Always returns the exact same output for the exact same inputs.
        
    - Causes no side effects (it returns a value instead of printing or changing outside variables).
        

```
# Pure function (depends only on inputs and returns a result)
def calculate(a, b):
    return a + b

result = calculate(3, 5) #output: 8

# Not a pure function (uses an outside variable and prints instead of returning)
bonus = 10
def add_bonus(value):
    print(value + bonus) #output: 15 (changes if bonus changes)

add_bonus(5)
```

# Side Effects

Happens when a function reaches outside its own local space and changes something in the rest of your program or computer.

- **Common examples:**
    
    - Changing a global variable.
        
    - Modifying a mutable object passed into it (like adding an item to an outside list).
        
    - Printing text to the screen with `print()`.
        
    - Reading from or writing to a file.
        

Side effects are not always bad—programs need them to show output or save files—but keeping them separate from your main logic makes code much easier to manage.

```
numbers = [1, 2, 3]

# Function WITH a side effect (modifies the outside list)
def add_item(value):
    numbers.append(value)

add_item(4) # numbers is now [1, 2, 3, 4]

# Function WITHOUT a side effect (returns a brand new list)
def get_new_list(items, value):
    return items + [value]

result = get_new_list([1, 2, 3], 4) #output: [1, 2, 3, 4]
```

# Closures

A nested (inner) function that remembers and keeps access to variables from its outer (enclosing) function, even after the outer function has finished running.

In Python, an **enclosing scope** is the space inside an outer function that wraps around an inner function. Closures use this space to store data safely without needing global variables.

```
def create_multiplier(factor):
    # 'factor' is in the enclosing scope
    def multiply(value):
        return value * factor # inner function remembers 'factor'
    return multiply

double = create_multiplier(2) # create_multiplier finishes running here
result = double(5) #output: 10 (still remembers factor = 2)
```

# Higher-Order Functions

In Python, functions are **first-class objects**, meaning you can treat them just like normal values (store them in variables, pass them around, or return them).

A higher-order function is simply a function that does at least one of two things: takes another function as an argument, or returns a function as its result. They are the building blocks of functional programming because they let you reuse logic easily.

- **Passing a function as an argument:** Pass the function name without parentheses `()`. Adding `()` calls the function immediately instead of passing the function itself.
    

```
def square(x):
    return x * x

# Higher-order function taking a function as an argument
def calculate(func, value):
    return func(value)

result = calculate(square, 4) #output: 16
```

- **Returning a function:**
    

```
# Higher-order function returning another function
def get_greeter(greeting):
    def greet(name):
        return f"{greeting}, {name}"
    return greet

say_hello = get_greeter("Hello")
result = say_hello("Sam") #output: Hello, Sam
```
#                                                                           Python conditions and logical operators
---

# if - elif - else

We use conditions in python to perform case based logical programming.

For this we use `if elif else` .

```python
#this is the syntax for using conditons. We are using <> for getting your input in it and it is not a syntax

if <condition> :
	
	<code_block>
	
elif <condition>:
	
	<code_block>
	
else:

	<code_block>
```

**Note:-** You can only use `if` and `else` one time in a condition block but you can use elif as much times as needed.

It is not necessary to use `elif` every time, you can also use `if - else` pair if needed.

example:-

```python
''' We want this function to check if num1 `is odd or even '''

num1 = 4

if num1 % 2 == 0: #we are checking if the remainder is equals to 0.

	print("num1 is even") #if num1 is zero then this code block will execute 
	
else: # if the value doesn't satisfy the above if statement then this else condition will work

	print("num1 is odd") #this code will run if num1 doesn't satisfy any of the other condition statements
```

---

# Nested conditions 

We use nested conditions when we need to check a second condition only after the first condition is satisfied.

```python
#this is the syntax for using nested conditions. We are using <> for getting your input in it and it is not a syntax

if <condition> :
	
	if <condition> :
	
elif <condition>:
	
	if <condition> :
	
else:

	if <condition> :
```

This is useful to solve problems that need multiple conditions to be satisfied.

example:

```python
marks = int(input("Enter your marks: ")) #this prompt's the user to enter their marks in integer data type and store it in marks variable.

if marks >= 33: #parent conditon
    print("You passed!")

    if marks >= 90: #this only works when the parent conditon is fullfilled 
        print("You got a distinction!")
        
else:
    print("You failed.")
```
---

# match and cases


We use match and cases to compare a value against multiple patterns and execute the code for the first matching case. It can be used as an alternative for `if elif else` in some cases.

**Warning:-** For applying conditions on range, we have to use `if elif else` statements. Match statement only works on certain values not on range.

```python 
#this is the syntax for using match and cases. We are using <> for getting your input in it and it is not a syntax.

match <variable_to_compare_against>:

	case <value1>:
	
		<code_block>
		
	case <value2>:
	
		<code_block>
		
	case <value3>:
	
		<code_block>
```

**See this file for the example: ![Calc](calc.py)**

---

# Logical operators

Operators used to combine or reverse conditions to get a result.

**They are of 3 types:-**

- and
- or
- not

```python 
#this is the syntax for using logical operators. We are using <> for getting your input in it and it is not a syntax.

if <condition> and <condition>: # Strictly only works when both condtions are True.
	
	<code_block>
	
elif <condition> or <condition>: # works when even one of the conditon is True
	
	<code_block>
	
elif not <condition>: #This reverse the boolean value, changing True to False and False to True, example:- not True -> False

	<code_block>
	
else:

	<code_block>
```

**See this file for the example: ![Logical_operators](logical_operators.py)**


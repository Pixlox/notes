#software-engineering/y11

### Binary data
---
All data in a computer is composed of a pattern of 1s and 0s. Programmers specify the type of data to be stored, so that a single pattern could refer to several different meanings. For example 01001010 could be the letter 'J', the number 74 of the value 18 and a half.


### Identifier
---
Programs can store data in either a variable or a constant. Variables can be read and modified throughout the program, whereas constants can only be read. Both are given an identifier, or name, which makes it simpler to access stored data throughout the program. 

Identifier should indicate the contexts or purpose of the value, but still be concise. The example (below) shows a variable being set, modified and accessed in Python.

```python
number = 5
number = 7
print(number)

OUTPUT: 7
```

#### Conventions
Programmers often follow shared conventions, which make it easier for them to read and understand each others' code. Some of the conventions of identifiers: 
- headlessCamelCase for variables and functions
- MACRO_CASE for constants
- CamelCase* for class names

Some programmers also use snake_case, Train-Case, and kebab-case


### Primitive data types
---
There are four data types in programming:
- Integers (ints)
	- Store whole numbers (eg. 5, 64792, -30, 0)
- Floating points (floats)
	- Store numbers which a decimal point (eg. 93.5, -0.003, 6.0)
- Booleans
	- Store either True or False
- Characters
	- Store a single letter/number/symbol (eg. 'R', '6', &')

#### What about strings?
A variable can only store one piece of data at a time. Multiple data can be stored in one location with data structures.

Since strings can store multiple characters, they are technically a data structure. However, they are often referred to and treated as a type by programmers. Some languages, including Python, cannot distinguish between characters and strings.

### Casting
---
Converting a data item from one type to another is called casting. For instance, input in Python is automatically stored as a string. Numeric values must be cast to integers or floats before they can be used.

Note that this will cause an error if the conversion is not possible.


### Floats
---
- Floating point numbers have a decimal point and can store fractional numbers. Any time you use the division operator in Python, the result is automatically a float. The round() function rounds a value to the specified number of decimal places. Casting to an integer, however, simply removes any values past the decimal point.
- Floats can be problematic! They are difficult for computers to store accurately, and this can cause unexpected behaviour in programs.

### Values
---
- Every single character has a unique code (called a keycode or code point) assigned to it. The Python function `ord()` returns the code for a single character. The `chr()` function returns the character for a given code. 
- Note that the appearance of each character depends on your font settings. Compare Courier New (left) with Arial (right).

### Functions 
---
A function is a block of code that can be used repeatedly. Each function should complete one logical task. All of a program's logic should be separated into functions; this makes it easier to read, debug and modify.

Parameters are the values passed to or returned from a function. Variables created inside a function can typically only be used within that function. 

Since returning takes the program out of the function, a return statement is usually the last part of a function. It is bad practice to have multiple return statements within a function.



### Arrays
---
An array is an ordered collection of related values of the same data type. We can visualise this collection as a row.

| 5   | 3   | 8   | 1   | 9   | 2   | 4   |
| --- | --- | --- | --- | --- | --- | --- |

Each position in the array can identified by its index, which can be used to access or change a value. In most languages, the first position has an index of 0. However, in some languages (including ALGOL, Lua, MatLab, Smalltalk), the first position has an index of 1.

### Records
---
A record is a collection of related key-value pairs. Instead of an index, a value is located with its key. This is often used to specify the attributes of a complex entity. For example, a person has a name, an age, and an address; a record could store all these details together.

Python has records, which it calls Dictionaries.

Python uses brackets with the key name (usually a string) to access the value. To add a new key-value pair to the dictionary, assign a value to a new key.


#### Iterating through an array
---
Having stored a lot of data in an array, it's important to be able to access it afterwards. A very common process is to iterate through the array. This requires a loop, which initialised a variable (often called an iterator, or just 'i') to the first position of the array, and increments it each time.

This process allows for many different actions, including displaying each value in the array, finding the sum of all values, and checking each value against a target value.


#### Populating an array
---
Say you wanted an array with all the even numbered between 2 and 1000. It would be incredibly slow and frustrating to type this out manually. Instead, create an empty array, then loop through the desired values and append each one.


### Nested data structures
---
A data structure is a way of organising related data. Sometimes, these related data items may contain more data structures. It is very common to use an array of arrays (known as a 2D array) or an array of records.

Data structures can be infinitely nested; this versatility makes them very useful. However, if they become too complex, humans will be unable to understand — or improve — the code.

#### 2D Array
Consider an array in which each value is another array.

using the index to access a location in this array will return a new array, rather that a specific value. To access a specific value, a second index for the inner ray must be used.

For example:
```pseudocode
array[1] will return [D, E, F]
array [1][2] will return 'F'
```


#### Iterating through a 2D array
To examine every item in a 2D array, two loops are necessary. The outer loop iterates through the main array, allowing access to each of the sub-arrays. The inner loop iterates through the current sub-array.

Since 'i' is typically used for the first iterator, 'j' is often used for the second.

#### Displaying an array
Simply outputting an array can be difficult to read and understand. This is even more problematic when dealing with more complex data structures. By iterating through the array, each value can be displayed in a suitable way.

#### Tables as 2D Array
A 2D array is often used to store the data of a table or grid. Two indices are required to access a specific value. The first index indicates the row, the second indicates the column.

### File operations
---
A file is a resource for storing data outside a program. It is a form of non-volatile memory, meaning the data persists even when the machine is turned off. Languages work with files in different ways, but typically must:
- Open the file, specifying the purpose
	- Read the data into a variable, *OR*,
	- Write from a variable into the file
- Close the file 
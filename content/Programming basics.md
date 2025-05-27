#software-engineering

### Syntax vs logic
---
- Syntax is the grammar of a programming language; your syntax has to be correct in order for the program to run.
- Logic is the meaning of a program's instructions; your logic has to be correct in order for the program to do what you say.

### Algorithms
---
- An algorithm is a way of expressing logic without using the syntax of any specific programming language. There are still rules, but these are more flexible than the syntax of a programming language.
- You can think of algorithms as a "universal language" for programmers.

### Control structures
---
A program or algorithm is, at its heart, the use of control structures to manipulate data. A control structure is a block that determines the order in which instructions are executed (carried out) in a program.

### Algorithm Flowcharts
---
- Every program must start with BEGIN and finish with END. In an algorithm flowchart, these are written inside rounded rectangles.
- A process is a simple instruction, represented in a flowchart by a rectangle. Not that there must be *exactly* one arrow leaving the process. The most common process is to create or change a variable.
- When a user enters data into a program, this is called input. When a program gives the user some data, this is called output.
- A flowchart used a parallelogram for both input and output and used words like "get" or "display".

### Loops
---
- To stop our loop from going on forever, a decision is added containing a condition. One path from the decision will continue the loop, the other will exit the loop.

#### Post test repetition
- A very useful but less common, type of repetition executes the block of code and then checks the condition. Depending on the result, the program returns to the start of the block or proceeds to the next line of code.
- This is called post-test repetition (because the condition is tested after completing the block). Many languages offer a `REPEAT` loop, a `DO-WHILE` loop or both; however neither are available in Python.

#### Counted repetition
- Another very common type of repetition executes the block of code a specific number of times. This is called counted repetition and typically uses the keyword `FOR`.

### Functions
---
A function is a self contained block of code that performs a single logical task. There are many advantages of functions, including:
- reusable
- make code easier to read
- easier to find and correct errors
- save time and space


### Abstraction / Refinement
---
The scale at which one should consider a problem depends on the type of problem and the intended action.
- Abstraction is the process of ignoring detail and focusing on essential features
- Refinement is the process of focusing on the details of a specific feature.
Both are necessary at different points.

### Input / Process / Output
---
An IPO chart is a tool used to describe the processes in a program that transform input into output.
##### Input
- The data sent to a process by the user or from another process.
##### Process
- An action, or series of instructions, that occur
- May represent a function in a program, or a group of functions
- Can be written in plain text or as pseudocode - typically a hybrid
##### Output
- The data sent from a process to the user or to another process

#### Common errors
You must ensure that your input and output values are **data**, not processes or objects; eg.:
- If the user enters their name, the data is "name", not "type name"
- If the user clicks a point on the screen, the data is "x/y coordinates", not "click"
- If a high score is being displayed on the screen, the output is "high score", not "display high score"
- If the user clicks to proceed to the next screen, there is **no data** being input - just a command.

### Wordle IPO chart
---

| Input       | Process                                                                                                                                                      | Output                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| Letter      | Check letter validity                                                                                                                                        | - Display letter in input box                              |
| Word        | Validate word, compare with secret word. If secret word = word, display victory message. If correct, but misplaced/placed letter correct, continue and show. | - Victory message<br>- Correct, misplaced<br>- Guess count |
| Guess count | Check max attempts                                                                                                                                           | - Game over message<br>- Secret word                       |

### Problem breakdown
---
A problem is typically described in an abstract way; before programming a solution, the problem needs to be refined. Consider a game of Tetris; pieces need to be created and dropped, the user needs to be able to move and rotate them, the program needs to test for collisions, and complete lines need to be removed.

Write out the key processes; in this case, they all occur inside the game loop.

- While game has not ended:
	- Generate new piece
	- Check for collisions
	- Move piece down
	- Respond to user input
	- Remove full lines.

Next, each of these processes need to be refined.


### Wordle - Refinement
----
`chooseWord()` — grabs word from DB according to specific day
`inputGuess()` — takes guess input, and checks against target word. Validates input data
`guessCheck()` — If guess matches word, end game. Increments guess count, if guess count is 6, end game.
`wordDisplay()` — Displays letters (correct pos/in word?) if guess count is below 6.
`displayMessage()` — Displays win/loss


### Selecting data structures
---
Once you have a general idea of the program's processes, you need to identify the required data structures. Some things you need to remember:
- Anything grid-based will likely use a 2D array.
- A pixel-based display is a grid
- A sequence of action can be stored as an array
- Strings are technically arrays of characters - so a string can be manipulated in the same ways as an array.
- Paired data can be stored in a tuple (if the values are independent) or dictionary (if one of the values will be used to locate the other)
- You can nest any data structure within any other data structure; for example, you could have an array, in which each item is a dictionary, and one of the values in each dictionary is a 2D array, in which each item is a tuple.

Select data structures based on what will be the most efficient and usable. The suggestions above are not always true.

### Data dictionary
---
A data dictionary stores the details of all identifiers in a program. This is particularly useful when a team of developers are all contributing to a program. It is drawn as a table with a row for each identifier (or variable), and columns for:
- Name
- Data type
- Format
- Storage size (bytes)
- Length (characters)
- Scope
- Description (of purpose)
- Example
- Validation

##### Example
---

| Name     | Type               | Format      | Description                  | Validation       |
| -------- | ------------------ | ----------- | ---------------------------- | ---------------- |
| avg      | float              | NN.NN       | Average for a class          | 0 <= avg <= 100  |
| students | Array of [student] |             | All the students in a class  |                  |
| student  | Record             |             |                              |                  |
| -> name  | String             | SurnameName | The student's full name      |                  |
| -> DOB   | Float              | DD/MM/YYYY  | The student's date of birth  |                  |
| ->       | Integer            | NN          | The student's mark in a task | 0 <= mark <= 100 |
|          |                    |             |                              |                  |





| Name          | Type   | Scope      | Description                                                              | Validation                                  |
| ------------- | ------ | ---------- | ------------------------------------------------------------------------ | ------------------------------------------- |
| `word_list`   | String | Game       | The current target word that the player must guess                       | 5-letter word, a valid word                 |
| `guess`       | String | User Input | The word input by the player as a guess                                  | 5-letter word, a valid word                 |
| `attempts`    | Int    | Game       | The number of guesses the user has guessed                               | 0-6                                         |
| `maxAttempts` | Int    | Game       | The max number of guesses allowed                                        | 6                                           |
| `feedback`    | Array  | Game       | The feedback on each letter in the guess (correct, in word, not in word) | 5 elements: {correct, in word, not in word} |
| `validWords`  | Array  | Game       | The list of acceptable words for guesses                                 | Contains valid 5-letter words               |
| `status`      | String | Game       | The current status of the game (win, loss)                               | playing, won, lost                          |



### Structure chart
---
A structure chart is used to show the hierarchy of functions in a program. It includes details like the name of each function, the order in which they are called, the parameters that are passed and returned, whether a function is repeated, and whether the function is optional.

Different symbols and shapes are used to represent each of these.

Important note: A structure chart gives *NO* information about what the program does or how it does it.
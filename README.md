
# The pySIMAS Programming Language
*Created by: Turrnut, forked and ported by Tuvalutorture*<br>
**Current Version v0.0.1**<br>
**SIMAS**, which is an acronym for **SIM**ple **AS**sembly, is a dynamically typed, Just-In-Time
(JIT) compiled, high level, procedural programming language with a syntax that is inspired
by the Assembly programming language. In SIMAS, each line starts with an instruction,
optionally followed by one or more operands, just like Assembly. pySIMAS is designed to be a direct 
1-to-1 port of SIMAS from JavaScript to Python for easier changes and portability.<br>

SIMAS is designed to be minimal. The run function contains all of the code you need to run
a SIMAS program. the parameter, inputText, is your SIMAS code.<br>

The instruction and its operands are separated by one space character and one space character
only, if anything other that is entered, unexcepted behavior will take place. Also, lines of
code are separated by semicolons, as new lines are ignored. 

To run a SIMAS program, load it by typing "load("")" with the blank 
quotes being your file path. Then it should work.

This also patches a bug where everything, including numbers, are treated as strings. 
This fixes that and allows for integers and floating point numbers to be inputter for basic operations.

## DOCUMENTATION 
### DATA TYPES 
#### - bool : a boolean value.
####        0 is false, all other numbers are true
####        an empty string is false, all other strings are true
#### - num  : a number, can be an integer or a decimal
#### - str  : a string of characters
## INSTRUCTIONS
#### - add
#### add the value of OPERAND 2 and 3 (as of now can only handle num)
#### the value will be assigned to OPERAND 2, if it is a variable name
#### OPERAND 1: the data type of both OPERAND 2 and 3
#### OPERAND 2: the first addend, optionally being a variable name
#### OPERAND 3: the second addend, optionally being a variable name

#### - comment
#### until a semicolon is seen, the rest of the line is ignored.

#### - copy
#### copy a variable's value to another
#### OPERAND 1: the name of the variable copying from
#### OPERAND 2: the name of the variable copying to

#### - print
#### print something to the console.
#### OPERAND 1: The name of the variable which the information is stored

#### - printc
#### print a constant to the console.
#### OPERAND 1: The constant being printed

#### - println
#### print a new line

#### - set
#### assign a value to a variable.
#### OPERAND 1: the type of value
####	if the operand here is "in", then the value of the user input will be stored
####	at this variable	
####	OPERAND 2: the name of the variable
####	OPERAND 3: the value you wish to assign

#### - start
#### initializes the program and the BOXES.

#### - sub
#### performs operation of OPERAND 2 minus OPERAND 3 (as of now can only handle num)
#### the value will be assigned to OPERAND 2, if it is a variable name
#### OPERAND 1: the data type of both OPERAND 2 and 3
#### OPERAND 3: the subtrahend, optionally being a variable name
#### OPERAND 2: the minuend, optionally being a variable name

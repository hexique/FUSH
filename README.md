
# FUSH
FUSH - programming language based on Python. ade as simple as possible for beginners, without brackets, quotes and even colon.
## Syntaxis
There's some code examples on FUSH

Calculator:
```
loop
    output Write a number №1
    input a
    var int a a
    output Write an operation (+, -, *, /)
    input operation
    output Write a number №2
    input b
    var num b b 
    is operation = "+"
        outputf <a> + <b> = <a+b>
    also operation = "-"
        outputf <a> - <b> = <a-b>
    also operation = "/"
        outputf <a> / <b> = <a/b>
    also operation = "*"
        outputf <a> * <b> = <a*b>
```

Guess number:
```
var client_num 0

loop
    var atts 0
    var func num rand 1 1000
    loop
        output Guess a number between 1 and 1000
        input client_num
        var int client_num client_num
        is client_num > num
            output Lower!
            var atts atts+1
        also client_num < num
            output Higher!
            var atts atts+1
        otherwise
            outputf Guessed for <atts> attempts
            output Press Enter to play again
            input x
            exit

```

## Commands
`output` - prints your text in console\
`input` - takes input of client and write it in variable\
`is` - executes a block of code if the statement is true. Usage: is {var1} {operator} {var2}\
`also` - like "is" command. Usage same like in "is"\
`otherwise` - executes a block of code if all the statements turned out to be false.\
`until` - executes a block of code until a statement becomes true. Usage: until {statemate}\
`loop` - executes a block of code a certain number of times. Usage: loop {var1} to {end} from {start} {step}\
`exit` - exits from cycle\
`repeat` - start cycle from start\
`func` - declare a function. Usage: func name\
`args` - used in functions, declare a argumets in function\
`back` - returns a value in function
`incase` - checks for errors in the code
`occurred` - executing if error occurred

## Functions
`rand` - Returns random number from x to y, takes 2 arguments

## How to install
1. Go to newest version branch
2. Download ZIP file and unpack this in single directory
3. Launch main.py

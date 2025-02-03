
# FUSH
FUSH - programming language based on Python. ade as simple as possible for beginners, without brackets, quotes and even colon.
## Syntaxis
There's some code examples on FUSH

Calculator:
```
loop
    output Write a number №1
    input a
    var num a a
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

Clicker:
```
var balance 0
var one_click 1
loop
    outputf type something to tap <balance>$
    outputf your income <one_click>$/click
    output 0 - upgrade 10$, 1 - upgrade 100$, 2 - upgrade 1000$
    input filler

    is filler = 0 str
        is balance >= 10
            var balance balance-10
            var one_click one_click+1
    also filler = 1 str
        is balance >= 100
            var balance balance-100
            var one_click one_click+10
    also filler = 2 str
        is balance >= 1000
            var balance balance-1000
            var one_click one_click+100
    also filler !=  str
        var balance balance+one_click

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
`back` - returns a value in function\
`incase` - checks for errors in the code\
`occurred` - executing if error occurred

## Functions
`rand` - returns random number from x to y, takes 2 arguments\
`lenght` - returns lenght of string\
`lowercase` - returns string in lower case\
`uppercase` - returns string in upper case\
`root` - returns square root of number. Takes 1 argument\
`fact` - returns factorial of number. Takes 1 argument\
`wait` - waiting for a certain amount of time in ms. Takes 1 argument\
`add` - adds element at the end of arrive\
`addstr` - adds string element at the end of arrive\
`write` - changes an element in arrive by index\
`writestr` - changes an element in arrive to sring by index\
`remove` - removes element in arrive by index\
`read` - reads value in arrive by index\
`reverse` - reverses an arrive\
`unique` - removes dublicates and sort arrive\
`sort` - sotrs an arrive\
`unix` - returns current time in unix format\
`time` - converts unix time to normal format\
`choose` - returns random element from arrive\
`play` - plays a sound from path\


## How to install
1. Go to the main branch
2. Download ZIP file and unpack this in single directory
3. If you don't install playsound type this in cmd:
   `pip install playsound`  
4. Launch main.py

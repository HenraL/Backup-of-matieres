# Why learn C

Basic\
very efficient\
can gives a better understanding of programming languages.\
Pool= good moment, new friends everyday\
try to work with diff. peop. ev.day = sit down at a different table every day\
Don't always work with your friends\

## After the pool
Learn diff language (Unix, Python, assembly, etc...)\
C will be in all projects (and mini projects)\

## What is "The coding style"

Standard way of coding
document on how to code as epitech expects it
Nigthmare cause +++ stuff to look at

to many coding style errors = 1

universal style applying = esear to read.


## Machine structure

Basic explanation:\
RAM (Random access memory) = bytes (1=8 bits each)
1 byte goes from 0 to 255

CPU interracts with the RAM

RAM = data\
CPU = comparing\
CPU = Microprocessor

Intputs/Outputs (I/O) = additional elements (keyboard, screen, hard drive, etc...) that communicate with the system.


C = translator between your code and assembly code.

Program interracts with different elements of the system (ex: RAM)

## C data Types
Types (char, short, int, long, long long  [depreciated]) = allows to define the type of an object

Pointer (*) = contains the link to a ressource (ex: an obj)

## syntax
data types = templates, a way a computer understands values in a memory.

declare a variable = type name;

type (ex: int)

unsigned int varName = can only contain positive numbers

When defining a varName = use a specific style and name

## Arrays...

fixed list\
declaration = type name[nb];

Ex:\
int my_tab[42]; //declaration of 42 contignuous int in memory\
char array_double[21][84];


Array <=> excel sheet

## ...and structures

A structure is an assembly of any data type elements in  memory and is declared in the following way

Syntax:
struct name_structure\
{\
    type name_var;\
    ...\
};\
...\
structure name_structure name;

Ex:
//Create a new type called struct s_my_structure
struct s_my_structure\
{\
    int a;\
    char b[21];\
};\
//Create an object in memory that struct s_my_structure type\
struct s_my_structure ;

### In epitech:
type a,b,c = works in C but forbidden in Epitech.

Numerous array/structure combinations are possible:
struct s_my_structure toto[42];
struct s_a;\
{\
    struct s_b titi[2];\
    struct s_a*next;\
    long 1;\
};

## A C Program
function = simple tasks that take data In, treats it, and sometimes spits it out

return_type function_name(type1 param1, type2 param2, ...);\
FUNCTION'S BLOCK

int my_function(char a, int b, long c);\
FUNCTION'S BLOCK

functions can be seen like machines of mathematical functions.

## How to build a block

{\
    //Declarative part at the top (the types [int, array, long, ...])

    //Imperative part (computing, imparative part)
}


Ex:\
int my_function(char a, in b, long c)\
{\
    char var_1;\
    int tab_1[84]

    //Imperative part
}

## When a program has different functions:
main = entry point [convention, mandatory] to start the program.\
main can call and use other functions in the program.\
once main is finished, the program is finished.\
If main is not present the compiler will not compile anything and/or return an error.


THIS DOES NOT STOP OTHER FUNCTIONS FROM BEEING DECLARED OR CALLED OUTSIDE OF THE MAIN FUNCTION AS LONG AS THE FIRST CALL COMES FROM THE FUNCTION main .

## Instructions
+++ type of things that can be done in a line
* affectations int c; int b; int a=b=c=3; (forbidden in Epitech); int a=3;int b=3;int c=3; (allowed)
* binary operations:
  * OR :          |
  * AND:          &
  * NO:           ~
  * OR exclusive: ^
  * SHIFT left:   <<
  * SHIFT right:  >>
* logical operators:
  * || or
  * && and
  * !  NOT
  * Ex:
    * expression || expression
    * expression && expression
    * !expression
    * returns bool.

  * *=
  * +=
  * ++
  * --
* comparisons 
  * (< <= >= > == !=)
    * < smaler than
    * > greater than
    * <= smaller or equivalent than
  * to compare an expression:
    * expression compare expression
  * (3+b)%4 == toto-21*2
* basics
* 

## Optimisation
name_variable++\
++name_variable

name_variable--\
--name_variable

order -- a or a ++ changes the order of the operation.

## ... and various expressions

sizeof(type/var_name):
* sizeof(int)
* sizeof(variable_name)

&name_variable is an expression whose points to a pointer

## The arithmetic of pointers

int tab[3]\
int *p;\
p=&(tab[0])

## Controls structure: if ...
if (expression)\
    imperative part

if (expression)\
    imperative part\
else:\
    imperative part

## ... while and return
The wile structure\
while (expression)\
    imperative part

The return function\
return (expression);\
retrun;

do 
    imperative part\
while (expression);

for (type exp1; cond exp2; do exp3){\
    imperative part\
}
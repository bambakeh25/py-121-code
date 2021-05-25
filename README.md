# py-121-code
Code from lessons as python files 


## In Class Exercises / HW 

### Compound Interest

Write a function that computes the compound interest of an intial investment, using principle rate and time  

Formula for compound interest:
A = P(1 + R/100) t 

Where, 
A is amount 
P is principle amount 
R is the rate and 
T is the time span.


Part 2:
Convert function to a method of a class i.e. (class Finances, calc_compound_interest)


### ASCII Calculator 
ASCII (American Standard Code for Information Interchange), is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.

There is a function for finding the ascii value of a character here:
https://docs.python.org/3/library/functions.html

Write a function that asks the user for input, and then computes the sum of all the ascii values of the characters. 

- "hello" -> 104 + 101 + 108 + 108 + 111 = 532 


Part 2:
Given a list of words (from user input) determine which word has the highest ascii value.  



### Ambiguous Dates
Dates can be written differently depending where you are in the world
05.05.2021 (the fifth of may 2021)
03.05.2021 (the third of may 2021 -> Europe, the 5th of march 2021 -> US)
05.03.2021 (the fifth of march 2021 -> Europe, the 3th of may 2021 -> US)


Sample Inputs (strings '05.05.2021'):
- 05.05.2021 -> non-ambiguous
- 03.05.2021 -> ambiguous
- 05.03.2021 -> ambiguous 


1) Write a function that detects if a date, written in the format NN.NN.NNNN where n is a digit [0-9] is ambiguous 
2) save all the dates of the year that are ambiguous and print to user   
3) Extra: write a function that converts the format NN.NN.NNNN to a date such as "the 5th of May, 2021" (HINT: Use string formatting, and lists of strings) 

### Double Letters
Analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.

Sample Inputs:
- hello -> True
- nono ->  False 
- sunday -> False
- racecar -> False

### Converting Numpy Array Datatypes
The following list represents tempuratures in New York 

tempuratures = ['76.5', '79.1','80.3', '78.3','75.6', '73.2']

1. Write a function that takes a string list of tempuratures 
2. Convert that string list into a list of floats and calculate the average

###### Hints:
- use .astype()

 

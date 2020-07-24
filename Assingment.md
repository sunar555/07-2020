 # ASSIGNMENTS
## TASK ONE: NUMBERS AND VARIABLES
####  1. Create three variables in a single a line and assign different values to them
and make sure their data types are different. Like one is int, another one is float and
the last one is a string.
```a, b, c = 2, 5.5,"Hello world"```
####  2. Create a variable of value type complex and swap it with another variable
whose value is an integer.
```x= 5```
```y= 3+5j```
```x, y= y,x```
```print(x)```
```print(y)```

#### 3. Swap two numbers using the third variable as the result name and do the same task without using any third variable.
```x,y=2,3```
```z=x```
```x=y``
```y=z```

```x,y=3,4```
```x,y=y,x```
#### 4. Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
##### python 2.x
```username = raw_input("Enter username:")```
##### python 3.x
```username = input("Enter username:")```
#### 5. Write a program to complete the task given below:

#### ● Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
```a=input("enter number between 1 to 10 : ")```
```b=input("enter another number between 1 to 10 : ")```
```z=int(a)+int(b)```
```print(z)```

#### ● Use z for adding 30 into it and print the final result by using variable result.
```result=z+30```
```print(result)```
#### 6. Write a program to check the data type of the entered values. HINT: Printed output should say - The input value data type is: int/float/string/etc
```type()```
#### 7. Create Variable using CamelCase, LadderCase and UPPERCASE. (Refer: https://capitalizemytitle.com/camel-case/) - Variable Conventions to write
##### camelCase
```firstName = "vishal"```
##### LadderCase
```FirstName = "vishal"```
##### CAPITALIZED
```FIRSTNAME = "vishal"```

#### 8. If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value. If Yes then Why?
##### Yes, the value will be changed because in the python the assinged variable is programmed to take most recent value.
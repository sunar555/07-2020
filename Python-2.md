###### TASK TWO: OPERATORS AND DECISION MAKING STATEMENTS
###### 1. Write a program in Python to perform the following operation:
###### ● If a number is divisible by 3 it should print “Consultadd” as a string
###### ● If a number is divisible by 5 it should print “c” as a string
###### ● If a number is divisible by both 3 and 5 its should print “Consultadd Python Training” as a string.  
```python
x = int(input("Enter any number ")) 
if x%3 ==0 and x%5 ==0: 
  print("Consultadd Python Training")
if x%3 ==0: 
  print("Consultadd")  
if x%5 ==0:  
  print("c")
```  

##### 2. Write a program in Python to perform the following operator based task:
##### ● Ask the user to choose the following option first:
##### ○ If User Enter 1 - Addition
##### ○ If User Enter 2 - Subtraction
##### ○ If User Enter 3 - Division
##### ○ If USer Enter 4 - Multiplication
##### ○ If User Enter 5 - Average
##### ● Ask the user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
##### ● Ask the user to enter two more numbers as first1 and second2 for calculating the average as soon as the user chooses an option 5.
##### ● In the end, if the answer of any operation is Negative print a statement saying “Zsa”
```python
query = """Enter mathematic operation you want to Perform\n
1 for Addition\n
2 for Subtraction\n
3 for Division\n
4 for Multiplication\n
5 for Average\n
"""
x = int(input(query))
if x in(1,2,3,4,5):
  first_number = int(input("Enter first number: "))
  second_number = int(input("Enter second number: "))
  if x==1:
    result = first_number+second_number
    print("Sum of your numbers is {}".format(result))
  if x==2:
    result = first_number-second_number
    print("Difference of your numbers is {}".format(result))
  if x==3:
    result = first_number/second_number
    print("Result from division is {}".format(result))
  if x==4:
    result = first_number*second_number
    print("Product of your numbers is {}".format(result))
  if x == 5:
    first1 = int(input("Enter first1 number: "))
    second2 = int(input("Enter second2 number: "))
    result = (first_number+second_number+first1+second2)/4
    print("Average of your numbers is {}".format(result))
  if result < 0:
    print("Zsa")
else:
  print("Invalid entry, Please re-run program and choose valid entry")
```




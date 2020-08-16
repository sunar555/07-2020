#### TASK SIX: FILE HANDLING AND EXCEPTION HANDLING 

#### 1. Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError 

try:
    x = ['a',2, Hello, 6,5.5]
except: SyntaxError
    print('your code has syntax error')

####2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an 
# exception and ask them to enter the name again. Make sure to use read only mode.  

import sys
d = 'TASK-6.py'
try:
  filename = input("Enter file name ?")
  fh = open(filename, 'r',  sys.argv)
except:
  while d != filename:
      print('Incorrect file name')
      print("Try again")
      filename = input("Enter file name ?")
      continue

#### 3. Write a program to handle an error if the user entered the number more than four digits it should return “Please length is 
# too short/long !!! Please provide only four digits”  

try:
  x= int(input('Enter a number with less than four digit '))
  if x > 9999 or x < 1000:
    raise Exception
except:
  print("Please length is too short/long !!! Please provide only four digits")

#### 4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the 
# password is incorrect give chance to enter it again but it should not be more than 3 times. 
user = input("Enter user name : ")
pwd = input("Enter password : ")
re_pass = input("Retype password : ")
count = 0
while count <3:
    if pwd != re_pass:
        re_pass = input("Password didn't match, Enter again : ")
    count+=1


#### 5. https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept. 

The finally keyword is used in try...except blocks. It defines a block of code to run when the try...except...else block is final.
The finally block will be executed no matter if the try block raises an error or not.
This can be useful to close objects and clean up resources.

try:
  x > 5
except:
  print("wrong")
else:
  print("right")
finally:
  print("finished")


The raise keyword is used to raise an exception. You can define what kind of error to raise, and the text to print to the user.

x = "python"

if not type(x) is int:
  raise TypeError("Only integers are allowed")


#### 6. Read any file using Python File handling concept and return only the even length string from the doc.txt file. 
#### Consider the content as:  

Hello I am a file  

Where you need to return the data string  

Which is of even length  

Make sure you return the content in  

The same link as it is present.

x = open('doc.txt', "w")
x.write('''Hello I am a file\nWhere you need to return the data string\n
Which is of even length\nMake sure you return the content in\nThe same link as it is present.''')


x = open('doc.txt')
z=x.read()
y =z.split('\n')
for sentence in y:
  if len(sentence) % 2 == 0:
    print(sentence)


TASK FOUR: FUNCTION 

 #### 1. Write a program using function USINto reverse a string. 
#### Sample data: “1234abcd” 
#### Expected Output: “dcba4321” 

def reverse(word):
  return word[::-1]

#### 2. Write a function that accepts a string and calculate the number of uppercase letters and lowercase letters. 
#### Expected Output: 
#### No. of Upper case characters : 3 
#### No. of Lower case Characters : 12 

def check_letter(word):
  lower=upper=0
  for i in x:
    if i.isupper():
      upper+=1
    if i.islower():
      lower+=1
    else:
      pass
  return lower,upper

x= input("Enter any string ")
lower,upper = check_letter(x)
print("Lower : "+str(lower))
print("Upper : "+str(upper))

#### 3. Create a function that takes a list and returns a new list with unique elements of the first list. 

def unique_list(y):
  x = []
  for a in y:
    if a not in x:
      x.append(a)
  return x
print(unique_list([1,2,2,3,3,4,4,4,5])) 

#### 4. Write a program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated 
# sequence after sorting them alphabetically. 

def sort_my_str(word):
  a= word.split("-")
  a.sort()
  print("-".join(a))

#### 5. Write a program that accepts a sequence of lines as input and prints the lines after making all characters in the sentence 
# capitalized. 
####Sample input: 

 Hello world 

Practice makes perfect 

#### Expected Output: 

HELLO WORLD 

PRACTICE MAKES PERFECT 

def capitalized(phrase):
  c = phrase.split('\n')
  d = [x.upper() for x in c]
  print('\n'.join(d))

 #### 6.Define a function that can receive two integral numbers in string form and compute their sum and print it in console. 

def get_sum(num1,num2):
  print("Sum : "+str(int(num1)+int(num2)))
 
 #### 7.Define a function that can accept two strings as input and print the string with maximum length in console. If two strings 
 # have the same length, then the function should print all strings line by line. 

def findMax(a,b):
  if len(a) > len(b):
    print(a)
  elif len(b)>len (a):
    print(b)
  else:
    print(a+'\n'+b)
  
findMax(input('Enter first string: '),input('Enter second string: '))
 
 #### 8.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20. 

#method-1
def generate_tuple():
  a=[]
  for x in range(2,20):
    a.append(x*x)
  return tuple(a)

#Method-2
def generate_tuple():
  a=tuple
  for x in range(2,20):
    a+=(x*x,)
  return a
 
 #### 9. Write a function called showNumbers that takes a parameter called limit. It should print all the numbers between 0 and 
 # limit with a label to identify the even and odd numbers.  

Example: If the limit is 3 , it should print: 

0 EVEN 

1 ODD 

2 EVEN 

3 ODD 

 def showNumbers(limit):
  for i in range(0,limit +1):
    if i % 2 == 0:
      print(str(i) + " : " +'EVEN')
    else:
      print(str(i) + " : "+ 'ODD')
  return(10)

#### 10. Write a program which can filter() to make a list whose elements are even number between 1 and 20 ( both included) 

l = range(1,21)
result = filter(lambda x:(x % 2 == 0),l)
print(list(result))

#### 11. Write a program which can map() and filter() to make a list whose elements are square of even number in 
# [1,2,3,4,5,6,7,8,9,10] 

#### Hints: Use map() to generate a list. 
####Use filter() to filter elements of a list 
#### Use lambda to define anonymous functions 

num = [1,2,3,4,5,6,7,8,9,10]
 
eve_num = map(lambda x: x**2, filter(lambda   x: x%2==0, num))
 
print((list)(eve_num))
 

#### 12. Write a function to compute 5/0 and use try/except to catch the exceptions 

def compute():
    try:
        x = 5/0
    except Exception as e
        print("Exception occured \n {}".format(e))

#### 13. Flatten the list [[1,2,3].,[4,5],[6,7,8]] into [1,2,3,4,5,6,7,8] using reduce 
#### Goal : Turn [1,2,3,4,5,6,7] to 1234567  

from functools import reduce
li= [[1,2,3],[4,5],[6,7,8]]
addition = reduce(lambda x,y: x+y, li)
print(addition)
for i in addition:
    print( i, end = '')
 
 
 #### 14.  

(i) def foo(): 

    try: 

        return 1 

    finally: 

        return 2 

k = foo() 

print(k) 

 #### Answer:  2
 
 ii) def a(): 

    try: 

        f(x, 4) 

    finally: 

        print('after f') 

    print('after f?') 

a() 

#### Answer: 
after f
Traceback (most recent call last):
  File "main.py", line 13, in <module>
    a() 
  File "main.py", line 5, in a
    f(x, 4) 
NameError: name 'f' is not defined
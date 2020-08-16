#### 1. Write a program to Python find the values which is not divisible 3 but is should be a multiple of 7. Make sure to use only 
# higher order function. 

num= [x for x in range(100) if x%3!=0 if x%7==0]
print(num)

#### 2. Write a program in Python to  multiple the element of list by itself using a traditional function and pass the function to
#  map to complete the operation. 

def multiply_number(n):
  return n*n

my_list = [1,2,3,4,5]
doubled_list = map(multiply_number,my_list)
print(list(doubled_list))

#### 3. Write a program to Python find out the character in a string which is uppercase using list comprehension. 

str = 'United States of America'
res = [i for i in str if i.isupper()]
print(res)

####  4. Write a program to construct a dictionary from the two lists containing the names of students and their corresponding 
# subjects. The dictionary should maps the students with their respective subjects. Let’s see how to do this using for loops and 
# dictionary comprehension. HINT-Use Zip function also 

#### Student = ['Smit', 'Jaya', 'Rayyan'] 

#### capital = ['CSE', 'Networking', 'Operating System'] 

y = {key:value for (key,value) in zip(Student, capital)}
print(y)
 

#### 5.  Learn More about Yield, next and Generators 
A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield 
keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. 
Generator functions return a generator object. Generator objects are used either by calling the next method on the generator object 
or using the generator object in a “for in” loop.

The yield statement is only used when defining a generator function, and is only used in the body of the generator function. Using 
a yield statement in a function definition is sufficient to cause that definition to create a generator function instead of a normal 
function.
The next() function returns the next item from the iterator. The syntax of next() is: next(iterator, default)

#### 6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training” 

x = "Consultadd Traning"
def reverse(word):
  n=-1
  for z in x:
    y = (x[n])
    n=n-1
    yield(y)

a = reverse(x)


print(next(a))
print(next(a))
print(next(a))
print(next(a))

#### 7. Write any example on decorators. 

def my_func(func):
  def demo_func():
    print('Hello')
    func()
  return demo_func

@my_func
def myFunc():
  print('How are you!')

myFunc()
 
#### 8. Learn about What is FRONT END and its Technologies and Tools 
Front End is a set of technologies that are used in developing the user interface of web applications and webpages. With the help 
of front-end technologies, developers create the design, structure, animation, and everything that you see on the screen while 
opening up a website, web application, or mobile app. The prime goal of front-end development tools and technologies is to help 
mobile and web developers increase their efficiency and make the development process quicker, simpler, and better.
#### Make sure to mention at least 5 top notch technologies of Frontend. 
Django, React, Javascript, HTML, CSS, jQuery.
#### Also mentioned the name of companies using those 5 technologies individually 
Facebook, Apple, Netflix, Instagram and Pinterest.
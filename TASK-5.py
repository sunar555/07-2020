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

#### 6. Write a program in Python using generators to reverse the string. Input String = “Consultadd Training” 

x = "testinghgjghgghjgjhgjh"
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
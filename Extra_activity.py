

#### 1. Create a list of the 10 elements of four different types of Data Types like int, string, complex and float. 

list= [1,9.5,'A',2+3j,'Nikola', 6.7,9, 5+4j, 'Vienna',11  ]

#### 2. Create a list of size 5 and execute the slicing structure  
My_list= ['a','b','c','d','e']
My_list[:]
['a', 'b', 'c', 'd', 'e']

My_list= ['a','b','c','d','e']
My_list[1:4]
['b', 'c', 'd']

My_list= ['a','b','c','d','e']
My_list[:3]
['a', 'b', 'c']

My_list= ['a','b','c','d','e']
My_list[2:]
['c', 'd', 'e']

My_list= ['a','b','c','d','e']
My_list[1:4:2]
['b', 'd']

My_list= ['a','b','c','d','e']
>>> My_list[::-1]
['e', 'd', 'c', 'b', 'a']

#### 3. Create a list of given structure and run  
#### x=[100,200,300,400,500,[1,2,3,4,5,[10,20,30,40,50],6,7,8,9],600,700,800] 

#### Access list [1, 2, 3, 4] 
a=x[5][:5]
print(a)

#### Access list [600,  700] 
b=x[6:8]
print(b)

#### Access list [100, 300, 500, 600, 800] 
c=x[0::2]
print(c)

#### Access list [[800, 700, 600, [1, 2, 3, 4, 5, [10, 20, 30, 40, 50], 6, 7, 8, 9], 500, 400, 300, 200, 100]] 
d=x[::-1]
print(d)

#### Access list [10] 
e=x[10]
print(e)---list index is out of range.

#### Access list [ ] 
Invalid syntax
#### 4. Create a list of thousand number using range and xrange and see the difference between each other. 

#Range
x = [y for y in range(0,1000)]
print(x)

--The range type() is
type(x)
<type 'list'>

--range() consumes more memory than xrange()
--Generate all item at one.
--return list object

#xrange
y = [x for x in xrange(0,1000)]
print(y)

--The xrange type() is 
type(x)
<type 'xrange'>

--xrange() consumes more memory than xrange()
--Generate one item at a time.
--return integer object

#### 5. How Tuple is beneficial as compare to the list? 
we can use Tuple as a dictionary keys because Tuple are immutable and we cannot use list becuase it is mutable. it is also 
beneficial for the security because of immutibility.

#### 6. Write a program in Python to iterate through the list of numbers in the range of 1,100 and print the number which is 
# divisible by 3 and a multiple of 2. 
c = []
for y in range(1,100):
  if y%3==0 and y%2==0:
    c.append(y)
print(c)

### 7. Write a program in Python to reverse a string and print only the vowel alphabet if exist in the string with their index. 
a = "Hello, welcome to the python training "
b=a[::-1]
count = 0
for letter in b:
  if letter in ('a','e','i','o','u'):
    print(count ,letter)
  count+=1

#### 8. Write a program in Python to iterate through the string “hello my name is abcde” and print the string which has even 
# length of word. 
def Words(s): 
  s = s.split(' ')  
  for word in s:  
    if len(word)%2==0: 
      print(word)  
s = "hello my name is abcd" 
Words(s)  
 
 #### 9. Write a program in python to print the pair of numbers whose sum is equal to result number that is let's say 8. 
#### x=[1,2,3,4,5,6,7,8,9,-1] 
x=[1,2,3,4,5,6,7,8,9,-1] 
a =[]
for y in x:
  for z in x:
    if (y+z == 8):
      
      a.append((y,z))
print(a)

#### 10. Write a program in Python to complete the following task: 
#### Create two different list as in even_list and odd_list 
#### Ask user to enter the number in the range of 1,50 and make sure if the entered number is even append it to the even_list and if 
#### the entered number is odd append it to the odd list. 
#### Keep that in mind you can only add 5 items in each list 
#### Make sure once you entered the total 5 element calculate the sum of the list and return the maximum out of the list. 

even = []
odd = []
count_even = 0
count_odd = 0
while count_even <5 or count_odd <5:
  x = int(input("Enter number 1 to 50: "))
  if x % 2 == 0:
    if count_even <= 5:
      even.append(x)
      count_even+=1
  else:
    if count_odd <= 5:
      odd.append(x)
      count_odd+=1
print("Sum of even numbers = {}".format(sum(even)))
print("Max of even numbers = {}".format(max(even)))
print("Sum of odd numbers = {}".format(sum(odd)))
print("Max of odd numbers = {}".format(max(odd)))

#### 11. Write a program to find out the occurrence of a specific word from an alphanumeric statement. Example: 12abcbacbaba344ab   
#### Output: a=5 b=5 c=2 make sure you should avoid the numbers in you logic 
a=[]
for x in b:
  if x.isalpha():
    a.append(x)
#print(a)
output =[]
for y in a:
  count = 0
  for z in a:
    if y==z:
      letter = y
      count= count+1
  if (y+'='+str(count)) not in output:
    output.append(y+'='+str(count)) 
print(' '.join(output))
 
 #### 12.Generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10). 
t=(1,2,3,4,5,6,7,8,9,10)
for i in t:
  if i % 2 == 0:
    print(i)
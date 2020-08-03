#### 1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float. 
```python
My_list= [2,3.5,'Apple',5+3j,'Tesla', 5.9,6, 3+2j, 'Vishal',10  ]

#### 2. Create a list of size 5 and execute the slicing structure. 

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[:]
['apple', 'orange', 'grapes', 'mango', 'berries']
My_list= ['apple', 'orange', 'grapes', 'mango','berries']
>>> My_list[1:4]
['orange', 'grapes', 'mango']
My_list= ['apple', 'orange', 'grapes', 'mango','berries']
>>> My_list[:3]
['apple', 'orange', 'grapes']
My_list= ['apple', 'orange', 'grapes', 'mango','berries']
>>> My_list[2:]
['grapes', 'mango', 'berries']
>>> My_list= ['apple', 'orange', 'grapes', 'mango','berries']
>>> My_list[1:4:2]
['orange', 'mango']
>>> My_list= ['apple', 'orange', 'grapes', 'mango','berries']
>>> My_list[::-1]
['berries', 'mango', 'grapes', 'orange', 'apple']

#### 3. Write a program to get the sum and multiply of all the items in a given list. 
## Multiplication
## Method-1

x=[10,20,30,40,50]
for i in range(len(x)):
  x[i]=x[i]*2
print(x)

##Method-2
x=[1,2,3,4,5]
y=[i*2 for i in x]
print(y)

## Addition
x=[1,2,3,4,5]
total=sum(x)
print(total)

#### 4.   Find the largest and smallest number from a given list. 
# largest number
list=[5,9,32,78,20,33,68]
max(list)

# smallest number
list=[5,9,32,78,20,33,68]
min(list)

#### 5. Create a new list which contains the specified numbers after removing the even numbers from a predefined list.  
list=[4,33,18,67,89,8,44,59,17,7]
## method-1
list=[4,33,18,67,89,8,44,59,17,7]
list2=[]
for i in list:
  if i % 2!=0:
    list2.append(i)
print(list2)

## Method-2
list=[4,33,18,67,89,8,44,59,17,7]
list2=[x for x in list if x%2!=0]
print(list2)

#### 6. Create a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included). 
l = list()
for i in range(1,31):
  l.append(i**2)
print(l[:5]+l[-5:])
	
#### 7. Write a program to replace the last element in a list with another list. 
Sample_data= [[1,3,5,7,9,10],[2,4,6,8]] 
y=Sample_data[0][:-1]+Sample_data[1]
print(y)

 

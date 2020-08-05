#### 1. Create a list of the 10 elements of four different types of Data Type like int, string, complex and float. 
```python
My_list= [2,3.5,'Apple',5+3j,'Tesla', 5.9,6, 3+2j, 'Vishal',10  ]

#### 2. Create a list of size 5 and execute the slicing structure. 

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[:]
['apple', 'orange', 'grapes', 'mango', 'berries']

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[1:4]
['orange', 'grapes', 'mango']

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[:3]
['apple', 'orange', 'grapes']

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[2:]
['grapes', 'mango', 'berries']

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[1:4:2]
['orange', 'mango']

My_list= ['apple', 'orange', 'grapes', 'mango','berries']
My_list[::-1]
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

 #### 8. Create a new dictionary by concatenating the following two dictionaries: 
a={1:10,2:20} 
b={3:30,4:40} 
Expected Result: {1:10,2:20,3:30,4:40} 

a={1:10,2:20} 
b={3:30,4:40} 
c= {**a,**b}
print(c)
#### 9. Create a dictionary that contains a number (between 1 and n) in the form(x,x*x). 
Sample data (n=5) 
Expected Output: {1:1,2:4,3:9,4:16,5:25} 

n=5
d = {}
for x in range(1,n+1):
    d[x]=x*x
print(d) 
#### 10. Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 

34,67,55,33,12,98 

The output should be: 

[‘34’,’67’,’55’,’33’,’12’,’98’] 

(‘34’,’67’,’55’,’33’,’12’,’98’) 

values = input("Input some comma seprated numbers : ")
list = values.split(",")
tuple = tuple(list)
print('List : ',list)
print('Tuple : ',tuple)
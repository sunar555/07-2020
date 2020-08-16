#### 1. Write a program that calculates and prints the value according to the given formula: 

# Q= Square root of [(2*C*D)/H] 
# Following are the fixed values of C and H: 
# C is 50. H is 30. 
# D is the variable whose values should be input to your program in a comma-separated sequence. 

import math

C= 50
H = 30
Ds = []
result =[]
Dv=input("enter the value of D\n")
Ds=Dv.split(",")
Ds = [int(i) for i in Ds]
i=0
l = len(Ds)
while(i<l):
    Q = round(math.sqrt((2*C*Ds[i])/H))
    result. append(Q)
    i+=1
print("output=",result)

#### 2. Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. 
# Both classes have an area function which can print the area of the shape where Shape’s area is 0 by default. 

class Shape():
  class Square():
    def __init__(self,x):
      x.self = 0
      return(x*x)

    def area(length):
      return length*length
    
y = Shape.Square.area(5)
print(y)

#### 3. Create a class to find the three elements that sum to zero from a set of n real numbers. 
# Input array: [-25,-10,-7,-3,2,4,8,10] 
# Output: [[-10,2,8],[-7,-3,10]] 

class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

#### 4. What is the output of the following code? Explain your answer as well. 

class Test: 

    def __init__(self): 

        self.x = 0 

class Derived_Test(Test): 

    def __init__(self): 

        self.y = 1 

def main(): 

    b = Derived_Test() 

    print(b.x,b.y) 

main() 

```ANS: AttributeError```

class A: 

    def __init__(self, x= 1): 

        self.x = x 

class der(A): 

    def __init__(self,y = 2): 

        super().__init__() 

        self.y = y 

def main(): 

    obj = der() 

    print(obj.x, obj.y) 

main()) 

```ANS:   1 2```

class A: 

    def __init__(self,x): 

        self.x = x 

    def count(self,x): 

        self.x = self.x+1 

class B(A): 

    def __init__(self, y=0): 

        A.__init__(self, 3) 

        self.y = y 

    def count(self): 

        self.y += 1      

def main(): 

    obj = B() 

    obj.count() 

    print(obj.x, obj.y) 

main() 

```ANS: 3 1```

  

class A: 

    def __init__(self): 

        self.multiply(15) 

        print(self.i) 

  

    def multiply(self, i): 

        self.i = 4 * i; 

class B(A): 

    def __init__(self): 

        super().__init__() 

  

    def multiply(self, i): 

        self.i = 2 * i; 

obj = B() 

```ANS: 30```

#### 5. Create a Time class and initialize it with hours and minutes. 
#### Make a method addTime which should take two time object and add them. E.g.- (2 hour and 50 min)+(1 hr and 20 min) is 
# (4 hr and 10 min) 
#### Make a method displayTime which should print the time. Make a method DisplayMinute which should display the total minutes in 
# the Time. E.g.- (1 hr 2 min) should display 62 minute. 

class Time():
  hour = int()
  minutes = int()
  def addtime(time1,time2):
    return time1[0]+time2[0],time1[1]+time2[1]

  def displayTime(mytime):
    x = mytime[0] 
    y = mytime[1] 
    z = y%60 
    a= (y-z)/60 
    return x+a,z 

  def displayMinutes(mytime):
    x = mytime[0]
    y = mytime[1]
    z = x*60+y
    return ('{} minutes'.format(z))

b = list(Time.addtime([3,50],[4,20]))
c = list(Time.displayTime(b))
print('{} hours {} and minutes'.format(c[0],c[1]))

d = Time.displayMinutes(b)
print(d)

  
#### 6.  Write a Person class with an instance variable, , and a constructor that takes an integer, , as a parameter. The 
# constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , 
# the constructor should set  to  and print Age is not valid, setting age to 0.. In addition, you must write the following instance
#  methods: 

yearPasses() should increase the  instance variable by . 

amIOld()  should perform the following conditional actions: 

If , print You are young.. 

If  and , print You are a teenager.. 

Otherwise, print You are old..  

Sample Input: 

4 

-1 

10 

16 

18 

Sample Output: 

Age is not valid, setting age to 0. 

You are young. 

You are young. 

  

You are young. 

You are a teenager. 

  

You are a teenager. 

You are old. 

  

You are old. 

You are old. 

class Person:
   def __init__(self,age=0):
       if age < 0:
           print('Invalid age!')
           self.age =0
       else:
           self.age = age
   def amIOld(self):
       if self.age <=13:
           print('You are Young')
       elif self.age > 13 and self.age <=18:
           print('You are Teenager')
       else:
           print('You are old')
   def yearPasses(self):
       print('Year passed')
def main(x):
   p = Person(x)
   p.amIOld()
   p.yearPasses()

while True:
  x=int(input("enter age : "))
  main(x)
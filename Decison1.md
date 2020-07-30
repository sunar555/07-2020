#### 3. Write a program in Python to implement the given flowchart.
```Python 
a=10
b= 20
c= 30
avg= (a+b+c)/3
print("avg=",avg) 
if avg > a and avg > b and avg >c:
  print("avg is higher than a,b,c")
elif avg >a and avg > b:
  print("avg is higher than a,b,c")
elif avg > a and avg > c:
  print("avg is higher than a,c")
elif avg > b and avg > c:
  print("avg is higher than b,c")
elif avg > a:
  print("avg is just higher than a")
elif avg > b:
  print("avg is just higher than b")
elif avg > c:
  print("avg is just higher than c")

#### 4. Write a program in Python to break and continue if the following cases occurs:

#### ● If user enters a negative number just break the loop and print “It’s Over”

#### ● If user enters a positive number just continue in the loop and print “Good Going”
x = 0
while True:
  x = int(input("Enter any number: "))
  if x < 0:
    print("Its over")
    break
  if x> 0:
    print("Good Going")
    continue

#### 5 Write a program in Python which will find all such numbers which are divisible by 7 but are not a multiple of 5, 
# between 2000 and 3200.
#Method 1
for number in range(2000, 3200):
  if number % 7 == 0 and number % 5 != 0:
    print(number)

#Method 2
list_of_number=[]
for number in range(2000, 3200):
  if number % 7 == 0 and number % 5 != 0:
    list_of_number.append(number)
print(list_of_number)

#Method 3
list= [num for num in range(2000, 3200)if num % 7 == 0 and num % 5 != 0]
print(list)

#### 6 What is the output of the following code examples?

# ● x=123

# for i in x:

# print(i)
The output is Error because integer cannot be sliced.

# ● i = 0

# while i < 5:

# print(i)

# i += 1

# if i == 3:

# break

# else:

# print(“error”)
The output is 
0
1
2

# ● count = 0

# while True:

# print(count)

# count += 1

# if count >= 5:

# Break
The optput is
0
1
2
3
4

#### 7 Write a program that prints all the numbers from 0 to 6 except 3 and 6. Expected output: 0 1 2 4 5
for x in range(0,7):
  if x==3 or x==6:
    continue
  print(x)

#### 8 Write a program that accepts a string as an input from user and calculate the number of digits and letters
# Expected output: consul12
# Letters 6
# Digits 2
x= input("Enter any string ")

digit=count = 0

for character in x:
  if character.isalpha():
    count = count +1
  if character.isdigit():
    digit = digit +1

print("Letter: {}".format(count))
print("Digit: {}".format(digit))

#### 9 Read the two parts of the question below:
####● Write a program such that it asks users to “guess the lucky number”. If the correct number is guessed the program stops, 
# otherwise it continues forever.
lucky_number = 12
number= 0
while (number != lucky_number):
  number = int(input("Guess your lucky number : "))
  continue

#### Modify the program so that it asks users whether they want to guess again each time. Use two variables, ‘number’ for the 
# number and ‘answer’ for the answer to the question whether they want to continue guessing. The program stops if the user 
# guesses the correct number or answers “no”. ( The program continues as long as a user has not answered “no” and has not 
# guessed the correct number)
lucky_number = 12
number= 0
while (number != lucky_number):
  number = int(input("Guess your lucky number : "))
  if (number == lucky_number):
    break
  answer = input("Wrong guess, wanna continue ? ")
  if (answer =='no'):
    break
  continue
 
 #### 10 Write a program that asks five times to guess the lucky number. Use a while loop and a counter, such as
# counter=1
# While counter <= 5:
# print(“Type in the”, counter, “number”
# counter=counter+1
# The program asks for five guesses (no matter whether the correct number was guessed or not). If the correct number is guessed, 
# the program outputs “Good guess!”, otherwise it outputs “Try again!”. After the fifth guess it stops and prints “Game over!”.
lucky_number = 12
number= 0
counter =1
while (number != lucky_number and counter <=5):
  number = int(input("Guess your lucky number : "))
  if number == lucky_number:
    print("Good Guess !")
  if counter == 5:
    print("Game over !")
    break
  print("Try Again !")
  counter = counter+1
  continue

#### 11 In the previous question, insert “break” after the “Good guess!” print statement. “break” will terminate the while loop 
# so that users do not have to continue guessing after they found the number. If the user does not guess the number at all, 
# print “Sorry but that was not very successful”.
lucky_number = 12
number= 0
counter =1
while (number != lucky_number and counter <=5):
  number = int(input("Guess your lucky number : "))
  if number == lucky_number:
    print("Good Guess !")
    break
  if counter == 5:
    print("Game over !")
    print("Sorry but that was not very successful")
    break
  print("Try Again !")
  counter = counter+1
  continue
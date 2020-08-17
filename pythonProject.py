a = [
[1,0,0,1,0],
[1,0,1,0,0],
[0,0,1,0,1],
[1,0,1,0,1],
[1,0,1,1,0],
]

b = [1,2,2,2,5]

c =[]
indexOfOne =[]

j = 0
for row in a:
  i=0
  index = []
  count = 0
  
  while i < (len(row)):
    if row[i] == 1:
      index.append(i)
    i+=1
    
  count+=1
  indexOfOne.append(index)
print(indexOfOne)


for row in a:
  counter = 0
  for column in row:
    if column == 1:
      row[counter] =0
      counter+=1
  c.append(counter)
print(c)



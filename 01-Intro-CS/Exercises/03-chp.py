# # # while loop example

n = int(input('choose a no.'))

while n > 0:
  print(n)
  n -= 1

# # # e1
# # # show a sad face when the user 
# # # enteredd the while loop more than 2 times

where = input('you in the woods, choose right or left')
counter = 0

while where == 'right':
  if counter < 2:
    counter += 1
    input('choose right or left again, coz you still in the woods')
  elif counter == 2:
    print(':( times up the lion is here')
    break

if where == 'left':
  print('you got out')

# # e2

for i in range(1,4,1):
  print(i)

for i in range(1,4,2):
  print(i)

for me in range(4,0,-1):
  print("$"*me)

#e4 try to get the sum 12 if the range is 3,5

mysum = 0
start = 3
end = 5 + 1
for i in range(start, end):
  mysum += i
print(mysum)

# finger exercise lecture 3

n = 5
for i in range(n):
  print('hello world')

while n > 0:
  print('hello world while loop')
  n -= 1
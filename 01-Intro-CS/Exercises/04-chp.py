'''
  Finger Exercise Lecture 4
  Assume you are given a positive integer variable named N. 
  Write a piece of Python code that finds the cube root of N. 
  The code prints the cube root if N is a perfect cube 
  or it prints error if N is not a perfect cube. 
  Hint: use a loop that increments a counter—you decide when the counter should stop.
'''

n = 27
answer = 0

while answer**3 < n:
  answer += 1

if answer ** 3 == n:
  print(answer)
else:
  print('error')


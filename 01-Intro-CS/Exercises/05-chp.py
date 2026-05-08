'''
Finger Exercise Lecture 5
Assume you are given a string variable named my_str. 
Write a piece of Python code that prints out a new string containing the even indexed characters of my_str. 
For example, if my_str = "abcdefg" then your code should print out aceg.
'''

my_str = 'abcdefg'

# print(my_str[0])

for i in my_str:
  if my_str.index(i) % 2 == 0:
    print(i)
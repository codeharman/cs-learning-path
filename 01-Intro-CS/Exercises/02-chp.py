# # Finger Exercise Lecture 2
# Assume you are given a variable named number (has a numerical value). Write a piece of Python code that prints out one of the following strings: 

# positive if the variable number is positive
# negative if the variable number is negative
# zero if the variable number is equal to zero

given_num = 0

if given_num > 0:
  print('positive')
elif given_num < 0:
  print('negative')
else:
  print('zero')

# Exercise 1
# what the value of s1 and s2?

b = ':'
c = ')'
s1 = b + 2*c
print(s1)

f = 'a'
g = ' b'
h = '3'

s2 = (f+g)*int(h)
print(s2)

# E2

s = 'ABC d3f ghi'

print(s[3:len(s)-1], s[4:0:-1])


# e3
# write a program that
# asks user for a verb and prints
# "I can __ better than you" * 5 times

word = input("enter the verb: ")
print(f"I can {word} better than you")
print((f'{word} ') *5)

# Guess cube

cube = int(input("Enter the cube num: "))
num = int(input("Enter the num: "))

ans = num + ((cube - num ** 3)/(3 * num**2))

if ans == round(ans):
  print(ans)
else:
  ans = ans
  print(ans)

# guess the secret number

x = 5
y = int(input("Guess the number: "))

if x == y:
  print("you won")
elif y > x:
  print("the number is too high")
else:
  print('the no. is to low')
'''
______
PART 4
______
Write a program that prompts the user to enter two integer inputs. The program prints a string stating if the inputs are both positive, negative, if one of the inputs is zero, or if they have opposite signs. (Hint: this code can be written using only four code blocks, but you may find ways to do this using more.)

Four examples of what should appear on the console when this program runs (note: the test driver is case sensitive):

Enter a number:  3
Enter another number:  7
positive

Enter a number:  -5
Enter another number:  -2
negative

Enter a number:  7
Enter another number:  0
zero

Enter a number:  2
Enter another number:  -2
opposite
'''

#start writing your code below
def findposnegzero():
  num = int(input("enter a number: "))
  if num == 0:
    return 'zero'
  elif num < 0:
    return 'negative'
  else:
    return 'positive'
result1 = findposnegzero()
result2 = findposnegzero()
if (result1 == 'zero') or (result2 == 'zero'):
  print('zero')
elif result1 == result2:
  print(result1)
else:
  print('opposite')
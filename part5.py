'''
______
PART 5
______

Write a program that asks the user to enter the name of a month as a string. The program will then print how many days that month could have in any given year, or print a statement saying that what the user entered is not the name of a month.

(Hint: This should require only four code blocks, but it can be done with 12 or more if you insist. If you are familiar with lists or other container datatypes, you may implement this using those, though it still requires four code blocks)

Four examples of what should appear on the console when the program runs (note: the test driver is case sensitive):

Enter a month:  March
31

Enter a month:  June
30

Enter a month:  February
28 or 29

Enter a month:  Saturday
not a month
'''

#start writing your code below
month = input('Enter a month: ')
months = {'January':'31 days','February':'28 days in a common year and 29 days in leap years','March':'31 days','April':'30 days','May':'31 days','June':'30 days','July':'31 days','August':'31 days','September':'30 days','October':'31 days','November':'30 days','December':'31 days'}
if month in months.keys():
  print(months[month])
else:
  print('not a month haha')
#how many code blocks is this?
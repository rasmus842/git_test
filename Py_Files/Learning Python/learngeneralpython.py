


### PRINT FUNCTIONS AND STRINGS
# In print, '\' is an escape character
#   Multi-line print
# print('''
# text
# ''')



### DATA STRUCTURES

#   TUPLES
#   tuples are immutable. Order is set
# x = 1, 3, 5, 6, 4
# #or
# x = (1, 3, 5, 6, 4)
#   Tuples used for example when returning a value from a function
#   Tuples faster to calculate than lists
#def example_func(a1, b1):
#   blablabla
#   return a1, b1
#a, b = example_func(a, b)

#   LISTS
#   Lists are mutable. Order is set
#y = [1, 3, 5, 6, 4]
#   Getting a specific element from a list or a tuple
#print(x[index1], y[index2]) #etc
#   How to manipulate lists
#   Append another element
#y.append(el)
#   Insert into a specific index
#y.insert(index, el)
#   Remove an element. Removes once beginning from 0th index
#y.remove(el)
#or
#y.remove(y[index])
#   referencing a sliced list. from index1 included to index2 not included
#print(y[index1:index2])
#   how to find the index of an element
#print(y.index[el])
#   finding out how many times the element occurs in the list
#print(y.count(el)) # also can find length aswell with len(y)
#   sorting the list. Numerically or alphabetically
# y.sort()
# y.reverse()

#   MULTI-DIMENSIONAL LISTS
#2D list here. Can make 3D and mixed lists, anything goes
#For math freaks can make and do matrice calcs
# y = [
#     [1, 2],
#     [9, 1],
#     [3, 2]
#     ]
# print[y[row][column]]

#   DICTIONARIERS
# Dict = {} or Dict = {key1 : object1, etc}
# Adding elements or changing them
# Dict[key] = object
# Removing keys
# del Dict[key]


### STATEMENTS



#   TRY and EXCEPT
# try:                  if this code throws out and error, it will keep running the program
#   some code
# except Exception as e:            can do something if the error occurs, for example save the error in e
#   some code
# or except NameError as e: or smth. This will run only if the error was a name error



### FILES INPUT AND OUTPUT



#   INPUT
# x = input('What is your name?: ')
# print('Hello',x)

#   FILES
#   write, read, or append
# f = open('fname.format','w') 
# f.write('text') when writing or appending to it
#   Readlines generates a list
# text = open('fname.format', 'r').readlines 

#   CSV files
#   delimiter in csv is a comma but can be anything
#   when reading data from a csv you get a list of strings
# import csv
# with open('example.csv') as csvfile:
#     readCSV = csv.reader(csvfile, delimiter=',')
#     for row in readCSV:
#         print(row)



### CLASSES AND MODULES



#   CLASSES
# Grouping things together. Behaves like a module
# e.g.
# class calculator:
#    def addition(x, y):
#        print(x + y)
# calculator.addition(3, 4) and it prints 7

#   MODULES
#   Making your own modules
# if you define your functions in a module, then you can write
# if __name__ == '__main__':
#     then do something
# Which is false when the module itself is not the program being ran
# When making your own modules save them to main library.
# Python scripts check modules locally first and then check main library

#   BUILT-IN FUNCTIONS
# help(function or module) - returns a description about the function or module, can just google
# abs(number)
# max(list)
# min(list)
# int(string), float(string), str(anything)
# round(number, digits=None)

#   BUILT-IN MODULES
#   math - math functions
# math.floor(number) - returns the largest integer that is less than number
# math.ceil(number) - return the lowest integer that is larger than number

#   os - for interacting with your operating system
# os.getcwd() - returns the current directory that we are in
# os.mkdir('newDir') - creates a new directory within the current directory
# os.rename('newDir', 'newDir2')
# os.rmdir('newDir')

#   time - for time functions
# time.sleep(seconds) - pause for x amount of seconds

#   statistics - statistics functions. For averaging (mean, median) and deviation (stdev, variance)

#   sys (system) - interacting with the command line.
# sys.stderr.write('text\n') - writes red text in cmd, meant for errors, I suppose
# sys.stderr.flush() - don't know
# sys.stdout.write('text\n') - writes blue text, meant for output I suppose
# sys.argv - returns the file name that we are running at this moment.




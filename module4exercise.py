# Module 4 exercises

# 1. Textbook R5.9
# Indicate the scope of each variable below and 
# trace through the program to determine what's printed

#a = 0 # global! Ends at end of program/file
#b = 5 #global! Ends at end of program/file

#def main():
    #global a, b # global! Ends at end of program/file
    #i = 10# start at 12 ends at 14
    #b = g(i)#starts at 13, ends at 14
    #print(a + b + i) # local variable supersedes global
    
#def f(i):# local starts at 16 ends at 20.
    #n = 0#local starts at 17, ends at 20 
    #while n * n <= i:
        #n = n + 1
    #return n - 1

#def g(a):#starts at 22 ends at 26
    #b = 0#starts at 23 ends at 26
    #for n in range(a):#starts at 24, ends at 26
        #i = f(n) #starts at 25 ends at 26 
        #b = b + i
   #print(i) # this will work! 

# 2. Textbook P5.4
# Write a function called middle that accepts a string as input
# and returns a string which is the middle character if the
# length of the string is odd, and returns a string which is the
# middle 2 characters if the length of the string is even.
'''
middleIndex = int(len(character) / 2) 
   
   if len(character) % 2: #if odd
      return(character[middleIndex])
   else:
      return character[middleIndex - 1] + character[middleIndex]
      
def main():
   userInput = input("Enter a string: ")
   print(middle(userInput))
   

main()
'''
# Write a main function that asks the user for a string,
# calls the middle function, and prints the middle string

    

# 3. Given the following printInfo function that prints 
# a student's information
'''
def printInfo(name, major, minor, age, fulltime, GPA, location):
    print ("Name:", name, "\nMajor:", major, "\nMinor:", minor,
          "\nage:", age, "\nfulltime:", fulltime, "\nGPA", GPA,
          "\nlocation:", location)
printInfo("Logan", "CS", "EE", 18, True, 3.75, "Cupertino")

# call the printInfo function and pass to it your data
def printInfo2(name, major = "CS", minor = "EE", age = 19, fulltime = True, GPA = 3.75, location = "Cupertino"):
    print ("Name:", name, "\nMajor:", major, "\nMinor:", minor,
          "\nage:", age, "\nfulltime:", fulltime, "\nGPA", GPA,
          "\nlocation:", location)
printInfo2("Logan", GPA = 3.88)
#printInfo("Logan", GPA = 3.88)
'''
# Make the printInfo function more user friendly by having 
# "name" the only required argument, and the rest are 
# optional arguments. Call the function printInfo2


# call the printInfo2 function and pass to it your name and whether
# you're a full time or part time student


# what happens if you call printInfo with the 2 arguments above?

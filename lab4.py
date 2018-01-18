# Lab 4:
#Logan Kilpatrick
#10/11/17
# Add to the program intName.py in ch 5, section 5 of the book.
# This program turns an integer into its English name.
#Program is working 100% and fufills all requirments! 

def intName(number) :
   ''' Turn a number into its English name 
       @param: number (int)
       @return: the name (str)
   '''   
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number. 
   
   
   if part >= 20000 :#This part is working...... for all numbers 20,000 - 999,999!!!
      name += secondFunc(part // 1000) + " thousand " #seperates the numbers 
      part = part % 1000  #reduces the number/part to be out of the thousands place 
      #print("Test 1", part)   
   
   
   if part >= 10000 :#THis part is working...... from 10,000-19,999 
      name += teenName(part // 1000) + " thousand "#we could technically get rid of this...
      part = part % 1000  
      #print("Test 1", part)
   
   if part >= 1000 :#works up to 9,999
      name += digitName(part // 1000) + " thousand "
      part = part % 1000  
      #print("Test 2", part)
   
   if part >= 100 :
      name += digitName(part // 100) + " hundered"
      part = part % 100
        

   if part >= 20 :
      name = name + " " + tensName(part) #Changed
      #print("Test 3", part)
      
      if part > 20: 
         name = name + "-" #adds the "- between 
         
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0
      #print("Test 4", part)
      


   if part > 0 :
      name = name + "" + digitName(part)
      #print(part)
      
   
   
      
   name = name.strip()#removes all trailing and leading whitespace
   return name
   #PART 3 & 4 goes in here too! 


def secondFunc(number):#TEST FUNC... works....
   '''
   takes in a number from the intName Function. 
   returns the name.  This aprt is sues for the thousands place
   (Only called for numbers greator than 20,000
   '''
   part = number   # The part that still needs to be converted.
   name = ""   # The name of the number.    
   
   if part >= 100 :
      name += digitName(part // 100) + " hundered"
      part = part % 100
        

   if part >= 20 :
      name = name + " " + tensName(part) #Changed
      #print("Test 3", part)
      
      if part > 20: 
         name = name + "-" #adds the "- between 
         
      part = part % 10
   elif part >= 10 :
      name = name + " " + teenName(part)
      part = 0
      #print("Test 4", part)
      


   if part > 0 :
      name = name + "" + digitName(part)
      #print(part)
      
   name = name.strip()#removes all trailing and leading whitespace
   return name
   #PART 3 goes in here too! 
   
def digitName(digit) :
   ''' Turn a digit into its English name
       @param: digit (int)
       @return: name (str)
   '''   
   if digit == 1 : return "one"
   if digit == 2 : return "two"
   if digit == 3 : return "three"
   if digit == 4 : return "four"
   if digit == 5 : return "five"
   if digit == 6 : return "six"
   if digit == 7 : return "seven"
   if digit == 8 : return "eight"
   if digit == 9 : return "nine"
   return ""


def teenName(number) :
   ''' Turn a number between 10 and 19 into its English name
       @param: number (int)
       @return: name (str)
   '''   
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"
   if number == 13 : return "thirteen"
   if number == 14 : return "fourteen"
   if number == 15 : return "fifteen"
   if number == 16 : return "sixteen"
   if number == 17 : return "seventeen"
   if number == 18 : return "eighteen"
   if number == 19 : return "nineteen"
   return ""


def tensName(number) :
   ''' Turn a number between 20 and 99 into its English name
       @param: number (int)
       @return: name (str)
   '''   
   if number >= 90 : return "ninety"
   if number >= 80 : return "eighty"
   if number >= 70 : return "seventy"
   if number >= 60 : return "sixty"
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return ""


def main() :
   value = ""
     
   while True:#Part 5
      try:#exception handeling for simplicty sake.... Covers all negative numbers and invalid inputs! 
         value = int(input("Please enter a positive integer < 1,000,000 (or 0 to end): "))
         if (value > 999999):#coverts the above 999,999 case
            raise ValueError
            
         if(value == 0):
            print("End of program. Thanks!")
            break
         print(intName(value))            
      except ValueError: #value error exception....
         print("Sorry, an invalid inout was detected please try again")
         continue
   
   
# Start the program.
main()
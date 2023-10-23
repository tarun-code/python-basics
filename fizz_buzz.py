
"""
if the number is divisible by 3 print Fizz    
if the number is divisible by 5 print Buzz
if the number is divisible by 3 and also divisible by 5 print Fizz Buzz

Testcase : 
    21 --> Fizz
    50 --> Buzz
    15 --> Fizz Buzz
    22 --> Invalid Input 
"""

# ***********************************************************
# Practice problem 1 
# ***********************************************************
# Create a game for FIZZ BUZZ and keeping playing with the user untill the user chooses to skip the game


while True:
   
    num=input("Enter a number or exit :" )
    if num!="exit":
       num=int(num)
       if num%3==0 and num%5==0 :
          print(" Fizz buzz")
       elif num%3==0:
          print("fizz")
       elif num%5==0:
          print("buzz")
       else:
          print("invalid input")
    else:
        print("You are out of the game!!!")
        break 
    



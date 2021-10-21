import random

number=random.randint(1,9)
chances=0
print("Enter your guess (between 1-9)")

while chances < 5 : 
     guess=int(input("Enter your guess:-    "))
     if number < guess:
         print("your guess is greater")
     elif number > guess :
         print("your guess is lesser")
     elif number == guess :
         print("CONGRATULATIONS YOU WON !!")
         break
     else:
         print("please enter a valid number !")
     chances+=1

if chances >= 5 :
    print("YOUR CHANCES ARE OVER !!")

      


#Amisha Parmessar
#Date: October 26th, 2023

import random #importing random library
cafeRand = random.randint(1,3) #This generates a random number between 1 and 3
import random
userScale = random.randint(1,5)


userName = input("Hello, what is your name?: ") #This creates a variable called 'userName' and it asks for the user to enter their name. 
print("Nice to meet you " + userName + "!") #This prints out 'Nice to meet you' along with the user's name.
print("I'm chatbot, and I will plan out your day today!") #This prints out 'I'm chatbot, and I will plan out your day today!' after the above statements are run. 

userTime = input("What is your favorite time of the day?: ") #This creates a variable called 'userTime' and it asks for the user to enter their favorite time of the day. 
print("Nice, I love " + userTime + " too!") #This prints out 'Nice, I love' along with the user's favorite time of the day.

weather = input("How is the weather outside?: ") #This creates a variable called 'weather' and it asks for the user to enter the weather outside. 
if weather == "Sunny": #This creates a conditional 'if-statement' that checks if the user's weather is sunny.
    print("Wear sunscreen and stay hydrated!") #This prints out 'Wear sunscreen and stay hydrated!' if the user's weather is sunny.

elif weather == "Cloudy": #This creates a condition 'elif-stament' that checks if the user's weather is cloudy.
    print("Prepare to take a raincoat and umbrella!") #The follwoing print statement is displayed when the above condition is met and when the weather is couldy, the user is suggested to 'Prepare to take a raincoat and umbrella!'. 

elif weather == "Cold": #This creates a condition 'elif-stament' that checks if the user's weather is cold. 
    print("Brrr... take...a...jacket...") #The follwoing print statement is displayed when the above condition is met and when the weather is cold, it suggests the user to take a jacket.


else: #This 'else-statement' is run when the previous conditionals are not met, and when the user's weather is not sunny, cloudy, or cold.
    print("Have a great day") #This prints out 'Have a great day' if the user's weather is not sunny, cloudy, or cold. 


userBreakfast = input("What is your favorite breakfast restaurant?: ") #This creates a variable called 'userBreakfast' and it asks for the user to enter their favorite breakfast restaurant. 
print (userBreakfast +" is a nice place to start the morning and to eat at!") #This prints out 'userBreakfast' along with the user's favorite breakfast restaurant that they inputted. 

userShop = input("Where is your go-to place to shop at when running errands?: ") #This creates a variable called 'userShop' and it asks for the user to enter their go-to place to shop at when running errands.
print("I love to shop at " + userShop + " too.") #This prints out 'I love to shop at' along with the user's go-to place to shop at when running errands. 

userBrunch = input("Do you like brunch time?: ") #This creates a variable called 'userBrunch' and it asks for the user to enter their favorite brunch restaurant.
if (userBrunch == "No" or userBrunch =="no" or userBrunch == "NO"): #This creates a conditional 'if-statement' that checks if the user likes brunch time. 
    print("Ok.") #This prints out 'Ok. How about lunch time?' if the user answers 'No' or 'no' or "NO" to the question 'Do you like brunch time?'. 
elif (userBrunch == "Yes" or userBrunch =="yes" or userBrunch == "YES"):
    print("Great! Let's go to Brunch!") #This prints out 'Great! Let's go to Brunch!' if the user answers 'Yes' or 'yes' or "YES" to the question 'Do you like brunch time?'.
else: #When the above condition about userBrunch is not met, this 'else-statement' is run. 
    print("Moving on...") #This prints out 'Nice, me too!' if the user answers 'Yes' in the console log. 

userLunch = input("Do you like lunch time?: ") #This creates a variable called userLunch and it asks the user "Do you like lunch time?" 
if(userLunch == "yes" or userLunch == "YES" or userLunch == "Yes"): #This creates a conditional 'if-statement' that checks if the user likes lunch time  using the user's input of 'yes' or 'YES' or 'Yes' if they like lunch time. 
     print("I love lunch time too!") #When the above condition is met, this prints out 'I love lunch time too!' if the user answers 'yes' or 'YES' or 'Yes'. 
else: #This 'else-statement' is run when the above condition is not met. 
     print("Oh, I see.") #When the above conditions are not met, an 'else-statement' is run and this prints out 'Oh, I see.'.


userCafe = input("On a scale of 1-3, how much do you like cafe shops?: ") #This creates a variable called 'userCafe' and it asks for the user to enter their rating of cafe shops.

cafeRand = random.randint(1,3) #This creates a variable called 'cafeRand' and it assigns a random number between 1 and 3 to it usingthe random's file library. 
if cafeRand == 1: #This creates a condition 'if-statement' that checks if the random number generated is equal to 1. 
    print("I like "+ userCafe + " too!") #This prints out 'I like' along with the user's favorite cafe shop if the random number generated is equal to 1. 

elif cafeRand == 2: #This creates a condition 'if-statement' that checks if the random number generated is equal to 2.
    print("Have you tried the new drink at " + userCafe + "?") #This prints out 'Have you tried the new drink at' along with the user's favorite cafe shop if the random number generated is equal to 2.

elif cafeRand == 3: #This creates a condition 'if-statement' that checks if the random number generated is equal to 3.
    print("Cafe shops are awesome to visit!") #This prints out 'Cafe shops are awesome to visit!' if the random number generated is equal to 3. 

else: #This 'else-statement' is run when the above conditions are not met.
    ("Alright, Let's move on.") #This prints out 'Alright, Let's move on.' if the random number generated is not equal to 1, 2, or 3. 


userStop = print("Alrighty, " + userName + " stopped at their favorite shop to buy a shirt and a pant.") #This creates a variable called 'userStop' and it prints out 'Alrighty,' along with the user's name and 'stopped at their favorite shop to buy a shirt and a pant. 
import math #This imports the math file library.
num1 = float(input("What was the cost of your shirt?: ")) #This creates a variable called 'num1' and it asks the user to enter the cost of their shirt.
num2 = float(input("What was the cost of your pant?: ")) #This creates a variable called 'num2' and it asks the user to enter the cost of their pant.
sum = num1 + num2 #This calculates addition
print("The total cost of " + str(num1) + " and "+ str(num2) + " is: " + str(sum)) #This prints out the total cost of the user's shirt and pant.

userRate = input("Rate your day on a scale of 1-5?: ") #This creates a variable called 'userRate' and it asks the user to rate their day on a scale of 1-5.
userScale = random.randint(1,5) #This creates a variable called 'userScale' and it includes random number between 1 and 5 to it using the random's file library.
if userScale == 1: #This creates a condition 'if-statement' that checks if the random number generated is equal to 1.
    print("Oh no, I'm sorry to hear.") #This prints out 'Oh no, I'm sorry to hear.' if the random number generated is equal to 1.

elif userScale == 2: #This creates a condition 'if-statement' that checks if the random number generated is equal to 2.
    print("Oh, I hope you have a better day!") #This prints out 'Oh, I hope you have a better day!' if the random number generated is equal to 2.

elif userScale == 3: #This creates a condition 'if-statement' that checks if the random number generated is equal to 3.
    print("Nice, your day was a mix of a good day and a bad day!") #This prints out 'Nice, your day was a mix of a good day and a bad day' if the random number generated is equal to 3.

elif userScale == 4: #This creates a condition 'if-statement' that checks if the random number generated is equal to 4.
    print("Awesome to hear!") #This prints out 'Awesome to hear!' if the random number generated is equal to 4.

elif userScale == 5: #This creates a condition 'if-statement' that checks if the random number generated is equal to 5.
    print("Fantastic, I had a great day too!") #This prints out 'Fantastic, I had a great day too!' if the random number generated is equal to 5.

else: #This 'else-statement' is run when the above conditions are not met.
    print("Not within the rating scale! Try again!") #This prints out 'Not within the rating scale! Try again!' if the random number the user inputted is not equal to 1, 2, 3, 4, or 5.

print("Goodbye. Unitl next time!") #This prints out 'Goodbye. Unitl next time!' at the end of the code. 


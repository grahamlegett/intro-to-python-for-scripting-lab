# Problem 1: Vowel or consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and 
#   determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user in the above
#   messages.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels. You may need to look up
#   how to use this online.
# - Ensure your code provides feedback for non-alphabetical or invalid entries.

def check_letter():
    # Your control flow logic goes here
    CAPS_my_list = ["Q","W","R","T","Y","P","S","D","F","G","H","J","K","L","Z","X","C","V","B","N","M"]
    my_list_lower = ["q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    vowel_list = ["a","e","i","o","u","A","E","I","O","U"]
    letter_check = input("Enter a letter from a-z not case sensitive: ")
    print(type(letter_check))
    if letter_check in CAPS_my_list:
        print("The letter "); print(letter_check); print(" is a consonant")
    elif letter_check in my_list_lower:
        print("The letter "); print(letter_check); print(" is a consonant") 
    elif letter_check in vowel_list:
        print("The letter "); print(letter_check); print(" is a vowel")
    else:
        print("INVALID ENTRY")
    


# Call the function
check_letter()

# Problem 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a
# user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative 
#   numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting
#   age.
# - Print a message indicating whether the user is eligible to vote based on the
#   entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure that you handle any 
#   conversion errors gracefully. You may need to look up how to do this online.
# - Use a conditional statement to check if the age meets the minimum voting age
#   requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    voting_age = 18
    age = input("Please enter your age: ")
    try:
        entered_age = int(age)
    except ValueError as e:
        print(f"Error: {e}"); 

    if entered_age > 0 and entered_age <= 17:
        print("You are NOT eligible to vote!")
    elif entered_age > 0 and entered_age >= voting_age:
        print("You ARE eligible to vote!")
    else: 
        print("INVALID ENTRY!!")  
              



# Call the function
check_voting_eligibility()

# Problem 3: Calculate dog years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's
# age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the
#   dog's age.

def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = input("Enter dog's age: ")
    try:
        dog_entered = int(dog_age)
    except ValueError as e:
        print(f"Error: {e}");   
    if dog_entered > 0 and dog_entered > 2:
        year_dog = ((10 * 2) + ((dog_entered - 2) * 7))
        print("The dog's age in dog years is: ")
        print(year_dog)
    elif dog_entered < 2 and dog_entered > 0:
        print("The dog is 10 years old in dog years")
    else:
        print("Sorry to say you don't have a dog")

# Call the function
calculate_dog_years()
# Problem 4: Weather advice
#
# Write a Python script named `weather_advice` that provides clothing advice
# based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle
#   multiple conditions.

def weather_advice():
    # Your control flow logic goes here
    cold_answer = input("Is it cold out (yes or no): ")
    rain_answer = input("Is it raining (yes or no): ")
    if cold_answer == "yes" and rain_answer == "yes":
        print("Wear a waterproof coat!")
    elif cold_answer == "yes" and rain_answer == "no":
        print("Wear a warm coat!")
    elif cold_answer == "no" and rain_answer == "yes":
        print("Carry an umbella!")
    else:
        print("Wear light clothing!!")


# Call the function
weather_advice()
# Problem 5: What's the season?
#
# Write a Python function named `determine_season` that figures out the season
# based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three
#   characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month:
#   "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in
#   <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure you validate the user's input and handle unexpected inputs
#   gracefully.

def determine_season():
    # Your control flow logic goes here
    winter_months = ["Jan","jan","Feb","feb","Mar","mar"]
    spring_months = ["Apr","apr","May","may","Mar","mar","Jun","jun"]
    fall_months = ["Oct","oct","Nov","nov","Sep","sep","Dec","dec"]
    summer_months = ["Jul","jul","Aug","aug","Jun","jun","Sep","sep"]
   # months = ["Jan","jan","Feb","feb","Apr","apr","May","may","Oct","oct","Nov","nov","Jul","jul","Aug","aug"]
    other_dates = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,23,24,25,26,27,28,29,30,31]
    mon_enter = input("Enter the month of the year using 3 charater Abreviation (Jan - Dec): ")
    day_enter = input("Enter the day of the month: ")
    try:
        day = int(day_enter)
    except ValueError as e:
        print(f"Error: {e}"); 
    
    
    if day == 21 and mon_enter == "Dec":
        print(mon_enter, day, " Winter")
    elif day == 19 and mon_enter == "Mar":
        print(mon_enter, day, " Winter")
    elif day == 21 and mon_enter == "dec":
        print(mon_enter, day, " Winter")
    elif day == 19 and mon_enter == "mar":
        print(mon_enter, day, " Winter")
    elif day == 20 and mon_enter == "Mar":
        print(mon_enter, day, " Spring")
    elif day == 20 and mon_enter == "Jun":
        print(mon_enter, day, " Spring")
    elif day == 20 and mon_enter == "mar":
        print(mon_enter, day, " Spring")
    elif day == 20 and mon_enter == "jun":
        print(mon_enter, day, " Spring")
    elif day == 21 and mon_enter == "Jun":
        print(mon_enter, day, " Summer")
    elif day == 21 and mon_enter == "Sep":
        print(mon_enter, day, " Summer")
    elif day == 21 and mon_enter == "jun":
        print(mon_enter, day, " Summer")
    elif day == 21 and mon_enter == "sep":
        print(mon_enter, day, " Summer")
    elif day == 22 and mon_enter == "Sep":
        print(mon_enter, day, " Fall")
    elif day == 20 and mon_enter == "Dec":
        print(mon_enter, day, " Fall")
    elif day == 22 and mon_enter == "sep":
        print(mon_enter, day, " Fall")
    elif day == 20 and mon_enter == "dec":
        print(mon_enter, day, " Fall")
    elif mon_enter in winter_months and day in other_dates:
        print(mon_enter, day, " Winter")
    elif mon_enter in spring_months and day in other_dates:
        print(mon_enter, day, " Spring")
    elif mon_enter in fall_months and day in other_dates:
        print(mon_enter, day, " Fall")
    elif mon_enter in summer_months and day in other_dates:
        print(mon_enter, day, " Summer!!")
    else:
        print("INVALID MONTH ENTRY!!!")
    
    
    
    
    
    
    
# Call the function
determine_season()
# Exercise 6: Number guessing game
#
# Write a Python function named `guess_number` that allows a user to guess a
# predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give
#   the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do
#   not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate
#   feedback.

def guess_number():
    # Your control flow logic goes here
    fixed = 23
    for i in range(3):
        entered = input("Enter a number from 1 - 100: ")
        try:
            guess = int(entered)
        except ValueError as e:
            print(f"Error: {e}"); 
        if guess == fixed:
            print("Congratulations you guessed right!!")
        elif guess > fixed:
            print("Too high try again")
        elif guess < fixed:
            print("Too low try again")
    last_try = input("Last TRY!!!: ")
    try:
       last_guess = int(last_try)
    except ValueError as e:
        print(f"Error: {e}"); 
        if last_guess == fixed:
            print("That was close but you got it!")
        else:
            print("Sorry you fal to guess in five attempts")




# Call the function
guess_number()

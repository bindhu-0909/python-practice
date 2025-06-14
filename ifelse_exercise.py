# given the age of bindhu and jeevan write a function that tells  who is elder

print("====================================")
print("Welcome to my Age Finder App! :)")
print("====================================")

person_1 = int(input("Please enter 1st person birth year: ")) 
person_2 = int(input("Please enter 2nd person birth year: "))

current_year = 2025

'''
Cases:
1. First person can be elder - Done
2. Second person can be elder - Done
3. Both can be of the same age
'''

def age_finder(birth_year):
    age = current_year - birth_year
    return age 

def eldest(first_person_year, second_person_year):

    # coverting person year to person age

for this:

    first_person_age = age_finder(first_person_year)
    second_person_age = age_finder(second_person_year)
     
    # find who is older
    # using found age from above for the if else logic
    if first_person_age < second_person_age:
        print("Second person is the eldest")
    elif first_person_age > second_person_age:
        print("First person is the eldest")
    else:
        print("Both are of same age")    

    # Age difference
    diffrence = abs(first_person_age - second_person_age) #abs() gives the positive difference 
    print(f"The age between them is {diffrence} years.")

    # Option to stop or continue
    choice = input("Do you want to ckeck again? (yes/no): ")
    if choice.lower() != 'yes':
        print("Thank you for using Age Finder App!")
        break     # exit the loop

eldest(person_1, person_2)

'''
Improvements:
1. App should not exit
2. Add name and age difference to the result
'''
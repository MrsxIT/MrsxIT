# Python user input practice - please remember I am a beginner so be kind when sending any edits through. Thank you!
# Please feel free to correct any errors I have made, & I am open to advice and guidance, too.

user_details = {}

name = input("What is your name? ")
print(f"Hello {name}, nice to meet you!")
user_details["name"] = name

birth_year = int(input("What year were you born? "))
if birth_year == 2024:
    print("Sorry, your answer is invalid. Please try again.")
    exit ()
elif birth_year < 1900 or birth_year > 2024:
    print("The birth year you entered is invalid. Please try again.")
    exit()
else:
    age = 2024 - birth_year
    print(f"Thank you, {name}. You are {age} years old.")
    user_details["birth year"] = birth_year
    user_details["age"] = age

occupation = input("What is your occupation?")
print(f"Thank you, {name}. Your occupation is {occupation}")
user_details["occupation"] = occupation

country = input("What country do you live in?")
print("Wow! You live in {country}!")
user_details["country"] = country

hobbies = input("What are you hobbies?")
print("Impressive hobbies!")
user_details["hobbies"] = hobbies

children_count = int(input("How many children do you have?"))
if children_count == 0:
    print(f"Thank you, {name}. You are {age} years old and you have no children.")
    user_details["children_count"] = children_count
else:
    children_data = []
    for i in range(children_count):
        child_name = input(f"Please enter the name of your child {i + 1}: ")
        child_age = int(input(f"How old is {child_name}? "))
        child_birth_year = 2024 - child_age
        child_school = input(f"Which school does {child_name} go to?")
        child_fav_activity = input(f"What is {child_name}'s favourite activity?")
        children_data.append({
            "name": child_name,
            "age": child_age,
            "birth_year": child_birth_year,
            "child_school": child_school,
            "child_fav_activity": child_fav_activity
        })
    
    user_details["children"] = children_data
    print(f"Thank you, {name}. You are {age} years old and you have {children_count} children.")
    print(f"Here are the details of your children:")
    for child in children_data:
        print(f"{child['name']}: {child['age']} years old (Born in {child['birth_year']}).")
        print(f"They attend {child['child_school']}, and loves {child['child_fav_activity']}.")
    print("\nSummary of your details:")
    for key, value in user_details.items():
        if key == "children":
            print("Children:")
            for child in value:
                print(f"{child['name']}: {child['age']} years old (Born in {child['birth_year']}).")
        else:
            print(f"{key.capitalize()}: {value}")
    print(f"You also live in {country}, your occupation is {occupation} and your hobbies are {hobbies}!")

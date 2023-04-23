gender = input("What is your gender (M or F): ")
first = input("First name: ")
last = input("Last name: ")
age = input("Age: ")
age = int(age)
if gender == "F":
    if age >= 20:
        marriage = input("Are you married, " + first +" Y/N: ")
        if marriage == "Y":
            print("Then i shall call you Mrs " + last)
        elif marriage == "N":
            print("Then i shall call you Ms " + first)
    elif age < 20:
        print(first + " " + last)



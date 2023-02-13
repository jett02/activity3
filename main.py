# HEADER
# Jett Phillips
# ISQA 3900 Web Application Development
# Due: 2/12/23
# The purpose of this program is to create a functioning grading calculator that uses the users input to output
# a letter grade from points the user enters between 0 and 1000.



# This defines what the title of the program is...later will be used to output in main.
def display_title():
    print('Welcome to the Grade Calculator')

# this function promts to user for and reads the total points earned.
# if the user enters in a value that is less than 0 or greater than 1000 it will report the error and ask the user to
# type in a new value.
def get_totalPoints(totalpoints):
    return totalpoints

# This function takes the average grade from main and returns the letter grade based on the averageEarned.
def get_letterGrade(averageEarned):
    letter_grade = ''
    if 92.0 <= averageEarned <= 100.0:
        letter_grade = "A"
    elif 88.0 <= averageEarned <= 91.99:
        letter_grade = "B+"
    elif 82.0 <= averageEarned <= 87.99:
        letter_grade = "B"
    elif 78.0 <= averageEarned <= 81.99:
        letter_grade = "C+"
    elif 70.0 <= averageEarned <= 77.99:
        letter_grade = "C"
    elif 60.0 <= averageEarned <= 69.99:
        letter_grade = "D"
    elif averageEarned < 60.0:
        letter_grade = "f"

    return letter_grade
# this function calls the title, points, percentage of grade, and gives letter grade.
# also uses try and except to pass alphabetical values through a print statement requiring integers.
def main():
    display_title()
    print()
    choice = "y"
    while choice.lower() == 'y':
        bool_variable = True
        while bool_variable:
            try:
                total_points = int(input("Enter the total score(0-1000):"))
            except:
                print("You must enter an integer value >=0 and <=1000. Try again.")
                continue
            if 0<= total_points <=1000:
                averageEarned = float(total_points/1000*100)
                format_float = "{:.1f}".format(averageEarned)
                str_output = "You earned an average of " + format_float + "%. Letter grade earned:" + get_letterGrade(averageEarned)
                print(str_output)
                print()
                choice = input("Would you like to enter another score (y/n)?: ")
                print()
                bool_variable = False
            else:
                print("You must enter an integer value >=0 and <=1000. Try again.")
                print()
    if choice == "n":
        print("Thank you.")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

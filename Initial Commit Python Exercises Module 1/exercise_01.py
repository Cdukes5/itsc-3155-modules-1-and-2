#Collin Dukes
def main():
    #Gets grade input
    grade = int(input('Enter a grade from 0 to 100: '))
    #Uses grade in a function to determine letter grade
    letter_grade(grade)

#Defines letter grade function
def letter_grade(score):
    if (score < 60 and score >= 0):
        print('Your grade is an F.')
    elif (score >= 60 and score <= 69):
        print('Your grade is a D.')
    elif (score >= 70 and score <= 79):
        print('Your grade is a C.')
    elif (score >= 80 and score <= 89):
        print('Your grade is a B.')
    elif (score >=90 and score <= 100):
        print('Your grade is an A.')
    else:
        print('Error: you have not entered a number between 0 and 100.')
    return score
main()
#Collin Dukes
def main():
    #Take in an integer greater than 1. Print out the cubes of each integer from 0 to the inputted integer.
    int1 = int(input('Enter an integer greater than 1: '))
    str1 = 'The cube of {} is {}'
    #For loop to determine the cube of each number to inputted integer
    for i in range(0, int1 + 1):
        print(str1.format(i,i**3))
main()
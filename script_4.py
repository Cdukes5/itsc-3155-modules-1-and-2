#Collin Dukes
def main():
    i = 0
    sum = 0
    str1 = "Enter int #{}: "
    str2 = "Your sum is {}"

    while i < 5:
        add = (input(str1.format(i+1)))

        #Switch for input validation by attempting to cast input as an int
        try:
            int(add)
            it_is = True
        #If there is an error in the try statement then except will execute
        except ValueError:
            it_is = False
        #Input validation. Asks the user to enter a valid int input
        while (it_is == False):
            print("Invalid input. Please enter an int.")
            add = (input(str1.format(i+1)))
            try:
                int(add)
                it_is = True
            except ValueError:
                it_is = False
        #Add the input to the sum each time the loop runs then add 1 to the iterator. Cast the input string as an int.
        sum = sum + int(add)
        i = i + 1
    print(str2.format(sum))
main()
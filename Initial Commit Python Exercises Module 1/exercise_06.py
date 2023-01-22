#Collin Dukes
def main():
    #Take in a row number from 1 to 5 inclusive and a column number from 1 to 5. Print out a grid of 0s, but in the row and column entered by the user, print a 1.
    row1 = int(input('Enter a row num from 1 to 5: '))
    col1 = int(input('Enter a col num from 1 to 5: '))
    #Subtracts 1 since index only goes to 4
    row1 = row1 - 1
    col1 = col1 - 1
    #Creates list of 5 rows
    list1 = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    #String to format
    str1 = '{} {} {} {} {}'
    #Sets input row and column to 1
    list1[row1][col1] = 1
    #For loop to print the grid
    for i in range(5):
            print(str1.format(list1[i][0], list1[i][1], list1[i][2], list1[i][3], list1[i][4]))
main()
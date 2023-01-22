#Collin Dukes
def main():
    #Take in integers until the user types "QUIT" and store the numbers in a list. 
    #Assume any input other than "QUIT" is a valid integer. Create another list of just the even numbers and print both lists.
    list1 = []
    list2 = []
    str1 = ''
    str2 = 'All nums: {}'
    str3 = 'Even nums: {}'
    while(str1 != 'QUIT'):
        str1 = input('Enter a number or QUIT to quit: ')
        if (str1 != 'QUIT'):
            #print(type(str1))
            #Changes str to int when appended to list
            list1.append(int(str1))
            #Checks if number is even then appends to list 2
            if ((int(str1) % 2) == 0):
                list2.append(int(str1))
    #Prints lists
    print(str2.format(list1))
    print(str3.format(list2))
main()
#Collin Dukes
def main():
    #Take in a string from the user and split it into an array of single characters. 
    #Split the list of characters into a list of lists where each inner list has 3 elements. Notice that the last inner array may have less than 3 elements.
    list1 = list(input('Enter a string: '))
    list2 = []
    #For loop to append 3 characters to each index of a list
    for i in range(0, len(list1), 3):
        #Begins at 0 and runs to the length of the list, i iterates by 3 each time it runs.
        #List 2 appends from list 1 slicing 3 characters at a time
        list2.append(list1[i:i+3])
    print(list2)
main()
#Collin Dukes
def main():
    #Take in 5 integers from the user and store them in a list. Then take in another 5 integers and store them in a separate list. 
    #Create a third array containing the common values from both arrays without duplicates. Print out all three lists.
    str1 = 'Enter a number for the first list: '
    str2 = 'Enter a number for the second list: '
    str3 = 'First list: {}'
    str4 = 'Second list: {}'
    str5 = 'Common list: {}'
    list1 = []
    list2 = []
    list3 = []
    #First list for loop
    for i in range(5):
        list1.append(int(input(str1)))
    #Second list for loop
    for i in range(5):
        list2.append(int(input(str2)))
    #Uses intersection to create a list of common values
    list3 = set(list1).intersection(list2)
    #Prints the lists
    print(str3.format(list1))
    print(str4.format(list2))
    print(str5.format(list3))
main()
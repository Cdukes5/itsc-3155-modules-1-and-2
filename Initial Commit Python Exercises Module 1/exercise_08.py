#Collin Dukes
def main():
    #Take in 10 integers from user. Create a new list with only elements which appear once. Print both lists.
    list1 = []
    list2 = []
    str1 = 'Enter number {}: '
    str2 = 'Original list: {}'
    str3 = 'Nums that appear once: {}'
    for i in range(10):
        int1 = (int(input(str1.format(i + 1))))
        #Appends to the first list
        list1.append(int1)
        #Checks the first list and appends or removes from the second list accordingly
        if (list1.count(int1) == 1):
            list2.append(int1)
        elif (list1.count(int1) == 2):
            list2.remove(int1)
    print(str2.format(list1))
    print(str3.format(list2))
main()
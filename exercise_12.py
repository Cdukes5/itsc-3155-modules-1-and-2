#Collin Dukes
def main():
    lowercase = []
    uppercase = []
    list1 = list(input('Enter a string: '))
    #Loop through the input list using the length and use if statements to append lowercase and uppercase letters into separate lists
    for i in range(len(list1)):
        if (list1[i] >= 'A' and list1[i] <= 'Z'):
            uppercase.append(list1[i])
        elif (list1[i] >= 'a' and list1[i] <= 'z'):
            lowercase.append(list1[i])
        #Combined both lists https://www.w3schools.com/python/gloss_python_join_lists.asp
        list2 = lowercase + uppercase
    #Use join without a separator to turn the list into a string https://www.w3schools.com/python/ref_string_join.asp
    print(''.join(list2))
main()
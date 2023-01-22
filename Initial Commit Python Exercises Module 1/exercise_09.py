#Collin Dukes
def main():
    #Take in 5 words from the user and store them in a list. Then, create a single string from the individual words, separated by spaces, and print the list and resultant string.
    list1 = []
    str2 = 'Words: {}'
    str3 = 'One string: {} {} {} {} {}'
    for i in range(5):
        str1 = str(input('Enter a word: '))
        list1.append(str1)
    print(str2.format(list1))
    print(str3.format(list1[0],list1[1],list1[2],list1[3],list1[4]))
main()
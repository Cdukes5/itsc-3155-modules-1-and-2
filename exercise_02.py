#Collin Dukes
def main():
    #Gets two string inputs
    string1 = str(input('Enter a string: '))
    string2 = str(input('Enter another string: '))
    #Uses endswith method to determine if suffix
    var1 = string2.endswith(string1)
    var2 = string1.endswith(string2)
    if (var1 == True or var2 == True):
        print('True')
    else:
        print('False')
main()
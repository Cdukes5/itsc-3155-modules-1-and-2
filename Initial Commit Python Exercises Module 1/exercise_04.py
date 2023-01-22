#Collin Dukes
def main():
    #Take in a number, n, from the user. Then, take in n floats from the user and store them in a list. 
    #For instance, if the user enters 4, then the user will have to enter 4 numbers. Print the list and the mean.
    int1 = int(input('Enter a number: '))
    float1 = 0
    list1 = []
    str1 = 'Enter number {}: '
    str2 = 'Average: {}'
    #For loop using input number to iterate
    for i in range (int1):
        #Appends each number to the list
        list1.append(float(input(str1.format(i + 1))))
        float1 += list1[i]
    print(list1)
    #Calculates average of the numbers
    print(str2.format(float1/int1))
main()
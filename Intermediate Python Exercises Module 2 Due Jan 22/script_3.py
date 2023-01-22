#Collin Dukes
def main():
    def count_dict(str1):
        #Make the string lowercase
        str1 = str1.lower()
        #Remove spaces
        str1 = str1.replace(" ", "")
        dict1 = {}  
        #For loop to count the letters
        for i in str1:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        return dict1

    str2 = "hello world"
    print(count_dict(str2))
main()
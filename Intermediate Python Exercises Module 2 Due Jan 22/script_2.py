#Collin Dukes
def main():
    def get_combined_dict(my_dict_1, my_dict_2):

        dict1 = {}
        #Compares the keys in both dictionaries and adds the values together if the key is in both
        for key, value in my_dict_1.items():
            if (key in my_dict_2.keys()):
                dict1[key] = value + my_dict_2[key]
        
        return dict1
    #Creates two dictionaries and combines them using the function then prints the output
    my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
    my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}

    combined_dict = get_combined_dict(my_dict_1, my_dict_2)

    print(combined_dict)
main()
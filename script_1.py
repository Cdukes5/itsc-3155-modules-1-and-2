#Collin Dukes
def main():
    list1 = [1,2,3,2,1,4]
    #Function to take in list as an input
    def get_unique_list(my_list):
        
        list2 = []
        
        #loop through the list and append unique ints to list2 
        for i in (list1):
            if i not in (list2):
                list2.append(i)
        #Return the unique list
        return list2
    unique_list = get_unique_list(list1)
    print(unique_list)
main()
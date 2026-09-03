def print_and_sum_list_of_lists(main_list):
    """
    This function takes a big main list of smaller lists.
    It prints what is inside each small list using a list-1, list-2 format.
    Then it adds up all the numbers it finds.
    """
    total = 0
    counter = 1
    
    # Go through the main list one sub-list at a time
    for sub_list in main_list:
        print("list-" + str(counter), "contains elements", sub_list)
        counter = counter + 1
        
        # Look at each single item inside the sub-list
        for single_item in sub_list:
            if type(single_item) is int or type(single_item) is float:
                total = total + single_item
                
    print("Total sum of numbers in the list:", total)
    return total        


def print_and_sum_dict_of_dicts(main_dictionary):
    """
    This function takes a big main dictionary of smaller sub-dictionaries.
    It prints what is inside each sub-dictionary using a dictionary_1, dictionary_2 format.
    Then it adds up all the values that are numbers.
    """
    total = 0
    counter = 1
    
    # Go through the main dictionary labels one by one
    for key_name in main_dictionary:
        sub_dictionary = main_dictionary[key_name]
        print("dictionary_" + str(counter), "contains elements", sub_dictionary)
        counter = counter + 1
        
        # Look at each specific key inside this sub-dictionary
        for item_key in sub_dictionary:
            actual_value = sub_dictionary[item_key]
            if type(actual_value) is int or type(actual_value) is float:
                total = total + actual_value
                
    print("Total sum of numbers in the dictionary:", total)
    return total    

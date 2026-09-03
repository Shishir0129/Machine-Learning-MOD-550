from tools import print_and_sum_list_of_lists, print_and_sum_dict_of_dicts

my_main_list = [
    [2, "apple", 1, "egg"],    
    ["mushroom", 3, "bread"]        
]

my_main_dictionary = {
    "Monday": {"apple": 3, "egg": 1},   
    "Tuesday": {"banana": 2, "mushroom": 4}   
}

    print("--- TESTING THE WEEKLY MEALS LIST ---")
    print_and_sum_list_of_lists(my_main_list)
    
    print("\n--- TESTING THE FRIDGE INVENTORY DICTIONARY ---")
    print_and_sum_dict_of_dicts(my_main_dictionary)

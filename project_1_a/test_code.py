# 1. Bring in our custom tools functions to check them
from tools import print_and_sum_list_of_lists, print_and_sum_dict_of_dicts

def run_our_code_tests():
    print("--- INITIATING SYSTEM ASSERTION TESTS ---")
    
    # 2. Setup a basic list of lists that we can easily add up in our heads
    # The numbers inside are 5, 2, and 3. The math total must be 10.
    sample_test_list = [
        [5, "apple"],
        [2, 3, "banana"]
    ]
    
    # Run the list function and save the total number it hands back to us
    calculated_list_total = print_and_sum_list_of_lists(sample_test_list)
    
    # Use assert to see if our function answer matches our head math (10)
    assert calculated_list_total == 10
    print("List calculation checks out perfectly!")


    # 3. Setup a basic dictionary of dictionaries that we can easily add up
    # The numbers inside are 20 and 30. The math total must be 50.
    sample_test_dictionary = {
        "Monday": {"eggs": 20, "milk": "one carton"},
        "Tuesday": {"bread": 30}
    }
    
    # Run the dictionary function and save the total number it hands back to us
    calculated_dict_total = print_and_sum_dict_of_dicts(sample_test_dictionary)
    
    # Use assert to see if our function answer matches our head math (50)
    assert calculated_dict_total == 50
    print("Dictionary calculation checks out perfectly!")

# This small loop makes Python fire off our test checklist automatically
if __name__ == "__main__":
    run_our_code_tests()
    print("\nSUCCESS: All tests completed with zero errors!")

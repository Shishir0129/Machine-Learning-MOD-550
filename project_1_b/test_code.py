"""
THIS IS MY TESTING SHEET FOR THE FRIDGE ASSIGNMENT (Part_1_b)
This file is an automatic checklist that tests our fridge code.
It uses the word 'assert' to check if our rules work right and if 
our math loop adds up numbers correctly, making sure there are no errors.
"""
from tools import check_fridge_power, add_up_all_power

def run_my_automated_tests():
    print("--- INITIATING SYSTEM ASSERTION TESTS ---")
    
    assert check_fridge_power(2.0, "closed") == 0
    
    assert check_fridge_power(5.0, "closed") == 1
    
    assert check_fridge_power(3.5, "open") == 2
    
    assert check_fridge_power(10.0, "closed") == 3
    
    print("All fridge temperature tests passed successfully!")
    
    sample_power_data = 

    calculated_math_total = add_up_all_power(sample_power_data)
    
    assert calculated_math_total == 6
    
    print("The power addition loop test passed successfully!")

if __name__ == "__main__":
    run_my_automated_tests()
    print("\nSUCCESS: All tests completed with zero errors!")

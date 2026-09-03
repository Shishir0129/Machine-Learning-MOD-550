def check_fridge_power(fridge_temp, door_is):
    """
    This program figures out the cooling work level for a fridge.
    
    My Everyday Assumptions:
    1. door_is can only be written as the text "open" or "closed".
    2. fridge_temp is the real number thermometer reading inside.
    3. The outcome is a speed step from 0 up to 3:
       - Step 0: Everything is shut tight and chilled down (4 degrees or under).
       - Step 1: Shut tight but creeping up slightly (between 4 and 8 degrees).
       - Step 2: Door left wide open but still holding some chill (6 degrees or under).
       - Step 3: Wide open and warm, OR spiking past a risky 8 degrees no matter what.
    """
   
    if fridge_temp > 8:
        return 3
        
    if door_is == "open":
        if fridge_temp > 6:
            return 3
        else:
            return 2
            
    if door_is == "closed":
        if fridge_temp > 4:
            return 1
        else:
            return 0


def add_up_all_power(list_of_readings):
    """
    This program takes an entry log sheet of energy values over time.
    It counts through them one by one to find the absolute final usage sum.
    """
    running_total = 0
    
    for single_reading in list_of_readings:
        running_total = running_total + single_reading
        
    return running_total

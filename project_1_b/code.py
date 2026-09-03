"""
THIS IS MY MAIN CODE SHEET FOR THE FRIDGE ASSIGNMENT (Part_1_b)
This file takes our 7-hour kitchen tracking numbers and checks them.
It uses our homemade rules from tools.py to find out the total energy score, 
and then it draws two easy charts on the screen.
"""

import matplotlib.pyplot as chart_maker
from tools import check_fridge_power, add_up_all_power

hours_tracked = [1, 2, 3, 4, 5, 6, 7]
fridge_temperatures = [3.2, 3.9, 5.1, 7.8, 5.6, 9.4, 3.5]
fridge_door_positions = ["closed", "closed", "closed", "open", "open", "closed", "closed"]

hourly_power_results = []
line_number_on_our_data_sheet = 0

for one_temperature in fridge_temperatures:
    one_door_position = fridge_door_positions[line_number_on_our_data_sheet]
    
    calculated_power_level = check_fridge_power(one_temperature, one_door_position)
    hourly_power_results.append(calculated_power_level)
    
    line_number_on_our_data_sheet = line_number_on_our_data_sheet + 1

running_total_history_list = []
current_running_total_sum = 0

for one_power_result in hourly_power_results:
    current_running_total_sum = current_running_total_sum + one_power_result
    running_total_history_list.append(current_running_total_sum)

grand_total_power_used = add_up_all_power(hourly_power_results)
print("==============================")
print("TOTAL POWER USED BY THE FRIDGE OVER ALL HOURS:", grand_total_power_used)
print("==============================")

chart_maker.figure(figsize=(11, 5))

chart_maker.subplot(1, 2, 1)
chart_maker.plot(hours_tracked, hourly_power_results, color="indigo", marker="o", linestyle="--")
chart_maker.title("Power Levels Changing Hour by Hour")
chart_maker.xlabel("Hours Recorded")
chart_maker.ylabel("Power Setting (0 to 3)")
chart_maker.grid(True)

chart_maker.subplot(1, 2, 2)
chart_maker.plot(hours_tracked, running_total_history_list, color="darkorange", marker="x", linestyle="-")
chart_maker.title("Total Energy Accumulating Over Time")
chart_maker.xlabel("Hours Recorded")
chart_maker.ylabel("Accumulated Power Units")
chart_maker.grid(True)

chart_maker.tight_layout()
chart_maker.show()


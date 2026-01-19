# Energy Consumption
# Given the number of Calories burned during a workout, and the number of watt-hours used by your electronic devices during that workout, determine which one used more energy.

# To compare them, convert both values to joules using the following conversions:

# 1 Calorie equals 4184 joules.
# 1 watt-hour equals 3600 joules.
# Return:

# "Workout" if the workout used more energy.
# "Devices" if the device used more energy.
# "Equal" if both used the same amount of energy.

def compare_energy(calories_burned, watt_hours_used):

    calories_burned = calories_burned * 4184
    watt_hours_used = watt_hours_used * 3600

    if calories_burned == watt_hours_used:
        return "Equal"
    elif calories_burned > watt_hours_used:
        return "Workout"
    elif calories_burned < watt_hours_used:
        return "Devices"

    
print(compare_energy(250, 50))
print(compare_energy(100, 200))
print(compare_energy(450, 523))
print(compare_energy(300, 75))
print(compare_energy(200, 250))
print(compare_energy(900, 1046))
        
"""
Plant the Crop
Given an integer representing the size of your farm field, and "acres" or "hectares" representing the unit for the size of your farm field, and a type of crop, determine how many plants of that type you can fit in your field.

1 acre equals 4046.86 square meters.
1 hectare equals 10,000 square meters.
Here's a list of crops that will be given as input and how much space a single plant takes:

Crop	Space per plant
"corn"	1 square meter
"wheat"	0.1 square meters
"soybeans"	0.5 square meters
"tomatoes"	0.25 square meters
"lettuce"	0.2 square meters
Return the number of plants that fit in the field, rounded down to the nearest whole plant.

"""
def get_number_of_plants(field_size, unit, crop):

    # Classify the field_size between the unit that is defined in the call
    if unit == "acres":
        field_size = field_size * 4046.86

    elif unit == "hectares":
        field_size = field_size * 10000
    
    # Based on the crop devide the field_size to be able to calculate the number of plants that fit in the specified field_size using switch case
    match crop:
        case "corn":
            return int(field_size / 1)
        case "wheat":
            return int(field_size / 0.1)
        case "soybeans":
            return int(field_size / 0.5)
        case "tomatoes":
            return int(field_size / 0.25)
        case "lettuce":
            return int(field_size / 0.2)

    
    return field_size


# Test Case
print(get_number_of_plants(1, "acres", "corn") )
print(get_number_of_plants(2, "hectares", "lettuce") )
print(get_number_of_plants(20, "acres", "soybeans")) 
print(get_number_of_plants(3.75, "hectares", "tomatoes"))
print(get_number_of_plants(16.75, "acres", "tomatoes")) 


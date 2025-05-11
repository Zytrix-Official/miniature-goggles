# Dictionary with conversion factors to kg
conversion_factors = dict(g=1, kg=1000)
#asks the user about the weight
weight = float(input("Enter the weight:"))
unit = (input("Enter the unit:"))
unit2 = (input("Enter the unit you want to convert to:"))
#Check if units are valid
if unit in conversion_factors and unit2 in conversion_factors:
    # Convert type1 to g, then to type2
    convert = weight * conversion_factors[unit]
    converted_weight = convert / conversion_factors[unit2]
    print(f"Converted weight: {converted_weight} {unit2}")




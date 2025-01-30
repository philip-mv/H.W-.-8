def calculate_power(base, exponent):
    """
    This function calculates the power of a base number raised to a given exponent. 
    
    Args:
        base: The base number.
        exponent: The exponent to raise the base to.
    
    Returns:
        The result of base raised to the power of exponent.
    """
    result = base ** exponent
    return result

# Get user input
base_num = float(input("Enter the base number: "))
exponent_num = float(input("Enter the exponent: "))

# Calculate the power
power = calculate_power(base_num, exponent_num)

# Print the result
print(f"{base_num} raised to the power of {exponent_num} is: {power}")
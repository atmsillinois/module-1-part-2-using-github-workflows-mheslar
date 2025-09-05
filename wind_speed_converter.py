'''Program to convert a user input of wind speed in mph to knots or m/s'''

def wind_speed_converter_mph(val, output_unit):
    """
    Convert wind speed from mph to m/s or knots.
    
    Parameters:
    val (float): The wind speed in mph
    output_unit (str): Requested unit ['m/s', 'knots']
    
    Returns:
    float: Converted wind speed value
    """
    
    # Convert through mph to requested unit
    if output_unit == 'm/s': 
      return val * 0.44704
    if output_unit == 'knots': 
      return val * 0.86898

a = float(input('What is your wind speed in mph?'))
b = input('What unit of wind speed would you like? m/s or knots')

print(wind_speed_converter_mph(a, b))




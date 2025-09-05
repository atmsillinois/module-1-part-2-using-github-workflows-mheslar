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
    if output_unit is 'm/s': 
      return val * 0.44704
    if output_unit is 'knots': 
      return val * 0.86898




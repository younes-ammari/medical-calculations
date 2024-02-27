def calculate_map(systolic_bp, diastolic_bp):
    """
    Calculate the Mean Arterial Pressure (MAP) using the formula: MAP = (2 * Diastolic BP + Systolic BP) / 3

    Parameters:
    - systolic_bp: Systolic blood pressure in mmHg
    - diastolic_bp: Diastolic blood pressure in mmHg

    Returns:
    - MAP value in mmHg
    """
    map_value = (2 * diastolic_bp + systolic_bp) / 3
    return map_value

# Example usage:
systolic_bp = 120  # in mmHg
diastolic_bp = 80  # in mmHg

map_value = calculate_map(systolic_bp, diastolic_bp)
print("Mean Arterial Pressure (MAP):", map_value, "mmHg")

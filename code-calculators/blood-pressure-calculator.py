def calculate_blood_pressure(systolic, diastolic):
    """
    Calculate mean arterial pressure (MAP) based on systolic and diastolic blood pressure.

    Parameters:
    - systolic: Systolic blood pressure (mmHg)
    - diastolic: Diastolic blood pressure (mmHg)

    Returns:
    - Mean arterial pressure (MAP) (float)
    """
    if systolic <= 0 or diastolic <= 0:
        raise ValueError("Blood pressure values must be greater than zero")

    map_pressure = (systolic + (2 * diastolic)) / 3
    return map_pressure

# Example usage:
systolic_pressure = 120 # mmHg
diastolic_pressure = 80 # mmHg

try:
    map_pressure = calculate_blood_pressure(systolic_pressure, diastolic_pressure)
    print("Mean Arterial Pressure (MAP):", map_pressure, "mmHg")
except ValueError as e:
    print("Error:", e)

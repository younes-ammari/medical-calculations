def calculate_sbp(map, dbp):
    """
    Calculate systolic blood pressure (SBP) from mean arterial pressure (MAP) and diastolic blood pressure (DBP).

    Parameters:
    - map: Mean arterial pressure in mmHg
    - dbp: Diastolic blood pressure in mmHg

    Returns:
    - Systolic blood pressure (SBP) in mmHg (float)
    """
    if map <= dbp:
        raise ValueError("Mean arterial pressure must be greater than diastolic blood pressure")

    sbp = (2 * map) - dbp
    return sbp

# Example usage:
mean_arterial_pressure = 90 # in mmHg
diastolic_blood_pressure = 70 # in mmHg

try:
    sbp = calculate_sbp(mean_arterial_pressure, diastolic_blood_pressure)
    print("Systolic Blood Pressure (SBP):", sbp, "mmHg")
except ValueError as e:
    print("Error:", e)

def calculate_sirs(temp, respiratory_rate, heart_rate, white_blood_cell_count):
    """
    Calculate the Systemic Inflammatory Response Syndrome (SIRS) score based on criteria.

    Parameters:
    - temp: Patient's temperature in Celsius
    - respiratory_rate: Patient's respiratory rate in breaths per minute
    - heart_rate: Patient's heart rate in beats per minute
    - white_blood_cell_count: Patient's white blood cell count in cells/mm^3

    Returns:
    - SIRS score
    """
    sirs_score = 0

    # Temperature criteria
    if temp < 36 or temp > 38:
        sirs_score += 1

    # Respiratory rate criteria
    if respiratory_rate > 20:
        sirs_score += 1

    # Heart rate criteria
    if heart_rate > 90:
        sirs_score += 1

    # White blood cell count criteria
    if white_blood_cell_count < 4000 or white_blood_cell_count > 12000:
        sirs_score += 1

    return sirs_score


# Example usage:
temp = 37.5
respiratory_rate = 25
heart_rate = 100
white_blood_cell_count = 15000

sirs_score = calculate_sirs(temp, respiratory_rate,
                            heart_rate, white_blood_cell_count)
print("SIRS Score:", sirs_score)

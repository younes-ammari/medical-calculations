def calculate_egfr(creatinine, age, is_male):
    """
    Calculate the estimated Glomerular Filtration Rate (eGFR) using the MDRD formula.

    Parameters:
    - creatinine: Serum creatinine level in mg/dL
    - age: Patient's age in years
    - is_male: Boolean indicating if patient is male (True) or female (False)

    Returns:
    - eGFR value
    """
    if is_male:
        k = 186 if creatinine <= 0.9 else 186 * \
            (creatinine ** -1.154) * (age ** -0.203)
    else:
        k = 141 if creatinine <= 0.7 else 141 * \
            (creatinine ** -1.154) * (age ** -0.203) * 0.742
    return k


# Example usage:
creatinine = 1.2  # in mg/dL
age = 50  # in years
is_male = True

egfr = calculate_egfr(creatinine, age, is_male)
print("eGFR:", egfr, "mL/min/1.73m²")

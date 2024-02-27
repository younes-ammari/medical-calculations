def estimate_crcl(serum_creatinine_mg_dl, weight_kg, age, sex):
    """
    Estimates Creatinine Clearance (CrCl) using the Cockcroft-Gault formula.

    Parameters:
    - serum_creatinine_mg_dl: Serum creatinine level in mg/dL
    - weight_kg: Weight in kilograms
    - age: Age in years
    - sex: String ("male" or "female")

    Returns:
    - Estimated CrCl in milliliters per minute (mL/min) (float)

    Raises:
    - ValueError: If sex is not "male" or "female"
    - ZeroDivisionError: If serum creatinine or weight is zero
    """

    if sex.lower() not in ("male", "female"):
        raise ValueError("Invalid sex. Please enter 'male' or 'female'.")

    if serum_creatinine_mg_dl <= 0 or weight_kg <= 0:
        raise ZeroDivisionError("Serum creatinine and weight must be positive values.")

    constant = 140  # Constant value in the Cockcroft-Gault formula
    if sex.lower() == "female":
        constant *= 0.85  # Adjustment factor for females

    try:
        crcl = ((constant - age) * weight_kg) / (72 * serum_creatinine_mg_dl)
    except ZeroDivisionError:
        raise ZeroDivisionError("Serum creatinine cannot be zero.")

    # Cap the estimated CrCl at a maximum value
    crcl = min(crcl, 120)  # Maximum estimated CrCl

    return crcl

# Example usage
serum_creatinine = 1.2  # Serum creatinine level in mg/dL
weight = 70  # Weight in kilograms
age = 35
sex = "male"

try:
    estimated_crcl = estimate_crcl(serum_creatinine, weight, age, sex)
    print("Estimated CrCl:", estimated_crcl, "mL/min")
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

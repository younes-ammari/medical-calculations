def calculate_bmr(weight_kg, height_cm, age, sex):
    """
    Calculates Basal Metabolic Rate (BMR) using different formulas based on sex.

    Parameters:
    - weight_kg: Weight in kilograms
    - height_cm: Height in centimeters
    - age: Age in years
    - sex: String ("male" or "female")

    Returns:
    - BMR in kilocalories (kcal) per day (float)

    Raises:
    - ValueError: If sex is not "male" or "female"
    - ZeroDivisionError: If height is zero
    """

    if sex.lower() not in ("male", "female"):
        raise ValueError("Invalid sex. Please enter 'male' or 'female'.")

    height_m = height_cm / 100
    if height_m == 0:
        raise ZeroDivisionError("Height cannot be zero.")

    if sex.lower() == "male":
        bmr = 88.362 + 13.397 * weight_kg + 4.799 * height_m - 5.677 * age
    else:
        bmr = 447.593 + 9.247 * weight_kg + 3.098 * height_m - 4.330 * age

    return bmr

# Example usage:
weight = 70  # in kilograms
height = 175  # in centimeters
age = 30
sex = "female"

try:
    bmr = calculate_bmr(weight, height, age, sex)
    print("Basal Metabolic Rate (BMR):", bmr, "kcal/day")
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

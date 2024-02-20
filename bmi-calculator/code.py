def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.

    Parameters:
    - weight: Person's weight in kilograms
    - height: Person's height in meters

    Returns:
    - BMI value
    """
    bmi = weight / (height ** 2)
    return bmi


def interpret_bmi(bmi):
    """
    Interpret the Body Mass Index (BMI) according to standard categories.

    Parameters:
    - bmi: Body Mass Index (BMI) value

    Returns:
    - Interpretation string
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# Example usage:
weight = 70  # in kilograms
height = 1.75  # in meters

bmi = calculate_bmi(weight, height)
interpretation = interpret_bmi(bmi)

print("BMI:", bmi)
print("Interpretation:", interpretation)

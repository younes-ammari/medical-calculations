def calculate_body_surface_area(height_cm, weight_kg):
    """
    Calculate body surface area (BSA) using the Mosteller formula.

    Parameters:
    - height_cm: Height in centimeters
    - weight_kg: Weight in kilograms

    Returns:
    - Body surface area (BSA) in square meters (float)
    """
    if height_cm <= 0 or weight_kg <= 0:
        raise ValueError("Height and weight must be greater than zero")

    height_m = height_cm / 100
    bsa = (height_m * weight_kg) ** 0.5 * 71.84 / 10000
    return bsa

# Example usage:
height = 175 # in centimeters
weight = 70 # in kilograms

try:
    bsa = calculate_body_surface_area(height, weight)
    print("Body Surface Area (BSA):", bsa, "m^2")
except ValueError as e:
    print("Error:", e)

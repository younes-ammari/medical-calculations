def classify_bmi(bmi_float):
  """
  Classifies BMI based on WHO guidelines.

  Parameters:
    - bmi_float: Body mass index (float)

  Returns:
    - String representing BMI category
  """

  if bmi_float < 18.5:
    return "Underweight"
  elif bmi_float < 25:
    return "Normal weight"
  elif bmi_float < 30:
    return "Overweight"
  else:
    return "Obese"

# Example usage
bmi = 24.5  # BMI value
category = classify_bmi(bmi)
print("BMI Category:", category)

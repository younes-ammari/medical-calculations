def check_fever(temperature_celsius):
  """
  Checks for potential fever based on a basic threshold.

  Parameters:
    - temperature_celsius: Body temperature in Celsius (float)

  Returns:
    - String indicating potential fever
  """

  fever_threshold = 38  # Celsius

  if temperature_celsius >= fever_threshold:
    return "Potential fever detected. Please consult a healthcare professional for further evaluation."
  else:
    return "Normal temperature."

# Example usage
temperature = 37.5  # Body temperature in Celsius
fever_status = check_fever(temperature)
print(fever_status)

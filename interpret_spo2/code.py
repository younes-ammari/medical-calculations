def interpret_spo2(spo2_percent):
  """
  Provides a basic interpretation of SpO2 level.

  Parameters:
    - spo2_percent: Oxygen saturation level in percentage (int)

  Returns:
    - String interpretation of SpO2 level
  """

  if spo2_percent > 95:
    return "Normal SpO2 level."
  elif spo2_percent >= 90:
    return "SpO2 level is slightly low. Monitor and consult a healthcare professional if further symptoms arise."
  elif spo2_percent >= 85:
    return "SpO2 level is moderately low. Seek medical attention immediately."
  else:
    return "SpO2 level is severely low. Emergency medical attention is crucial."

# Example usage
spo2 = 92  # SpO2 level in percentage
interpretation = interpret_spo2(spo2)
print(interpretation)

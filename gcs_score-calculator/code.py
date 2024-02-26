def calculate_gcs_score(eye_opening, verbal_response, motor_response):
    """
    Calculate Glasgow Coma Scale (GCS) score.

    Parameters:
    - eye_opening: Numeric score for eye opening (int)
    - verbal_response: Numeric score for verbal response (int)
    - motor_response: Numeric score for motor response (int)

    Returns:
    - Glasgow Coma Scale (GCS) score (int)
    """
    gcs_score = eye_opening + verbal_response + motor_response
    return gcs_score

# Example usage:
eye_opening_score = 4
verbal_response_score = 5
motor_response_score = 6

gcs = calculate_gcs_score(eye_opening_score, verbal_response_score, motor_response_score)
print("GCS Score:", gcs)

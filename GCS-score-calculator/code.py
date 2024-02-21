def calculate_gcs(eye_opening, verbal_response, motor_response):
    """
    Calculate the Glasgow Coma Scale (GCS) score based on eye opening, verbal response, and motor response.

    Parameters:
    - eye_opening: Score for eye opening (integer: 1-4)
    - verbal_response: Score for verbal response (integer: 1-5)
    - motor_response: Score for motor response (integer: 1-6)

    Returns:
    - GCS score (integer: 3-15)
    """
    # Validate input scores
    if not (1 <= eye_opening <= 4):
        raise ValueError("Eye opening score must be between 1 and 4")
    if not (1 <= verbal_response <= 5):
        raise ValueError("Verbal response score must be between 1 and 5")
    if not (1 <= motor_response <= 6):
        raise ValueError("Motor response score must be between 1 and 6")

    # Calculate GCS score
    gcs_score = eye_opening + verbal_response + motor_response
    return gcs_score

# Example usage:
eye_opening_score = 4
verbal_response_score = 5
motor_response_score = 6

try:
    gcs_score = calculate_gcs(eye_opening_score, verbal_response_score, motor_response_score)
    print("Glasgow Coma Scale (GCS) Score:", gcs_score)
except ValueError as e:
    print("Error:", e)

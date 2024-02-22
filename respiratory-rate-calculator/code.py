def calculate_respiratory_rate(breaths, duration_seconds):
    """
    Calculate the average respiratory rate (breaths per minute) based on the number of breaths and duration.

    Parameters:
    - breaths: Number of breaths
    - duration_seconds: Duration in seconds

    Returns:
    - Average respiratory rate (float)
    """
    if breaths <= 0:
        raise ValueError("Number of breaths must be greater than zero")
    if duration_seconds <= 0:
        raise ValueError("Duration must be greater than zero")

    respiratory_rate = (breaths / duration_seconds) * 60
    return respiratory_rate

# Example usage:
breaths = 240
duration = 120 # in seconds

try:
    avg_respiratory_rate = calculate_respiratory_rate(breaths, duration)
    print("Average Respiratory Rate (BPM):", avg_respiratory_rate)
except ValueError as e:
    print("Error:", e)

def calculate_heart_rate(beats, duration_minutes):
    """
    Calculate the average heart rate (beats per minute) based on the number of beats and duration.

    Parameters:
    - beats: Number of heart beats
    - duration_minutes: Duration in minutes

    Returns:
    - Average heart rate (float)
    """
    if beats <= 0:
        raise ValueError("Number of beats must be greater than zero")
    if duration_minutes <= 0:
        raise ValueError("Duration must be greater than zero")

    heart_rate = beats / duration_minutes
    return heart_rate

# Example usage:
beats = 350
duration = 10 # in minutes

try:
    avg_heart_rate = calculate_heart_rate(beats, duration)
    print("Average Heart Rate (BPM):", avg_heart_rate)
except ValueError as e:
    print("Error:", e)

def classify_blood_pressure(systolic, diastolic):
    if systolic < 90 or diastolic < 60:
        return "Hypotension"
    elif systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    elif 130 <= systolic < 140 or 80 <= diastolic < 90:
        return "Hypertension Stage 1"
    else:
        return "Hypertension Stage 2"

# Example usage:
systolic_bp = 120
diastolic_bp = 80

classification = classify_blood_pressure(systolic_bp, diastolic_bp)
print("Blood Pressure Classification:", classification)

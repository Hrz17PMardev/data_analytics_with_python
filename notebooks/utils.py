def age_group_label(age, minor_threshold=30, senior_threshold=60):
    if age < minor_threshold:
        return "Minor"
    elif age < senior_threshold - 1:
        return "Middle-aged"
    else:
        return "Senior"


def income_band(income, low=80000, high=170000):
    if income < low:
        return "Low"
    elif income <= high:
        return "Medium"
    else:
        return "High"
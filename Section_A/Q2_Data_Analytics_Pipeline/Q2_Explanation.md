# Input
Student dataset containing:
    Student ID  
    Name
    Department
    Attendance
    Diary Entries
    Tasks Completed
    Assignment Score
    Lab Score

# Process
    Validate the dataset.
    Check for missing values.
    Replace missing numeric values with 0.
    Calculate the readiness score.
    Classify each student into a performance band.
    Generate department-wise analytics.

# Decision Conditions
    Score < 45 → Support
    45–69 → Developing
    70–89 → Strong
    90 and above → Excellent

# Loop Structure
    Use a FOR loop to process each student record.

# Output
    Cleaned dataset
    Readiness score
    Performance band
    Department average
    Top performer
    Students needing support
    Three insights

# Edge Cases
    Dataset is empty.
    Required columns are missing.
    Numeric values are missing.
    Attendance or task values are 0.
def determine_band(score):
    if score < 40:
        band = "Support"
    elif score < 70:
        band = "Developing"
    elif score < 90:
        band = "Strong"
    else:
        band = "Excellent"
        
    return band

# Test the scores from our dry run
test_scores = [38, 62, 81, 94]

for score in test_scores:
    result = determine_band(score)
    print(f"Score: {score} -> Band: {result}")
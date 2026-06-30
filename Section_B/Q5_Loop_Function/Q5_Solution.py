def readiness_score(attendance_pct, diary_entries, tasks_completed):
    score = 0

    score += attendance_pct * 0.5
    score += min(diary_entries, 14) / 14 * 25
    score += min(tasks_completed, 10) / 10 * 25

    if attendance_pct < 50:
        score -= 10
    elif attendance_pct >= 90 and tasks_completed >= 8:
        score += 5

    return max(0, min(round(score, 2), 100))
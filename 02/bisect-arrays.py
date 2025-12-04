import bisect

scores = [81, 68, 53, 91, 90, 82, 76, 71, 84]
breakpoints = [60, 70, 80, 90]
grades = "FDCBA"


def calculate_grade_simple(score):
    if score <= 60:
        return "F"
    elif score <= 70:
        return "D"
    elif score <= 80:
        return "C"
    elif score <= 90:
        return "B"
    else:
        return "A"


def calculate_grade(score):
    i = bisect.bisect_left(breakpoints, score)
    return grades[i]


scored_grades = [calculate_grade(score) for score in scores]
print("scores:", scores)
print("grades (bisect):", scored_grades)

scored_grades_simple = [calculate_grade_simple(score) for score in scores]
print("grades (simple):", scored_grades_simple)

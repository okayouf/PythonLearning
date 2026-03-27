# ============================================
# 11. Student Grade Tracker & Analyzer
# ============================================
# A complete project combining ALL concepts:
#   - Variables and data types
#   - Data structures (list, dict, tuple, set)
#   - Control flow (if/elif/else, for loops)
#   - Functions (def, return, docstrings, raise)
#   - Lambda functions
#   - Iterators (enumerate, zip)
#   - List & dict comprehensions
#   - Generators (expressions and functions)
#   - Pandas chunking
# ============================================
import pandas as pd


# --- Task 1: Variables & Data Types ---
name = "Yael Cohen"
scores = [92, 78, 88]
average_score = round(sum(scores) / len(scores), 1)
print(average_score)
passed = True

print(type(name))
print(type(scores))
print(type(average_score))
print(type(passed))


# --- Task 2: Data Structures ---
students = ["Yael Cohen", "Noam Levy", "Tamar Shapira", "Ori Mizrahi", "Dana Peretz", "Eitan Katz"]
names_scores = {"Yael Cohen": 92, "Noam Levy": 65, "Tamar Shapira": 95, "Ori Mizrahi": 45, "Dana Peretz": 83, "Eitan Katz": 71}
subjects = ("Math", "English", "Science")
student_names = {"Yael Cohen", "Noam Levy", "Tamar Shapira", "Ori Mizrahi", "Dana Peretz", "Eitan Katz"}


# --- Task 3: Control Flow ---
for name, grade in names_scores.items():
    if grade >= 90:
        print(name, "- Grade: A")
    elif grade >= 80:
        print(name, "- Grade: B")
    elif grade >= 70:
        print(name, "- Grade: C")
    elif grade >= 60:
        print(name, "- Grade: D")
    else:
        print(name, "- Grade: F")


# --- Task 4: Functions ---
def get_grade(score):
    """Returns the letter grade as a string ("A", "B", "C", "D", or "F")"""
    if type(score) != int and type(score) != float:
        raise TypeError("Score must be a number")
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print(get_grade(85))


# --- Task 5: Lambda, Enumerate, Zip ---
math_scores = [92, 65, 95, 45, 83, 71]
pass_or_fail = lambda score: "Pass" if score >= 60 else "Fail"

for index, name in enumerate(students, start=1):
    print(index, name)

for name, score in zip(students, math_scores):
    print(name, score)


# --- Task 6: List & Dict Comprehensions ---
scores_above_70 = [score for score in math_scores if score > 70]
print(scores_above_70)

pass_fail = ["Pass" if score >= 60 else "Fail" for score in math_scores]
print(pass_fail)

graded = {student: get_grade(score) for student, score in zip(students, math_scores)}
print(graded)


# --- Task 7: Generators ---
gen_grades = ("Pass" if score >= 60 else "Fail" for score in math_scores)
print(next(gen_grades))
print(next(gen_grades))

def grade_students(names, scores):
    for name, score in zip(names, scores):
        yield name, ":", get_grade(score)

for result in grade_students(students, math_scores):
    print(result)


# --- Task 8: Pandas Chunking ---
total = 0
for chunk in pd.read_csv('students.csv', chunksize=10):
    total += sum(chunk['score'])
print(total)


# --- Task 9: Putting It All Together ---
def class_report(filename):
    """Generates a full class report from a CSV file of student scores."""
    try:
        df = pd.read_csv(filename)
        unique_names = list(set(df['name']))
        report = {}
        for name in unique_names:
            student_scores = df[df['name'] == name]['score']
            average = sum(student_scores) / len(student_scores)
            report[name] = get_grade(round(average))
        print(report)
    except:
        print("File not found")

class_report('students.csv')

name = "Yael Cohen"
scores = [92, 78, 88]
average_score = round(sum(scores) / len(scores), 1)
passed = True

print(type(name))
print(type(scores))
print(type(average_score))
print(type(passed))

students = ["Yael Cohen","Noam Levy","Tamar Shapira","Ori Mizrahi","Dana Peretz","Eitan Katz"]
math_scores = {"Yael Cohen" : 92 ,"Noam Levy" : 65,"Tamar Shapira" : 95 ,"Ori Mizrahi": 45 ,"Dana Peretz" : 83,"Eitan Katz" : 71}
subjects = ("Math","English","Science")
student_names = {"Yael Cohen","Noam Levy","Tamar Shapira","Ori Mizrahi","Dana Peretz","Eitan Katz"}

for name,grade in math_scores.items():
    if grade >= 90:
        print(name,"- Grade: A")
    elif grade >= 80:
        print(name,"- Grade: B")
    elif grade >= 70:
        print(name,"- Grade: C")
    elif grade >= 60:
        print(name,"- Grade: D")
    else:
        print(name,"- Grade: F")

def get_grade(score):
    """Returns the letter grade as a string ("A", "B", "C", "D", or "F")"""
    if type(score) != int and type(score) != float:
        raise TypeError("Score must be a number")
    if score >= 90:
        return  "A"
    elif score >= 80:
        return  "B"
    elif score >= 70:
        return  "C"
    elif score >= 60:
        return  "D"
    else:
        return  "F"
print(get_grade(85))
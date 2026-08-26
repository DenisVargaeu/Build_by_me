score = 0
grade = 0 

def check (score):
    if score >= 90:
        grade = "Excellent"
    elif score >= 75:
        grade = "Very Good"
    elif score >= 50:
        grade = "Good"
    elif score >= 0:
        grade = "Faild"
    print (f"Your score is {score} and your grade is {grade}") 
check (float(input("Please input your score: ")))
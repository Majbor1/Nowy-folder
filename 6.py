import json

def f(years, course, avg_grades):
    with open('data.json', 'r') as file:
        data = json.load(file)
    
    count = 0
    for student in data:
        if student["age"] >= years:
            for c in student["studies"]["courses"]:
                if c["name"] == course:
                    avg = sum(c["grades"]) / len(c["grades"])
                    if avg >= avg_grades:
                        count += 1
                        break
    return count
    
        
        
print(f(21, "statistics", 4))
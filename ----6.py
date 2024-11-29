import json

def f(years, avg_grades):
    json_file = open('data.json', 'r', encoding='utf-8')
    ludz = json.load(json_file)
    json_file.close()
        
    return type(ludz)
        
        
print(f(5, 16))
import re

def f(arr):
    
    pattern = r'^[a-z0-9_]{4,12}$'
        
    matches = 0
    for word in arr:
        if re.match(pattern, word):
            matches += 1
    
    return matches
            
print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
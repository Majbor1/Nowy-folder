def f(arr):
    valid = 'qwertyuiopasdfghjklzxcvbnm_1234567890'
    is_valid = False
    count = 0
    for name in arr:
        for char in name:
            if char in valid:
                is_valid = True
            else:
                is_valid = False
                break
                
            
        if is_valid and len(name) >= 4 and len(name) <= 12:
            count += 1
    return count
            
print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))
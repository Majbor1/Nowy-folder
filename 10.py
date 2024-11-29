def f(arr):
    s_s = []
    for i in arr:
        for j in i:
            s_s.append(j)
            
    smallest = min(s_s)
    
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == smallest:
                if i == j:
                    return True
                else:
                    return False
                
                
print(f([[7,8],[5,3],[9,4]]))
print(f([[7,8,5,3],[9,4,2,6]]))

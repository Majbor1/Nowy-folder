def f(array2D):
    is_True = False
    row1 = 0
    row2 = 0
    row3 = 0
    col1 = 0
    col2 = 0
    col3 = 0
    
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if i == 0:
                row1 += array2D[i][j]
            elif i == 1:
                row2 += array2D[i][j]
            elif i == 2:
                row3 += array2D[i][j]
    
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            if j == 0:
                col1 += array2D[i][j]
            elif j == 1:
                col2 += array2D[i][j]
            elif j == 2:
                col3 += array2D[i][j]
            
    if row1 == col1 and row2 == col2 and row3 == col3:
        return True
    else:
        return False
        
    

if __name__ == "__main__":
    print(f([[3,7,2],[4,2,5],[5,2,1]]) )
    print(f([[3,7,2],[4,2,5],[9,2,1]]) )
def f(array2D):
    is_True = False
    row = 0
    col = 0
    for i in range(len(array2D)):
        for j in range(len(array2D[i])):
            row += array2D[i][j]
            col += array2D[i][0]
    return row, col

if __name__ == "__main__":
    print(f([[3,7,2],
             [4,2,5],
             [5,2,1]]) )
    print(f([[3,7,2],[4,2,5],[9,2,1]]) )
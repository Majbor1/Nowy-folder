def f(player1, player2):
    values1 = 0
    values2 = 0
    
    for char in player1:
        if char in 'AKQJT':
            values1 += 10
        else:
            values1 += int(char)
    
    for char in player2:
        if char in 'AKQJT':
            values2 += 10
        else:
            values2 += int(char)
    
    if values1 >= values2:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(f("AJ972","AQT72") )
    print(f("9532","K8") )

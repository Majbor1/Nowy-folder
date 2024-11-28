def f(arr):
    for i in range(len(arr)):
        if arr[i] != arr[i+1]:
            return arr[i+1]
        
        
if __name__ == "__main__":
    print(f([7,7,7,7,7,5,7,7]))
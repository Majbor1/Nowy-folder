def f(subject):
    avg = []
    for value in subject.values():
        sum = 0
        for grade in value:
            sum += grade
        avg.append(sum/len(value))

    top_avg = max(avg)
    
    i = 0
    for key in subject.keys():
        if top_avg == avg[i]:
            return key
        i += 1

    
if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))    
    
    
    
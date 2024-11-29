import csv

def f(value):
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        count = 0
        for row in csv_reader:
            if int(row[9]) >= value:
                count += 1
                    
    return count


print(f(9200))
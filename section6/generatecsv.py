import csv
import math

numRows = 1000
data = [['number', 'square', 'cube', 'square-root', 'cube-root']]



for i in range(numRows):
    print("Adding row: "+ str(i))
    rowValue = [i, i*i, i**3, i**(1/2), i**(1/3)]
    data.append(rowValue)


with open('demo.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
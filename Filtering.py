import csv
import os
import pandas as pd

os.system('cls')

f = open('Filtered.csv')

r = csv.reader(f)

data = []

for row in r:
    data.append(row)

sData = data[1:]

filteredm = []
filteredr = []
filteredg = []
ind = []

counter = 0
for row in sData:
    if(float(row[3]) <= 350.0 and float(row[3]) >= 150.0):
        filteredm.append(row[1])
        filteredr.append(row[2])
        filteredg.append(row[3])
        counter += 1
        ind.append(counter)


df = pd.DataFrame(list(zip(ind, filteredm, filteredr, filteredg)), columns=[
                  "Index", "Mass", "Radius", "Gravity"])


df.to_csv("Cleaned.csv")

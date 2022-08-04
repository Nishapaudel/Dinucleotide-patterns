import sys
import pandas as pd

file = sys.argv[1]


#file= sys.argv[1]
lyst = []
df = pd.read_csv(file, sep = '\t')
df
for i in df.columns[5:21]:
    #x = df[i].mean()
    y = df[i].median()
    lyst.append(y) 
print(lyst)
#lyst.clear()

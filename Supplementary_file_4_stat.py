import pandas as pd
#file = '/home/nisha/Desktop/Dinucleotide_project/all_vertebrates/Acanthisitta_chloris/Acanthisitta_chloris_exon.txt'
import sys

file= sys.argv[1]
lyst = []
df = pd.read_csv(file, sep = '\t')
df
for i in df.columns[5:21]:
    #x = df[i].mean()
    y = df[i].median()
    lyst.append(y) 
print(lyst)
#lyst.clear()

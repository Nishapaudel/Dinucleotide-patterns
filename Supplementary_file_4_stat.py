import numpy
from scipy import stats
import pandas as pd
import sys
import os

file= sys.argv[1] # The input of the file is the output ratio file from supplementary file 3. and output should look like 'Zerene_cesonia_exon_stat.txt'
df = pd.read_csv(file, sep = '\t')
df
print('Mean','Median','Mode' ,' std', 'var', 'skew', 'kurtosis', sep = '\t')
for i in df.columns[4:20]:
    x = df[i].mean()
    y = df[i].median()
    z = df[i].mode()
    a = df[i].std()
    b = df[i].var()
    c = df[i].skew()
    d = df[i].kurtosis()
    print(x, y ,z ,a, b, c, d, sep = '\t')
    #print(z)

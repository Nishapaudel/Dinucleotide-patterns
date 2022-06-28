

#load libraries
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn import preprocessing
import numpy as np
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
#load data

file = sys.argv[1] # This should contain the meta file that contains median of exon of ratio file....eg of this file plant is z_Plant_meta_file The output figures looks given bellow heat mmap.

df = pd.read_table('file, sep = '\t')
species = df['name']
grouping = df['class']
non_numeric =['name', 'class']
df_numeric = df.drop(non_numeric, axis = 1)
lut = dict(zip(grouping.unique(), [ '#cceeff', '#bf80ff','#ffb3e6',  '#ffe6f7',    '#ff6699','#ff80b3','#000000','#e6b3ff', '#b3b300', '#666633','#e0e0d1' , '#ffb366','#ff8000','#804000','#ffe6cc','#993300','#996600',  '#331a00', '#ff8000','#cc00cc','#ff1a66', '#cc00cc', '#4d0039', '#00ffff', '#ff8000','#ff4d4d','#D033FF' ,'#a0522d', '#999900','#b3ccff'])) #, , , , , '#ffff33']))
row_colors = grouping.map(lut)
legend_patch = []
for x in lut.keys():
    legend_patch.append(mpatches.Patch(color=lut[x], hatch='o', label=x))
sns.set(font_scale = 0.70)

fig = plt.figure(figsize =(60,47))
sns.color_palette()
ax = sns.clustermap(df_numeric, cmap="YlGnBu", col_cluster = False,row_colors = row_colors, yticklabels=species)

plt.legend(handles=legend_patch,loc='right')
plt.savefig('cluster_heatmap.jpg')

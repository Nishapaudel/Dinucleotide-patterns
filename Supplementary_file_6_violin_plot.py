import numpy as np
import holoviews as hv
from holoviews import opts
hv.extension('bokeh')


 
violin_data = sys.argv[1] #The input for this file is output file form supplementary file 5 code.

df = pd.read_csv(violin_data, sep = '\t')

violin = hv.Violin(df, ('Dinucleotide', 'Dinucleotides'), ('ratio', 'Ratio')).redim.range(ratio=(0, 2))

violin = hv.Violin(df, ('Dinucleotide', 'Dinucleotides'), ('ratio', 'Ratio')).redim.range(ratio=(0, 2))
violin.opts(height=500, width=900, violin_fill_color=hv.dim('Dinucleotides').str(), cmap='Set1', title= 'violin_plot')
